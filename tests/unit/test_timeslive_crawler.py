import unittest

from dexter.models import Document
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import TimesLiveCrawler

class TestTimesliveCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = TimesLiveCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_extract(self):
        html = """

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <title>TimesLIVE - Print Article</title>
        <link rel="stylesheet" href="http://www.timeslive.co.za/template/common/css/print.css" type="text/css" media="print" />
        <link type="text/css" rel="stylesheet" href="http://www.timeslive.co.za/template/common/css/uniform.default.css" />
        <script type="text/javascript">
            function printpage()
            {
                window.print();
            }
        </script>
    </head>
    <body onload="printpage()">
        <a href="#" onclick="javascript:print();">
            Print this page
        </a><br />
        <div class="container">
            <div class="clear"></div>
            <div id="content">
                <div class="span-24 column">
                    <div class="articleheader">
                        <h1>IEC's Tlakula must resign: opposition parties</h1>
                        <div> Apr 1, 2014 | Sapa</div>
                        <h3>Several opposition parties met in Pretoria on Tuesday to discuss Public Protector Thuli Madonsela's finding on the Nkandla upgrades and the controversy around IEC chairwoman Pansy Tlakula.</h3>
                    </div>

                    <div class="articlerelated">
                        <div class="image">
        <img width="290px" title="" alt="" src="http://www.timeslive.co.za/migration_catalog/ST/2009/09/10/26869_499542.jpg/RESIZED/Small/26869_499542.jpg">
         IEC chairwoman Pansy Tlakula</div>
    <br/>
<div class="quote">
                                <h3>
                                    <span>"</span>
                                    <p> </p><span class="end">"</span>
                                </h3>
                                <div class="clear"></div>
                            </div>
                        </div>
                    <p>Chairman of the multi-party forum Bantu Holomisa, who also heads the United Democratic Movement (UDM), said the opposition parties resolved to push for Tlakula's resignation.</p><p>"All the political parties present, with the exception of the Democratic Alliance and the Freedom Front Plus, agreed that advocate Tlakula must resign immediately.</p><p>"Should she refuse to resign, the parties who are in agreement will pursue legal action," said Holomisa.</p><p>The forum included the African Christian Democratic Party, AgangSA, Azapo, Economic Freedom Fighters, FF Plus, Inkatha Freedom Party, United Christian Democratic Party, and Holomisa's UDM.</p><p>Regarding Nkandla, the parties resolved to convene another summit after President Jacob Zuma had reacted to Parliament as ordered by Madonsela.</p><br/>
                    <br/>
                    <center>
                        ~ o O o ~
                    </center>
                </div>
            </div>
        </div>
    </body>
</html>
"""
        
        doc = Document()
        doc.url = 'http://www.timeslive.co.za/politics/2014/04/01/iec-s-tlakula-must-resign-opposition-parties'
        self.crawler.extract(doc, html)

        self.assertEqual(doc.title, u"IEC's Tlakula must resign: opposition parties")
        self.assertEqual(doc.summary, u"Several opposition parties met in Pretoria on Tuesday to discuss Public Protector Thuli Madonsela's finding on the Nkandla upgrades and the controversy around IEC chairwoman Pansy Tlakula.")
        self.assertEqual(doc.published_at.strftime('%d %m %Y'), '01 04 2014')
        self.assertEqual(doc.author.name, "Sapa")
        self.assertEqual(doc.medium.name, 'Times')
        
        self.assertEqual(doc.text, u'Chairman of the multi-party forum Bantu Holomisa, who also heads the United Democratic Movement (UDM), said the opposition parties resolved to push for Tlakula\'s resignation.\n\n"All the political parties present, with the exception of the Democratic Alliance and the Freedom Front Plus, agreed that advocate Tlakula must resign immediately.\n\n"Should she refuse to resign, the parties who are in agreement will pursue legal action," said Holomisa.\n\nThe forum included the African Christian Democratic Party, AgangSA, Azapo, Economic Freedom Fighters, FF Plus, Inkatha Freedom Party, United Christian Democratic Party, and Holomisa\'s UDM.\n\nRegarding Nkandla, the parties resolved to convene another summit after President Jacob Zuma had reacted to Parliament as ordered by Madonsela.')
