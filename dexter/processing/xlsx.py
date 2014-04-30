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

    def build(self):
        """
        Generate an Excel spreadsheet and return it as a string.
        """
        output = StringIO.StringIO()
        workbook = xlsxwriter.Workbook(output)

        self.formats['date'] = workbook.add_format({'num_format': 'yyyy/mm/dd'})

        self.summary_worksheet(workbook)
        self.documents_worksheet(workbook)
        self.sources_worksheet(workbook)
        self.bias_worksheet(workbook)


        workbook.close()
        output.seek(0)

        return output.read()

    def summary_worksheet(self, wb):
        ws = wb.add_worksheet('summary')

        ws.write('D1', 'Generated')
        ws.write_datetime('E1', datetime.now(), self.formats['date'])
        ws.set_column('E:E', 10)

        ws.write('A3', 'Filters')
        ws.write('B4', 'from')
        ws.write('B5', 'to')
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


        ws.write('A10', 'Summary')
        ws.write('A11', 'articles')
        ws.write('B11', self.filter(Document.query).count())

    def documents_worksheet(self, wb):
        from dexter.models.views import DocumentsView

        ws = wb.add_worksheet('documents')
        docs = self.filter(db.session.query(DocumentsView).join(Document)).all()

        if docs:
            keys = docs[0].keys()
            data = [list(doc) for doc in docs]

            ws.add_table(0, 0, len(docs)-1, len(keys)-1, {
                'name': 'Documents',
                'columns': [{'header': k} for k in keys],
                'data': data,
                })

    def sources_worksheet(self, wb):
        from dexter.models.views import DocumentSourcesView

        ws = wb.add_worksheet('sources')
        docs = self.filter(db.session.query(DocumentSourcesView).join(Document)).all()

        if docs:
            keys = docs[0].keys()
            data = [list(doc) for doc in docs]

            ws.add_table(0, 0, len(docs)-1, len(keys)-1, {
                'name': 'Sources',
                'columns': [{'header': k} for k in keys],
                'data': data,
                })

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


    def filter(self, query):
        return self.form.filter_query(query)
