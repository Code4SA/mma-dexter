import xlsxwriter
import StringIO
from datetime import datetime
from dateutil.parser import parse

from .bias import BiasCalculator
from ..models import Document, db

class XLSXBuilder:
    def __init__(self, form):
        self.form = form
        self.formats = {}

        # we use these to filter our queries, rather than trying to pull
        # complex filter logic into our view queries
        self.doc_ids = [d[0] for d in form.filter_query(db.session.query(Document.id)).all()]

    def build(self):
        """
        Generate an Excel spreadsheet and return it as a string.
        """
        output = StringIO.StringIO()
        workbook = xlsxwriter.Workbook(output)

        self.formats['date'] = workbook.add_format({'num_format': 'yyyy/mm/dd'})
        self.formats['bold'] = workbook.add_format({'bold': True})

        self.summary_worksheet(workbook)
        self.documents_worksheet(workbook)
        self.sources_worksheet(workbook)
        self.bias_worksheet(workbook)
        self.fairness_worksheet(workbook)
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

        ws.write('A7', 'medium')
        if self.form.medium():
            ws.write('B7', self.form.medium().name)

        ws.write('A8', 'user')
        if self.form.user():
            ws.write('B8', self.form.user().full_name())

        ws.write('A9', 'problems')
        if self.form.problems.data:
            ws.write('B9', ', '.join(p.short_desc for p in self.form.get_problems()))


        ws.write('A11', 'Summary', self.formats['bold'])
        ws.write('A12', 'articles')
        ws.write('B12', self.filter(Document.query).count())

    def documents_worksheet(self, wb):
        from dexter.models.views import DocumentsView

        ws = wb.add_worksheet('documents')
        docs = self.filter(db.session.query(DocumentsView).join(Document)).all()
        self.write_table(ws, 'Documents', docs)

    def sources_worksheet(self, wb):
        from dexter.models.views import DocumentSourcesView

        ws = wb.add_worksheet('sources')
        rows = self.filter(db.session.query(DocumentSourcesView).join(Document)).all()
        self.write_table(ws, 'Sources', rows)

    def fairness_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentFairnessView

        ws = wb.add_worksheet('fairness')
        rows = self.filter(db.session.query(DocumentsView, DocumentFairnessView)\
                    .join(Document)\
                    .join(DocumentFairnessView)).all()
        if rows:
            # joining the two views can result in columns with the same name,
            # we simply de-dup them here
            keys = sorted(list(set(rows[0].keys())))
            self.write_table(ws, 'Fairness', rows, keys)

    def everything_worksheet(self, wb):
        from dexter.models.views import DocumentsView, DocumentSourcesView, DocumentFairnessView

        ws = wb.add_worksheet('everything')
        rows = self.filter(db.session.query(DocumentsView, DocumentFairnessView, DocumentSourcesView)\
                    .join(Document)\
                    .join(DocumentFairnessView)\
                    .join(DocumentSourcesView)).all()
        if rows:
            # joining the two views can result in columns with the same name,
            # we simply de-dup them here
            keys = sorted(list(set(rows[0].keys())))
            self.write_table(ws, 'Everything', rows, keys)

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
        ws.write(6, 0, 'bias')

        for i, score in enumerate(scores):
            col = i + 1

            ws.write(0, col, score.group)
            ws.write(1, col, score.oppose)
            ws.write(2, col, score.favour)
            ws.write(3, col, score.discrepancy)
            ws.write(4, col, score.parties)
            ws.write(5, col, score.fair)
            ws.write(6, col, score.score)

    def write_table(self, ws, name, rows, keys=None):
        if rows:
            if not keys:
                keys = rows[0].keys()
                data = [list(doc) for doc in rows]
            else:
                data = []
                for row in rows:
                    info = row._asdict()
                    data.append([info[k] for k in keys])

            ws.add_table(0, 0, len(rows), len(keys)-1, {
                'name': name,
                'columns': [{'header': k} for k in keys],
                'data': data,
                })

    def filter(self, query):
        return query.filter(Document.id.in_(self.doc_ids))
