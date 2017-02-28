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


class FDIExportBuilder:
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

        self.investments_worksheet(workbook)

        workbook.close()
        output.seek(0)

        return output.read()

    def investments_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentInvestmentView

        ws = wb.add_worksheet('raw_sources')

        tables = OrderedDict()
        tables['doc'] = DocumentsView
        tables['investment'] = DocumentInvestmentView

        rows = self.filter(db.session
                           .query(*self.merge_views(tables, ['document_id']))
                           .join(Document)
                           .join(DocumentInvestmentView)).all()
        self.write_table(ws, 'Sources', rows)

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
