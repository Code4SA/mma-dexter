from collections import OrderedDict, defaultdict
from itertools import groupby

import xlsxwriter
import StringIO
from datetime import datetime
from dateutil.parser import parse

from sqlalchemy.sql import func
from sqlalchemy.types import Integer

from ..analysis import BiasCalculator
from ..models import Document, AnalysisNature, db


class XLSXExportBuilder:
    def __init__(self, form):
        self.form = form
        self.formats = {}

        # we use these to filter our queries, rather than trying to pull
        # complex filter logic into our view queries
        self.doc_ids = form.document_ids()

    def build(self):
        """
        Generate an Excel spreadsheet and return it as a string.
        """
        output = StringIO.StringIO()
        workbook = xlsxwriter.Workbook(output)

        self.formats['date'] = workbook.add_format({'num_format': 'yyyy/mm/dd'})
        self.formats['bold'] = workbook.add_format({'bold': True})

        self.summary_worksheet(workbook)

        self.origin_worksheet(workbook)
        self.topic_worksheet(workbook)

        if self.form.analysis_nature().nature == AnalysisNature.ELECTIONS:
            self.bias_worksheet(workbook)
            self.fairness_worksheet(workbook)

        if self.form.analysis_nature().nature == AnalysisNature.CHILDREN:
            self.child_focus_worksheet(workbook)
            self.child_gender_worksheets(workbook)
            self.child_race_worksheets(workbook)
            self.child_context_worksheet(workbook)
            self.child_victimisation_worksheet(workbook)
            self.principles_worksheet(workbook)
            self.children_worksheet(workbook)

        self.documents_worksheet(workbook)
        self.sources_worksheet(workbook)
        self.utterances_worksheet(workbook)
        self.places_worksheet(workbook)
        self.keywords_worksheet(workbook)
        self.issues_worksheet(workbook)
        self.everything_worksheet(workbook)

        workbook.close()
        output.seek(0)

        return output.read()

    def summary_worksheet(self, wb):
        ws = wb.add_worksheet('summary')

        ws.write('D1', 'Generated')
        ws.write_datetime('E1', datetime.now(), self.formats['date'])
        ws.set_column('E:E', 10)

        ws.write('A3', 'Filters', self.formats['bold'])
        ws.write('B4', 'from')
        ws.write('C4', 'to')
        ws.set_column('B:C', 10)

        ws.write('A5', 'added')
        if self.form.created_from:
            ws.write_datetime('B5', parse(self.form.created_from, yearfirst=True, dayfirst=True), self.formats['date'])
        if self.form.created_to:
            ws.write_datetime('C5', parse(self.form.created_to, yearfirst=True, dayfirst=True), self.formats['date'])

        ws.write('A6', 'published')
        if self.form.published_from:
            ws.write_datetime('B6', parse(self.form.published_from, yearfirst=True, dayfirst=True), self.formats['date'])
        if self.form.published_to:
            ws.write_datetime('C6', parse(self.form.published_to, yearfirst=True, dayfirst=True), self.formats['date'])

        ws.write('A7', 'analysis')
        if self.form.analysis_nature():
            ws.write('B7', self.form.analysis_nature().name)

        ws.write('A8', 'countries')
        if self.form.countries():
            ws.write('B8', ', '.join(c.name for c in self.form.countries()))

        ws.write('A9', 'medium')
        media = self.form.media()
        if media:
            ws.write('B9', ', '.join(x.name for x in media))

        ws.write('A10', 'user')
        if self.form.user():
            ws.write('B10', self.form.user().full_name())

        ws.write('A11', 'problems')
        if self.form.problems.data:
            ws.write('B11', ', '.join(p.short_desc for p in self.form.get_problems()))

        ws.write('A12', 'keyword search')
        if self.form.q.data:
            ws.write('B12', self.form.q.data)

        ws.write('A13', 'tags')
        if self.form.tags.data:
            ws.write('B13', self.form.tags.data)

        ws.write('A15', 'Summary', self.formats['bold'])
        ws.write('A16', 'articles')
        ws.write('B16', self.filter(Document.query).count())

    def documents_worksheet(self, wb):
        from dexter.models.views import DocumentsView

        ws = wb.add_worksheet('raw_documents')
        docs = self.filter(db.session.query(DocumentsView).join(Document)).all()
        self.write_table(ws, 'Documents', docs)

    def sources_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentSourcesView

        ws = wb.add_worksheet('raw_sources')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['source'] = DocumentSourcesView

        rows = self.filter(db.session
                           .query(*self.merge_views(tables, ['document_id']))
                           .join(Document)
                           .join(DocumentSourcesView)).all()
        self.write_table(ws, 'Sources', rows)

    def utterances_worksheet(self, wb):
        from dexter.models.views import PersonUtterancesView

        ws = wb.add_worksheet('quotations')

        rows = self.filter(db.session.query(PersonUtterancesView).join(Document)).all()
        self.write_table(ws, 'Quotations', rows)

    def issues_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentIssuesView

        ws = wb.add_worksheet('issues')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['issues'] = DocumentIssuesView

        rows = self.filter(db.session
                           .query(*self.merge_views(tables, ['document_id']))
                           .join(Document)
                           .join(DocumentIssuesView)).all()
        self.write_table(ws, 'Issues', rows)

    def keywords_worksheet(self, wb):
        from dexter.models.views import DocumentKeywordsView
        from dexter.models import DocumentKeyword

        ws = wb.add_worksheet('raw_keywords')

        # only get those that are better than the avg relevance
        subq = db.session.query(
            DocumentKeyword.doc_id,
            func.avg(DocumentKeyword.relevance).label('avg'))\
            .filter(DocumentKeyword.doc_id.in_(self.doc_ids))\
            .group_by(DocumentKeyword.doc_id)\
            .subquery()

        rows = db.session.query(DocumentKeywordsView)\
            .join(subq, DocumentKeywordsView.c.document_id == subq.columns.doc_id)\
            .filter(DocumentKeywordsView.c.relevance >= subq.columns.avg)\
            .all()

        self.write_table(ws, 'Keywords', rows)

    def fairness_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentFairnessView

        ws = wb.add_worksheet('fairness')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['fairness'] = DocumentFairnessView

        rows = self.filter(db.session
                           .query(*self.merge_views(tables, ['document_id']))
                           .join(Document)
                           .join(DocumentFairnessView)).all()
        self.write_table(ws, 'Fairness', rows)

    def principles_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentPrinciplesView

        ws = wb.add_worksheet('principles')

        # supported
        rows = self.filter(
            db.session.query(
                DocumentPrinciplesView.c.principle_supported,
                func.count(1).label('count')
            )
            .join(Document)
            .filter(DocumentPrinciplesView.c.principle_supported != None)  # noqa
            .group_by('principle_supported')
        ).all()
        rownum = 3 + self.write_table(ws, 'PrincipleSupported', rows)

        # violated
        rows = self.filter(
            db.session.query(
                DocumentPrinciplesView.c.principle_violated,
                func.count(1).label('count')
            )
            .join(Document)
            .filter(DocumentPrinciplesView.c.principle_violated != None)  # noqa
            .group_by('principle_violated')
        ).all()
        self.write_table(ws, 'PrincipleViolated', rows, rownum=rownum)

        # raw data
        ws = wb.add_worksheet('raw_principles')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['principles'] = DocumentPrinciplesView

        rows = self.filter(
            db.session
            .query(*self.merge_views(tables, ['document_id']))
            .join(Document)
            .join(DocumentPrinciplesView)).all()
        self.write_table(ws, 'Principles', rows)

    def origin_worksheet(self, wb):
        from dexter.models.views import DocumentsView

        ws = wb.add_worksheet('origins')

        query = db.session.query(
            DocumentsView.c.origin,
            func.count(1).label('count')
        )\
            .join(Document)\
            .group_by('origin')
        rows = self.filter(query).all()
        rownum = 3 + self.write_table(ws, 'Origins', rows)

        query = db.session.query(
            DocumentsView.c.origin_group,
            func.count(1).label('count')
        )\
            .join(Document)\
            .group_by('origin_group')
        rows = self.filter(query).all()
        self.write_table(ws, 'OriginGroups', rows, rownum=rownum)

    def topic_worksheet(self, wb):
        from dexter.models.views import DocumentsView

        ws = wb.add_worksheet('topics')

        # topic groups
        rows = self.filter(
            db.session.query(
                DocumentsView.c.topic_group,
                func.count(1).label('count')
            )
            .join(Document)
            .group_by('topic_group')).all()
        rownum = 3 + self.write_table(ws, 'TopicGroups', rows)

        # topics
        rows = self.filter(
            db.session.query(
                DocumentsView.c.topic,
                func.count(1).label('count')
            )
            .join(Document)
            .group_by('topic')).all()
        self.write_table(ws, 'Topics', rows, rownum=rownum)

    def children_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentChildrenView

        ws = wb.add_worksheet('raw_children')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['children'] = DocumentChildrenView

        rows = self.filter(db.session
                           .query(*self.merge_views(tables, ['document_id']))
                           .join(Document)
                           .join(DocumentChildrenView)).all()
        self.write_table(ws, 'Children', rows)

    def child_victimisation_worksheet(self, wb):
        from dexter.models.views import DocumentChildrenView

        ws = wb.add_worksheet('child_secondary_victimisation')

        rows = self.filter(
            db.session.query(
                func.sum(DocumentChildrenView.c.secondary_victim_source == 'secondary-victim-source', type_=Integer).label('secondary_victim_source'),
                func.sum(DocumentChildrenView.c.secondary_victim_identified == 'secondary-victim-identified', type_=Integer).label('secondary_victim_identified'),
                func.sum(DocumentChildrenView.c.secondary_victim_victim_of_abuse == 'secondary-victim-abused', type_=Integer).label('secondary_victim_victim_of_abuse'),
                func.sum(DocumentChildrenView.c.secondary_victim_source_identified_abused == 'secondary-victim-source-identified-abused', type_=Integer).label('secondary_victim_source_identified_abused'),
            )
            .join(Document)).all()
        if not rows:
            return

        d = rows[0]._asdict()
        data = [[k, d[k]] for k in sorted(d.keys(), key=len)]
        ws.add_table(0, 0, len(data), 1, {
            'name': 'ChildSecondaryVictimisation',
            'data': data,
            'columns': [
                {'header': ''},
                {'header': 'count'},
            ]
        })

    def child_focus_worksheet(self, wb):
        from dexter.models.views import DocumentChildrenView

        query = db.session.query(
            DocumentChildrenView.c.child_focused,
            func.count(1).label('count')
        )\
            .join(Document)\
            .group_by('child_focused')
        rows = self.filter(query).all()

        ws = wb.add_worksheet('child_focused')
        self.write_table(ws, 'ChildFocused', rows)

    def child_gender_worksheets(self, wb):
        """
        For documents with child sources, give various breakdowns by gender of
        those children. All reports are source focused, providing counts
        of *sources* in each category.
        """
        from dexter.models.views import DocumentsView, DocumentSourcesView

        # genders
        query = db.session.query(
            DocumentSourcesView.c.gender,
            func.count(DocumentSourcesView.c.document_source_id).label('count')
        )\
            .join(Document)\
            .filter(DocumentSourcesView.c.source_type == 'child')\
            .group_by('gender')
        rows = self.filter(query).all()

        ws = wb.add_worksheet('child_genders')
        self.write_table(ws, 'ChildGenders', rows)
        rownum = len(rows) + 4

        # topics by gender
        query = self.filter(
            db.session.query(
                DocumentsView.c.topic_group,
                DocumentSourcesView.c.gender,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .join(DocumentSourcesView, DocumentsView.c.document_id == DocumentSourcesView.c.document_id)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('topic_group', 'gender')
            .order_by('topic_group'))

        rownum += 3 + self.write_summed_table(ws, 'ChildGenderTopics', query, rownum=rownum)

        # origins by gender
        query = self.filter(
            db.session.query(
                DocumentsView.c.origin,
                DocumentSourcesView.c.gender,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .join(DocumentSourcesView, DocumentsView.c.document_id == DocumentSourcesView.c.document_id)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('origin', 'gender')
            .order_by('origin'))

        rownum += 3 + self.write_summed_table(ws, 'ChildGenderOrigins', query, rownum=rownum)

        # roles by gender
        query = self.filter(
            db.session.query(
                DocumentSourcesView.c.role,
                DocumentSourcesView.c.gender,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('role', 'gender')
            .order_by('role'))

        rownum += 3 + self.write_summed_table(ws, 'ChildGenderRoles', query, rownum=rownum)

        # ages by gender
        query = self.filter(
            db.session.query(
                DocumentSourcesView.c.source_age,
                DocumentSourcesView.c.gender,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('source_age', 'gender')
            .order_by('source_age'))

        rownum += 3 + self.write_summed_table(ws, 'ChildGenderAges', query, rownum=rownum)

        # quoted-vs-non by gender
        query = self.filter(
            db.session.query(
                DocumentSourcesView.c.quoted,
                DocumentSourcesView.c.gender,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('quoted', 'gender')
            .order_by('quoted'))

        self.write_summed_table(ws, 'ChildGenderQuoted', query, rownum=rownum)

    def child_race_worksheets(self, wb):
        """
        For documents with child sources, give various breakdowns by race of
        those children. All reports are source focused, providing counts
        of *sources* in each category.
        """
        from dexter.models.views import DocumentsView, DocumentSourcesView

        # races
        rows = self.filter(
            db.session.query(
                DocumentSourcesView.c.race,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('race')).all()

        ws = wb.add_worksheet('child_races')
        rownum = 3 + self.write_table(ws, 'ChildRace', rows)

        # topics by race
        query = self.filter(
            db.session.query(
                DocumentsView.c.topic_group,
                DocumentSourcesView.c.race,
                func.count(DocumentSourcesView.c.document_source_id).label('count')
            )
            .join(Document)
            .join(DocumentSourcesView, DocumentsView.c.document_id == DocumentSourcesView.c.document_id)
            .filter(DocumentSourcesView.c.source_type == 'child')
            .group_by('topic_group', 'race')
            .order_by('topic_group'))

        self.write_summed_table(ws, 'RaceTopics', query, rownum=rownum)

    def child_context_worksheet(self, wb):
        from dexter.models.views import DocumentChildrenView

        rows = self.filter(
            db.session.query(
                func.sum(DocumentChildrenView.c.basic_context == 'basic-context', type_=Integer).label('basic_context'),
                func.sum(DocumentChildrenView.c.causes_mentioned == 'causes-mentioned', type_=Integer).label('causes_mentioned'),
                func.sum(DocumentChildrenView.c.consequences_mentioned == 'consequences-mentioned', type_=Integer).label('consequences_mentioned'),
                func.sum(DocumentChildrenView.c.solutions_offered == 'solutions-offered', type_=Integer).label('solutions_offered'),
                func.sum(DocumentChildrenView.c.relevant_policies == 'relevant-policies', type_=Integer).label('relevant_policies'),
                func.sum(DocumentChildrenView.c.self_help_offered == 'self-help-offered', type_=Integer).label('self_help_offered'),
            )
            .join(Document)).all()
        if not rows:
            return

        ws = wb.add_worksheet('child_context')

        d = rows[0]._asdict()
        data = [[k, d[k]] for k in d.keys()]
        ws.add_table(0, 0, len(data), 1, {
            'name': 'ChildContext',
            'data': data,
            'columns': [
                {'header': ''},
                {'header': 'count'},
            ]
        })

    def write_summed_table(self, ws, name, query, rownum=0):
        """
        For a query which returns three columns, [A, B, C],
        write a table that uses A as row labels, B values as column
        labels, and C as counts for each.

        The query must return rows ordered by the first column.

        Returns number of rows written, including headers and footers.
        """
        row_label = query.column_descriptions[0]['name']

        # calculate col labels dynamically
        col_labels = set()

        data = OrderedDict()
        for label, rows in groupby(query.all(), lambda r: r[0]):
            data[label or '(none)'] = row = defaultdict(int)

            for r in rows:
                col_label = r[1] or '(none)'
                col_labels.add(col_label)
                row[col_label] = r[2]
                row['total'] += r[2]

        # final column labels
        col_labels = sorted(list(col_labels)) + ['total']
        keys = [row_label] + col_labels

        # decompose rows into a list of values
        data = [[label] + [r[col] for col in col_labels] for label, r in data.iteritems()]

        ws.add_table(rownum, 0, rownum + len(data) + 1, len(keys) - 1, {
            'name': name,
            'total_row': True,
            'columns': [{'header': k, 'total_function': 'sum' if i > 0 else None} for i, k in enumerate(keys)],
            'data': data,
        })

        # number of rows plus header and footer
        return len(data) + 2

    def places_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentPlacesView

        ws = wb.add_worksheet('raw_places')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['places'] = DocumentPlacesView

        rows = self.filter(
            db.session
            .query(*self.merge_views(tables, ['document_id']))
            .join(Document)
            .join(DocumentPlacesView)).all()
        self.write_table(ws, 'Places', rows)

    def everything_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentSourcesView, DocumentFairnessView, DocumentPlacesView

        ws = wb.add_worksheet('raw_everything')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['fairness'] = DocumentFairnessView
        tables['sources'] = DocumentSourcesView
        tables['places'] = DocumentPlacesView

        rows = self.filter(
            db.session
            .query(*self.merge_views(tables, ['document_id']))
            .join(Document)
            .outerjoin(DocumentFairnessView)
            .outerjoin(DocumentSourcesView)
            .outerjoin(DocumentPlacesView)).all()
        self.write_table(ws, 'Everything', rows)

    def bias_worksheet(self, wb):
        ws = wb.add_worksheet('bias')

        calc = BiasCalculator()
        docs = self.filter(calc.get_query()).all()
        scores = calc.calculate_bias_scores(docs, key=lambda d: d.medium.group_name())

        ws.write(1, 0, 'oppose')
        ws.write(2, 0, 'favour')
        ws.write(3, 0, 'discrepancy')
        ws.write(4, 0, 'parties')
        ws.write(5, 0, 'fair')
        ws.write(6, 0, 'final score')

        for i, score in enumerate(scores):
            col = i + 1

            ws.write(0, col, score.group)
            ws.write(1, col, score.oppose)
            ws.write(2, col, score.favour)
            ws.write(3, col, score.discrepancy)
            ws.write(4, col, score.parties)
            ws.write(5, col, score.fair)
            ws.write(6, col, score.score)

        # key
        ws.write(9, 0, 'KEY')
        key = [
            ('Oppose', 'number of stories biased against an entity'),
            ('Favour', 'number of stories biased in favour of an entity'),
            ('Discrepancy', 'difference between the number of stories biased and/or favouring an entity (1 is the ideal score)'),
            ('Parties', 'spread of political party coverage (the better the spread of coverage the better the score - 1 is the ideal score although media are compared against each other'),
            ('Fair', 'percentage of stories that are fair'),
            ('Final score', 'the total weighting of all the scores above. The closer the score is to 1, the better the performance in terms of fairness. This can be used as a percentage.'),
        ]
        for i, item in enumerate(key):
            ws.write(10 + i, 0, item[0])
            ws.write(10 + i, 1, item[1])

    def write_table(self, ws, name, rows, keys=None, rownum=0, colnum=0):
        if rows:
            if not keys:
                keys = rows[0].keys()
                data = [list(doc) for doc in rows]
            else:
                data = []
                for row in rows:
                    info = row._asdict()
                    data.append([info[k] for k in keys])

            ws.add_table(rownum, colnum, rownum + len(rows), colnum + len(keys) - 1, {
                'name': name,
                'columns': [{'header': k} for k in keys],
                'data': data,
            })

        return len(rows) + 1

    def filter(self, query):
        return query.filter(Document.id.in_(self.doc_ids))

    def merge_views(self, tables, singletons=None):
        """
        Merge a name-to-table map into an array of
        aliased column objects that can be used in a query.
        This ensures that if two tables have columns with the
        same name, that they get renamed to be unique.
        The +singletons+ array is a list of column names
        which should only be included once (useful for common PK columns).
        """
        singletons = set(singletons or [])
        included = set()

        # we need to alias columns so they don't clash
        cols = []
        for alias, table in tables.iteritems():
            for col in table.c:
                if col.name not in singletons or col.name not in included:
                    included.add(col.name)
                    cols.append(col.label('%s_%s' % (alias, col.name)))

        return cols
