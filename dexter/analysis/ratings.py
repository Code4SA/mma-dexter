from collections import OrderedDict, defaultdict
from itertools import groupby
from functools import partial

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
import StringIO
from datetime import datetime
from dateutil.parser import parse

from sqlalchemy.sql import func
from sqlalchemy.types import Integer

from ..analysis import BiasCalculator
from ..models import Document, Medium, db, AnalysisNature

r2c = partial(xl_rowcol_to_cell, row_abs=True, col_abs=True)

class ChildrenRatingExport:
    """ This class generates an XLSX export of per-media ratings
    based on stories analysed for the `children` analysis type.
    The produced spreadsheet contais both the final ratings
    and the raw data used to calculate the ratings. This means that
    users can dig into a rating to understand its context.
    The spreadsheet is also live, in that it contains live
    formulas so that a user can customise the ratings if
    required.

    The produced XLSX file has two worksheets:

    Rating: contains weighted per-media ratings across a number
            of different factors.
    Scores: the raw scores for each media used to calculate the
            overall rating.

    Ratings are weighted and can be composed of other ratings.
    For example, consider the rating

        0,500: Are Childrens Rights Respected		
            0,100: Diversity of Roles
            0,200: Rights Respected
            0,700: Information Points	
                0,500: Self-help
                0,500: Child's best interest

    In this case the "Are Childrens Rights Respected" rating
    has a weight of 0.500 and is composed of three sub-ratings,
    each with their own weights. The last rating, "Information Points",
    is in turn made up of weighted sub-ratings.

    A score for each rating is calculated based on the content and
    analysis of all the documents for a medium.
    """

    def __init__(self, doc_ids):
        # we use these to filter our queries, rather than trying to pull
        # complex filter logic into our view queries
        self.doc_ids = doc_ids
        self.formats = {}

        # TODO balance these weights
        self.ratings = [
            [0.500, 'Are Childrens Rights Respected', [
                [0.101, 'Diversity of Roles'],
                [0.267, 'Rights Respected'],
                [0.302, 'Access Codes', [
                    [0.833, 'Abuse 1 True'],
                    [0.167, 'Abuse 1 Not True']]],
                [0.148, 'Information Points', [
                    [0.500, 'Self-help'],
                    [0.500, 'Childs best interest']]]]],
        ]

        # map from a score name to its row in the score sheet
        self.score_row = {}
        self.n_columns = 0

        # collect media headings
        medium_ids = self.filter(db.session.query(func.distinct(Document.medium_id)))
        self.media = Medium.query\
                .filter(Medium.id.in_(medium_ids))\
                .order_by(Medium.name)\
                .all()

        self.n_columns = len(self.media)
        self.score_col_start = 3

        # how nested are the ratings?
        def depth(ratings, deep=1):
            for rating in ratings:
                if len(rating) < 3:
                    yield deep
                else:
                    yield max(depth(rating[2], deep+1))

        # the column at which the ratings for each medium starts
        self.rating_col_start = max(depth(self.ratings)) * 2


    def build(self):
        """
        Generate an Excel spreadsheet and return it as a string.
        """
        output = StringIO.StringIO()

        workbook = xlsxwriter.Workbook(output)

        self.formats['date'] = workbook.add_format({'num_format': 'yyyy/mm/dd'})
        self.formats['bold'] = workbook.add_format({'bold': True})

        # generate the sheets we'll use
        self.rating_ws = workbook.add_worksheet('Rating')
        self.scores_ws = workbook.add_worksheet('Scores')

        self.build_scores_worksheet()
        self.build_rating_worksheet()

        workbook.close()
        output.seek(0)

        return output.read()

    def build_scores_worksheet(self):
        """ Build up the scores worksheet. """
        # TODO:

    def build_rating_worksheet(self):
        """ Build up the rating worksheet. """
        for i, medium in enumerate(self.media):
            self.rating_ws.write(1, self.rating_col(i), medium.name)

        self.add_nested_ratings(self.ratings, row=3, col=0)

    
    def add_nested_ratings(self, ratings, row, col):
        for info in ratings:
            weight, rating = info[0:2]

            self.add_rating(weight, rating, row, col)
            row = row + 1

            if len(info) > 2:
                # sub-ratings
                row = self.add_nested_ratings(info[2], row, col+1)
                row = row + 1

        return row

    def add_rating(self, weight, rating, row, col):
        self.rating_ws.write(row, col  , weight)
        self.rating_ws.write(row, col+1, rating)

        # TODO: indicator for rating
        score_row = self.score_row.get(rating, 5)

        for i in xrange(self.n_columns):
            cell = xl_rowcol_to_cell(row, self.score_col(i), row_abs=True, col_abs=True)
            self.rating_ws.write(row, self.rating_col(i), '=Scores!%s' % cell)

    def score_col(self, i):
        """ The index of the score for the i-th medium """
        return self.score_col_start + i

    def rating_col(self, i):
        """ The index of the rating for the i-th medium """
        return self.rating_col_start + i


    def filter(self, query):
        return query.filter(Document.id.in_(self.doc_ids))

