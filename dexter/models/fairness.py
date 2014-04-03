from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Boolean,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

from wtforms import StringField, TextAreaField, validators, DateTimeField, HiddenField
from wtforms.fields.html5 import URLField

from ..forms import Form, SelectField
from .support import db

class Fairness(db.Model):
    """
    A measure of how fair a source is.
    """
    __tablename__ = "fairness"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Fairness name='%s'>" % (self.name)


    @classmethod
    def create_defaults(self):
        text = """
        Language - exaggeration
        Language - trivialisation
        Language - generalisation
        Presentation
        Omission
        Fair
        Unclear
        """

        fairness = []
        for s in text.strip().split("\n"):
            f = Fairness()
            f.name = s.strip()
            fairness.append(f)

        return fairness

class DocumentFairness(db.Model):
    """
    Fairness/bias description for an article.
    """
    __tablename__ = "document_fairness"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True, nullable=False)

    # Is the article biased for or against anyone? Note that, for now, biased is
    # for or against a fixed list of organisations/affiliations. In time, that list
    # will have to be changed and merged into the entity table.
    fairness_id  = Column(Integer, ForeignKey('fairness.id'), index=True, default=6, nullable=False)
    # who is the source biased in favour of?
    bias_favour_affiliation_id = Column(Integer, ForeignKey('affiliations.id'), index=True, nullable=True)
    # who is the source biased against?
    bias_oppose_affiliation_id = Column(Integer, ForeignKey('affiliations.id'), index=True, nullable=True)
    
    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    fairness    = relationship("Fairness", lazy=False)
    bias_favour = relationship("Affiliation", lazy=False, foreign_keys=[bias_favour_affiliation_id])
    bias_oppose = relationship("Affiliation", lazy=False, foreign_keys=[bias_oppose_affiliation_id])

    def __repr__(self):
        return "<DocumentFairness id=%s, doc=%s, fairness=%s>" % (self.id, self.document, self.fairness)


class DocumentFairnessForm(Form):
    fairness_id                  = SelectField('Bias', default='')
    bias_favour_affiliation_id   = SelectField('Favour', default='')
    bias_oppose_affiliation_id   = SelectField('Disfavour', default='')

    def __init__(self, *args, **kwargs):
        super(DocumentFairnessForm, self).__init__(*args, **kwargs)

        self.fairness_id.choices = [[str(s.id), s.name] for s in Fairness.query.order_by(Fairness.name).all()]

        # sort according to code
        affiliations = sorted(Affiliation.query.all(), key=Affiliation.sort_key)
  
        self.bias_favour_affiliation_id.choices = [['', '(none)']] + [[str(s.id), s.full_name()] for s in affiliations]
        self.bias_oppose_affiliation_id.choices = self.bias_favour_affiliation_id.choices


    def create_or_update(self, document):
        if self.is_new():
            return self.create_fairness(document)
        else:
            self.populate_obj(self.document_fairness)
            return None

    def create_fairness(self, document):
        f = DocumentFairness()
        f.document = document
        self.populate_obj(f)

        return f


    def is_new(self):
        return self._prefix.startswith('fairness-new')


class Affiliation(db.Model):
    """
    Quick hack to support the legacy Group -> Org -> Affiliation construct
    from the old database. At some point this should be merged into the 
    entity/person tables.
    """
    __tablename__ = "affiliations"

    id        = Column(Integer, primary_key=True)
    code      = Column(String(10), index=True, nullable=False, unique=True)
    name      = Column(String(100), index=True, nullable=False)

    def full_name(self):
        return self.code + ' - ' + self.name

    def sort_key(self):
        return [int(k) if k else 0 for k in self.code.split('.')]

    def __repr__(self):
        return "<Affiliation code='%s', name='%s'>" % (self.code, self.name)


    @classmethod
    def create_defaults(self):
        text = """
1 National Government
1.1 Presidency
1.2 National Planning Commission
1.3 Department of Performance Monitoring and Evaluation & Administration
1.4 Parliament
1.5 Department of Agriculture, Forestry and Fisheries 
1.6 Department of Arts and Culture 
1.7 Department of Basic Education 
1.8 Department of Communications 
1.9 Department of Cooperative Governance and Traditional Affairs 
1.10  Department of Correctional Services 
1.11  Department of Defence and Military Veterans 
1.12  Department of Economic Development 
1.13  Department of Energy 
1.14  Department of Finance 
1.15  Department of Health
1.16  Department of Higher Education and Training 
1.17  Department of Home Affairs 
1.18  Department of Human Settlements 
1.19  Department of International Relations and Cooperation 
1.20  Department of Justice and Constitutional Development 
1.21  Department of Labour 
1.22  Department of Mineral Resources 
1.23  Department of Police 
1.24  Department of Public Enterprises 
1.25  Department of Public Service and Administration 
1.26  Department of Public Works 
1.27  Department of Rural Development and Land Reform 
1.28  Department of Science and Technology 
1.29  Department of Social Development 
1.30  Department of Sport and Recreation 
1.31  Department of State Security 
1.32  Department of Tourism 
1.33  Department of Trade and Industry 
1.34  Department of Transport  
1.35  Department of Water and Environmental  Affairs 
1.36  Department of Women, Children and People with Disabilities 
1.37  Other government department
2 Provincial Government
2.1 Eastern Cape Provincial Government
2.2 Freestate Provincial Government
2.3 Gauteng Provincial Government
2.4 KwaZulu-Natal Provincial Government
2.5 Limpopo Provincial Government
2.6 Mpumalanga Provincial Government
2.7 North West Provincial Government
2.8 Northern Cape Provincial Government
2.9 Western Cape Provincial Government
2.10  National Council of Provinces - NCOP
3 Local Government
3.1 Nelson Mandela Bay 
3.2 Buffalo City Metropolitan Municipality
3.3 Alfred Nzo District Municipality
3.4 Amathole District Municipality
3.5 Cacadu District Municipality
3.6 Chris Hani District Municipality
3.7 OR Tambo District Municipality
3.8 Ukhahlamba District Municipality
3.9 Other municipality in Eastern Cape
3.10  Mangaung Metropolitan Municipality
3.11  Fezile Dabi District Municipality
3.12  Lejweleputswa District Municipality
3.13  Motheo District Municipality
3.14  Thabo Mofutsanyana District Municipality
3.15  Xhariep District Municipality
3.16  Other municipality in Free State
3.17  City of Johannesburg 
3.18  City of Tshwane 
3.19  Ekurhuleni Municipality
3.20  Metsweding District Municipality
3.21  Sedibeng District Municipality
3.22  West Rand District Municipality
3.23  Other municipality in Gauteng
3.24  Ethekwini Metropolitan Municipality 
3.25  Amajuba District Municipality
3.26  Harry Gwala District
3.27  Ilembe District Municipality
3.28  Ugu District Municipality
3.29  Umgungundlovu District Municipality
3.30  Umzinyathi District Municipality
3.31  Uthungulu District Municipality
3.32  Umkhayakude District
3.33  Uthukela District
3.34  Zululand District Municipality
3.35  Other municipality in KwaZulu-Natal
3.36  Capricorn District Municipality
3.37  Greater Sekhukhune District Municipality
3.38  Mopani District Municipality
3.39  Vhembe District Municipality
3.40  Waterberg District Municipality
3.41  Other municipality in Limpopo
3.42  Ehlanzeni District Municipality
3.43  Gert Sibande District Municipality
3.44  Nkangala District Municipality
3.45  Other municipality in Mpumalanga
3.46  Bojanala Platinum District Municipality
3.47  Dr Ruth Segomotsi Mompati District Municipality
3.48  Dr Kenneth Kaunda District Municipality
3.49  Ngaka Modiri Molema District Municipality
3.50  Other municipality in North West
3.51  Frances Baard District Municipality
3.52  John Taolo Gaetsewe District Municipality
3.53  Namakwa District Municipality
3.54  Pixley Ka Seme District Municipality
3.55  Other municipality in Northern Cape
3.56  City of Cape Town Metropolitican Municipality
3.57  Cape Wineland District Municipality
3.58  Central Karoo District Municipality
3.59  Eden District Municipality
3.60  Overberg District Municipality
3.61  West Coast District Municipality
3.62  Other municipality in Western Cape
4 Political Parties
4.1 African Christian Democratic Party - ACDP 
4.2 A Party
4.3 African National Congress - ANC 
4.4 Agang SA
4.5 Azanian People's Organisation - Azapo  
4.6 Christian Democratic Party - CDP  
4.7 Congress of the People(Cope  
4.8 Democratic Alliance/Demokratiese Alliansie - DA  
4.9 Dikwankwetla Party Of South Africa - DPSA  
4.10  Economic Freedom Fighters - EFF
4.11  Inkatha Freedom Party - IFP  
4.12  Keep It Straight And Simple - Kiss  
4.13  Labour Party Of South Africa - LP  
4.14  Minority Front - MF 
4.15  National Alliance - NA  
4.16  National Democratic Convention - NADECO
4.17  National Freedom Party - NFP
4.18  Pan Africanist Congress of Azania - PAC  
4.19  Pan Africanist Movement - PAM
4.20  Peace And Justice Congress - PJC
4.21  Royal Loyal Progress - RLP
4.22  Sindawonye Progressive Party - SPP
4.23  South African Communist Party - SACP
4.24  United Christian Democratic Party - UCDP
4.25  United Democratic Movement - UDM  
4.26  Vryheidsfront Plus/Freedom Front Plus - VF+ /FF Plus  
4.27  Other political party not listed
5 International Groups / Donors
5.1 Foreign Government
5.2 International Body - other than UN and AU
5.3 International Political Figure
5.4 Open Society Foundation
5.5 United Nations - UN
5.6 World Bank
5.7 Internation Monetary Funds - IMF
5.8 European Union - EU
5.9 African Union - AU
5.10  Osteopathic European Academic Network - OSEAN
5.11  Southern African Development Community - SADC
5.12  Economic Community Of West African States - ECOWAS
5.13  Arab League
5.14  Intergovernmental Authority on Development - IGAD
5.15  New Partnership for Africa's Development - NEPAD
5.16  World Health Organisation - WHO
5.17  International election observer
5.18  Other international group / donor not listed
6 Commisions  & Independent Bodies
6.1 Independent Electoral Commission - IEC
6.2 Human Rights Commission - HRC
6.3 Independent Communications Authourity of South Africa - ICASA
6.4 Commision on Gender Equality - CGE
6.5 Broadcasting Complaints Commission of South Africa - BCCSA
6.6 Press Council of South Africa
6.7 Marikana Commission of Inquiry - Farlam Commission
6.8 Arms Deal Commission of Inquiry - Sereti Commission
6.9 Other commission / independent body not listed
7 Academics / Experts / Researchers 
7.1 Centre for Policy Studies
7.2 Human Sciences Research Council
7.3 University of Johannesburg
7.4 Rhodes University
7.5 University of South Africa - UNISA
7.6 University of Cape Town
7.7 University of KwaZulu-Natal
7.8 University of Pretoria
7.9 University of Stellenbosch
7.10  University of the Free State
7.11  University of the Witwatersrand
7.12  University of Western Cape
7.13  Other university / research centre / institute not listed
8 NGOs / CBOs / FBOs
8.1 Media Monitoring Africa
8.2 People Opposing Women Abuse - POWA
8.3 Centre for the Study of Violence and Reconciliation - CSVR
8.4 Women's Net
8.5 Men's Forum
8.6 Men as Partners - MAP
8.7 Media Institute of Southern Africa - MISA
8.8 Institute for Women's Development - NISAA
8.9 Gender Advocacy Programme - GAP
8.10  Southern African Media and Gender Institute - SAMGI
8.11  The Triangle Project
8.12  Gay and Lesbian Memory in Action - GALA
8.13  Gay and Lesbian Project
8.14  Childline
8.15  Teddy Bear Clinic
8.16  Oxfam
8.17  Amnesty International
8.18  Human Rights Watch
8.19  Gender Links
8.20  Treatment Action Campaign - TAC
9 Unions
9.1 COSATU
9.2 FEDUSA
9.3 NUMSA
9.4 SOLIDARITY
9.5 NEHAWU
9.6 NACTU
9.7 NAPTOSA
9.8 National Union of Educators
9.9 Professional Educators' Union
9.10  SADTU
9.11  Other union not listed
10  Justice System
10.1  Judge
10.2  Constitutional Court
10.3  Lawyer / Prosecutor / Advocate
10.4  Court
10.5  Children's Court
10.6  South African Police Service - SAPS
10.7  Foreign Police Service / Interpol
10.8  Rural Legal Centre
10.9  Lawyers for Human Rights
10.10 Women's Legal Resource Centre
10.11 Tswaranang Legal Advocacy Centre
10.12 Legal Aid Clinic
10.13 Legal Aid Board
10.14 Other justice system organisation not listed
11  Professionals
11.1  Agriculture - forestry, farm workers, farmers
11.2  Beauty contestant - includes model
11.3  Community Association
11.4  Community Leader
11.5  Criminal - convicted criminal, suspected criminal
11.6  Education - teacher, principal
11.7  Emergency services - ambulance, firefighter
11.8  Entertainer - dancer, actor, singer, artist
11.9  Entrepreneur - small and micro businessperson
11.10 Health - doctor, nurse, psychologist, lab technician
11.11 Homemaker - either male or female
11.12 Labourers - construction worker, truck driver, factory worker
11.13 Media - editor, jourmalist, dj, presenter, critic, public relations
11.14 Military - corporal, general, sergeant
11.15 Mining - miner, rock driller
11.16 Office and Service workers - secretary, personal assistant, waiters
11.17 Prominent people/ celebrities
11.18 Religion - priest, traditionalist, all faiths
11.19 Royalty - king, queen, prince
11.20 Science & Technology - engineer, information technology, biologist
11.21 Sex worker
11.22 Social Service - social worker
11.23 Sports - sports bodies/officials, athlete, golfers, coaches, soccer players
11.24 Student - scholar, pupil
11.25 Other occupation not listed
12  Citizens
12.1  Aunt
12.2  Caregiver
12.3  Child - son, daughter
12.4  Family Member
12.5  Father
12.6  Friend
12.7  Mother
12.8  Neighbour/Resident
12.9  Protestor
12.10 Spouse - husband or wife
12.11 Survivor
12.12 Victim
12.13 Uncle
12.14 Witness
12.15 Other citizen not listed
13  Corporations
13.1  ABSA
13.2  Anglo American
13.3  De Beers
13.4  Eskom
13.5  First National Bank
13.6  Microsoft
13.7  Nedbank
13.8  Sasol
13.9  Standard Bank
13.10 Telkom
13.11 Pick 'n Pay
13.12 Transnet
13.13 Vodacom
13.14 MTN
13.15 Iscor
13.16 SAA
13.17 Ipsos Markinor
13.18 TNS
13.19 Other corporation not listed
        """

        affiliations = []
        for s in text.strip().split("\n"):
            code, name = s.split(" ", 1)
            i = Affiliation()
            i.code = code.strip()
            i.name = name.strip()
            affiliations.append(i)

        return affiliations
