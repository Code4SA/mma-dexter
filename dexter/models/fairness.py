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

from .support import db
from .with_offsets import WithOffsets

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


class Individual(db.Model):
    """
    Quick hack to support the legacy Group -> Org -> Individual construct
    from the old database. At some point this should be merged into the 
    entity/person tables.
    """
    __tablename__ = "individuals"

    id        = Column(Integer, primary_key=True)
    code      = Column(String(10), index=True, nullable=False, unique=True)
    name      = Column(String(100), index=True, nullable=False)

    def full_name(self):
        return self.code + ' - ' + self.name

    def __repr__(self):
        return "<Individual code='%s', name='%s'>" % (self.code, self.name)


    @classmethod
    def create_defaults(self):
        text = """
1                   |National Government
1.1                 |Presidency
1.1.1               |Jacob Zuma (President)
1.1.2               |Kgalema Motlanthe (Deputy President)
1.10                |Correctional Services
1.10.1              |Ms NN Mapisa-Nqakula (Min)
1.10.2              |Adv N Ramathlodi (Dep Min)
1.11                |Defence and Military Veterans
1.11.1              |Dr LN Sisulu (Min)
1.11.2              |Mr T Makwetla (Dep Min)
1.12                |Economic Development
1.12.1              |Mr E Patel (Min)
1.12.2              |Mr E Godongwana (Dep Min)
1.13                |Energy
1.13.1              |Ms ED Peters (Min)
1.13.2              |Ms B Thompson (Dep Min)
1.14                |Finance
1.14.1              |Mr PJ Gordhan (Min)
1.14.2              |Mr NM Nene (Dep Min)
1.15                |Health
1.15.1              |Dr PA Motsoaledi (Min)
1.15.2              |Dr G Ramokgopa (Dep Min)
1.16                |Higher Education and Training
1.16.1              |Dr BE Nzimande (Min)
1.16.2              |Ms HB Mkhize (Dep Min)
1.17                |Home Affairs
1.17.1              |Dr NC Dlamini Zuma (Min)
1.17.2              |Ms F Chohan (Dep Min)
1.18                |Human Settlements
1.18.1              |Mr TME Sexwale (Min)
1.18.2              |Ms ZA Kota-Fredericks (Dep Min)
1.19                |International Relations and Cooperation
1.19.1              |Ms MM Nkoana-Mashabane (Min)
1.19.2              |Mr M Fransman (Dep Min)
1.19.3              |Mr EI Ebrahim (Dep Min)
1.2                 |National Planning Commission
1.2.1               |Mr TA Manuel (Min)
1.20                |Justice and Constitutional Development
1.20.1              |Mr JT Radebe (Min)
1.20.2              |Mr AC Nel (Dep Min)
1.21                |Labour
1.21.1              |Ms M Oliphant (Min)
1.22                |Mineral Resources
1.22.1              |Ms S Shabangu (Min)
1.22.2              |Mr G Oliphant (Dep Min)
1.23                |Police
1.23.1              |Mr N Mthethwa (Min)
1.23.2              |Ms MM Sotyu (Dep Min)
1.24                |Public Enterprises
1.24.1              |Mr MKN Gigaba (Min)
1.24.2              |Mr B Martins (Dep Min)
1.25                |Public Service and Administration
1.25.1              |Mr R Baloyi (Min)
1.25.2              |Ms A Dlodlo (Dep Min)
1.26                |Public Works
1.26.1              |Ms G Mahlangu-Nkabinde (Min)
1.26.2              |Ms HI Bogopane-Zulu (Dep Min)
1.27                |Rural Development and Land Reform
1.27.1              |Mr G Nkwinti (Min)
1.27.2              |Mr TW Nxesi (Dep Min)
1.28                |Science and Technology
1.28.1              |Ms GNM Pandor (Min)
1.28.2              |Mr DA Hanekom (Dep Min)
1.29                |Social Development
1.29.1              |Ms BO Dlamini (Min)
1.29.2              |Ms BM Ntuli (Dep Min)
1.3                 |Performance Monitoring and Evaluation & Administration
1.3.1               |Mr OC Chabane (Min)
1.30                |Sport and Recreation
1.30.1              |Mr F Mbalula (Min)
1.30.2              |Mr GC Oosthuizen (Dep Min)
1.31                |State Security
1.31.1              |Mr SC Cwele (Min)
1.31.2              |Ms D Pule (Dep Min)
1.32                |Tourism
1.32.1              |Mr M van Schalkwyk (Min)
1.32.2              |Ms T Xasa (Dep Min)
1.33                |Trade and Industry
1.33.1              |Dr R Davies (Min)
1.33.2              |Ms TV Tobias-Pokolo (Dep Min)
1.33.3              |Ms E Thabethe (Dep Min)
1.34                |Transport
1.34.1              |Mr JS Ndebele (Min)
1.34.2              |Mr J Cronin (Dep Min)
1.35                |Water and Environmental  Affairs
1.35.1              |Ms BE Molewa (Min)
1.35.2              |Ms RT Mabhudafhasi  (Dep Min)
1.36                |Women, Children and People with Disabilities
1.36.1              |Ms L Xingwana (Min)
1.37                |Other Government Departments
1.37.1              |Minister
1.37.2              |Deputy Minister
1.4                 |Parliament
1.4.1               |Speaker
1.4.2               |Deputy Speaker
1.5                 |Agriculture, Forestry and Fisheries
1.5.1               |Ms T Joemat-Pettersson (Min)
1.5.2               |Dr PW Mulder (Dep Min)
1.6                 |Arts and Culture
1.6.1               |Mr P Mashatile (Min)
1.6.2               |Dr MJ Phaahla (Dep Min)
1.7                 |Basic Education
1.7.1               |Ms MA Motshekga (Min)
1.7.2               |Mr E Surty (Dep Min)
1.8                 |Communications
1.8.1               |Mr R Padayachie (Min)
1.8.2               |Mr O Bapela (Dep Min)
1.9                 |Cooperative Governance and Traditional Affairs
1.9.1               |Mr S Shiceka (Min)
1.9.2               |Mr Y Carrim (Dep Min)
10                  |Justice
10.1                |Judges
10.10               |Women's Legal Resource Centre
10.11               |Tswaranang Legal Advocacy Centre
10.12               |Legal Aid clinics
10.13               |Legal Aid Board
10.2                |Constitutional Court
10.3                |Lawyers, prosecutors, advocates
10.4                |Courts
10.5                |Children's Court
10.6                |South African Police Service (SAPS)
10.6.1              |National Police Commissioner
10.7                |Foreign Police Service/Interpol
10.8                |Rural Legal Centre
10.9                |Lawyers for Human Rights
11                  |Media
11.1                |Editor
11.2                |Journalist
11.3                |Critic
11.4                |DJ/Presenter
11.5                |SABC
11.6                |etv
11.7                |Public relations
12                  |Professionals
12.1                |Agriculture - forestry, farm workers, farmers
12.10               |Health - doctors, nurses, psychologist, lab technician
12.11               |Homemaker - either male or female
12.12               |Labourers - construction worker, truck driver, factory worker
12.13               |Military - army, corporals, generals, sergeants
12.14               |Mining
12.15               |Office and Service workers - secretary, personal assistant, waiters
12.16               |Prominent people/ celebrities
12.17               |Religion - priest, traditionalist, all faiths
12.18               |Royalty - kings, queens, princes
12.19               |Science & Technology - engineer, information technology, biologist
12.2                |Beauty contestant - includes model
12.20               |Sex workers
12.21               |Social Service - social workers
12.22               |Sports - sports bodies/officials, athlete, golfers, coaches, soccer players
12.23               |Student - scholar, pupil
12.24               |Other - where occupation cannot be categorised in terms of this list
12.3                |Community Associations
12.4                |Community Leader
12.5                |Criminal - convicted criminal, suspected criminal
12.6                |Education - teachers, principals
12.7                |Emergency services - ambulance, firefighters
12.8                |Entertainer - dancer, actor, singer, artist
12.9                |Entrepreneur - small and micro businessperson
13                  |Citizens
13.1                |Aunt
13.10               |Spouse - husband or wife
13.11               |Survivor
13.12               |Victim
13.13               |Uncle
13.14               |Witness
13.2                |Caregiver
13.3                |Child - son, daughter
13.4                |Family Member
13.5                |Father
13.6                |Friend
13.7                |Mother
13.8                |Neighbour/Resident
13.9                |Protestor
14                  |Corporations
14.1                |ABSA
14.10               |Telkom
14.11               |Pick 'n Pay
14.12               |Transnet
14.13               |Vodacom
14.14               |MTN
14.15               |Iscor
14.16               |SAA
14.17               |Ipsos Markinor
14.18               |TNS
14.19               |Other corporations
14.2                |Anglo American
14.3                |De Beers
14.4                |Eskom
14.5                |First National Bank
14.6                |Microsoft
14.7                |Nedbank
14.8                |Sasol
14.9                |Standard Bank
15                  |Other (Last Resort)
2                   |Provincial Government
2.1                 |Eastern Cape
2.1.1               |Ms N Kiviet (Premier)
2.1.2               |MECs
2.10                |National Council of Provinces (NCOP)
2.2                 |Freestate
2.2.1               |Mr A Magashule (Premier)
2.2.2               |MECs
2.3                 |Gauteng
2.3.1               |Ms N Mokonyane (Premier)
2.3.2               |MECs
2.4                 |KwaZuluNatal
2.4.1               |Mr Z Mkhize (Premier)
2.4.2               |MECs
2.5                 |Limpopo
2.5.1               |Mr C Mathale (Premier)
2.5.2               |MECs
2.6                 |Mpumalanga
2.6.1               |Mr D Mabuza (Premier)
2.6.2               |MECs
2.7                 |North West
2.7.1               |Ms T Modise (Premier)
2.7.2               |MECs
2.8                 |Northern Cape
2.8.1               |Ms H Jenkins (Premier)
2.8.2               |MECs
2.9                 |Western Cape
2.9.1               |Ms H Zille (Premier)
2.9.2               |MECs
3                   |Local Government
3.1                 |City of Johannesburg
3.1.1               |Mayor: Amos Masondo
3.1.2               |Municipal Manager
3.1.3               |Other City Official
3.1.4               |City Councillor
3.10                |Beaufort West
3.10.1              |Mayor
3.10.2              |Municipal Manager
3.10.3              |Other City Official
3.10.4              |City Councillor
3.100               |Frances Baard District Municipality
3.100.1             |Mayor
3.100.2             |Municipal Manager
3.100.3             |Other City Official
3.100.4             |City Councillor
3.101               |Joe Morolong Local Municipality
3.101.1             |Mayor
3.101.2             |Municipal Manager
3.101.3             |Other City Official
3.101.4             |City Councillor
3.102               |John Taolo Gaetsewe District Municipality
3.102.1             |Mayor
3.102.2             |Municipal Manager
3.102.3             |Other City Official
3.102.4             |City Councillor
3.103               |Namakwa District Municipality
3.103.1             |Mayor
3.103.2             |Municipal Manager
3.103.3             |Other City Official
3.103.4             |City Councillor
3.104               |Pixley Ka Seme District Municipality
3.104.1             |Mayor
3.104.2             |Municipal Manager
3.104.3             |Other City Official
3.104.4             |City Councillor
3.105               |Siyanda District Municipality
3.105.1             |Mayor
3.105.2             |Municipal Manager
3.105.3             |Other City Official
3.105.4             |City Councillor
3.106               |Dikgatlong
3.106.1             |Mayor
3.106.2             |Municipal Manager
3.106.3             |Other City Official
3.106.4             |City Councillor
3.107               |Siyathemba
3.107.1             |Mayor
3.107.2             |Municipal Manager
3.107.3             |Other City Official
3.107.4             |City Councillor
3.108               |Other Municipalities in Northern Cape
3.108.1             |Mayor
3.108.2             |Municipal Manager
3.108.3             |Other City Official
3.108.4             |City Councillor
3.11                |George
3.11.1              |Mayor
3.11.2              |Municipal Manager
3.11.3              |Other City Official
3.11.4              |City Councillor
3.12                |Mossel Bay
3.12.1              |Mayor
3.12.2              |Municipal Manager
3.12.3              |Other City Official
3.12.4              |City Councillor
3.13                |Stellenbosch
3.13.1              |Mayor
3.13.2              |Municipal Manager
3.13.3              |Other City Official
3.13.4              |City Councillor
3.14                |Drakenstein
3.14.1              |Mayor
3.14.2              |Municipal Manager
3.14.3              |Other City Official
3.14.4              |City Councillor
3.15                |Cape Agulhas
3.15.1              |Mayor
3.15.2              |Municipal Manager
3.15.3              |Other City Official
3.15.4              |City Councillor
3.16                |Knysna
3.16.1              |Mayor
3.16.2              |Municipal Manager
3.16.3              |Other City Official
3.16.4              |City Councillor
3.17                |Cape Wineland District Municipality
3.17.1              |Mayor
3.17.2              |Municipal Manager
3.17.3              |Other City Official
3.17.4              |City Councillor
3.18                |Central Karoo District Municipality
3.18.1              |Mayor
3.18.2              |Municipal Manager
3.18.3              |Other City Official
3.18.4              |City Councillor
3.19                |Eden District Municipality
3.19.1              |Mayor
3.19.2              |Municipal Manager
3.19.3              |Other City Official
3.19.4              |City Councillor
3.2                 |City of Tshwane
3.2.1               |Mayor
3.2.2               |Municipal Manager
3.2.3               |Other City Official
3.2.4               |City Councillor
3.20                |West Coast District Municipality
3.20.1              |Mayor
3.20.2              |Municipal Manager
3.20.3              |Other City Official
3.20.4              |City Councillor
3.21                |Other Municipalities in Western Cape
3.21.1              |Mayor
3.21.2              |Municipal Manager
3.21.3              |Other City Official
3.21.4              |City Councillor
3.22                |Ethekwini Metropolitan Municipality
3.22.1              |Mayor
3.22.2              |Municipal Manager
3.22.3              |Other City Official
3.22.4              |City Councillor
3.23                |Nongoma
3.23.1              |Mayor
3.23.2              |Municipal Manager
3.23.3              |Other City Official
3.23.4              |City Councillor
3.24                |The Msunduzi Metropolitan Municipality
3.24.1              |Mayor
3.24.2              |Municipal Manager
3.24.3              |Other City Official
3.24.4              |City Councillor
3.25                |Newcastle
3.25.1              |Mayor
3.25.2              |Municipal Manager
3.25.3              |Other City Official
3.25.4              |City Councillor
3.26                |Emnambithi/Ladysmith
3.26.1              |Mayor
3.26.2              |Municipal Manager
3.26.3              |Other City Official
3.26.4              |City Councillor
3.27                |Dannhauser
3.27.1              |Mayor
3.27.2              |Municipal Manager
3.27.3              |Other City Official
3.27.4              |City Councillor
3.28                |Ulundi
3.28.1              |Mayor
3.28.2              |Municipal Manager
3.28.3              |Other City Official
3.28.4              |City Councillor
3.29                |Maphumulo
3.29.1              |Mayor
3.29.2              |Municipal Manager
3.29.3              |Other City Official
3.29.4              |City Councillor
3.3                 |Ekurhuleni
3.3.1               |Mayor
3.3.2               |Municipal Manager
3.3.3               |Other City Official
3.3.4               |City Councillor
3.30                |Msinga
3.30.1              |Mayor
3.30.2              |Municipal Manager
3.30.3              |Other City Official
3.30.4              |City Councillor
3.31                |Umhlabuyalingana
3.31.1              |Mayor
3.31.2              |Municipal Manager
3.31.3              |Other City Official
3.31.4              |City Councillor
3.32                |uMngeni
3.32.1              |Mayor
3.32.2              |Municipal Manager
3.32.3              |Other City Official
3.32.4              |City Councillor
3.33                |Amajuba District Municipality
3.33.1              |Mayor
3.33.2              |Municipal Manager
3.33.3              |Other City Official
3.33.4              |City Councillor
3.34                |Ilembe District Municipality
3.34.1              |Mayor
3.34.2              |Municipal Manager
3.34.3              |Other City Official
3.34.4              |City Councillor
3.35                |Sisonke District Municipality
3.35.1              |Mayor
3.35.2              |Municipal Manager
3.35.3              |Other City Official
3.35.4              |City Councillor
3.36                |Ugu District Municipality
3.36.1              |Mayor
3.36.2              |Municipal Manager
3.36.3              |Other City Official
3.36.4              |City Councillor
3.37                |Umgungundlovu District Municipality
3.37.1              |Mayor
3.37.2              |Municipal Manager
3.37.3              |Other City Official
3.37.4              |City Councillor
3.38                |Umzinyathi District Municipality
3.38.1              |Mayor
3.38.2              |Municipal Manager
3.38.3              |Other City Official
3.38.4              |City Councillor
3.39                |Uthungulu District Municipality
3.39..3             |Other City Official
3.39.1              |Mayor
3.39.2              |Municipal Manager
3.39.4              |City Councillor
3.4                 |Metsweding District Municipality
3.4.1               |Mayor
3.4.2               |Municipal Manager
3.4.3               |Other City Official
3.4.4               |City Councillor
3.40                |Zululand District Municipality
3.40.1              |Mayor
3.40.2              |Municipal Manager
3.40.3              |Other City Official
3.40.4              |City Councillor
3.41                |Other Municipalities in Kwa Zulu Natal
3.41.1              |Mayor
3.41.2              |Municipal Manager
3.41.3              |Other City Official
3.41.4              |City Councillor
3.42                |Nelson Mandela Bay
3.42.1              |Mayor
3.42.2              |Municipal Manager
3.42.3              |Other City Official
3.42.4              |City Councillor
3.43                |Buffalo City
3.43.1              |Mayor
3.43.2              |Municipal Manager
3.43.3              |Other City Official
3.43.4              |City Councillor
3.44                |Matatiele
3.44.1              |Mayor
3.44.2              |Municipal Manager
3.44.3              |Other City Official
3.44.4              |City Councillor
3.45                |Alfred Nzo District Municipality
3.45.1              |Mayor
3.45.2              |Municipal Manager
3.45.3              |Other City Official
3.45.4              |City Councillor
3.46                |Amathole District Municipality
3.46.1              |Mayor
3.46.2              |Municipal Manager
3.46.3              |Other City Official
3.46.4              |City Councillor
3.47                |Cacadu District Municipality
3.47.1              |Mayor
3.47.2              |Municipal Manager
3.47.3              |Other City Official
3.47.4              |City Councillor
3.48                |Chris Hani District Municipality
3.48.1              |Mayor
3.48.2              |Municipal Manager
3.48.3              |Other City Official
3.48.4              |City Councillor
3.49                |OR Tambo District Municipality
3.49.1              |Mayor
3.49.2              |Municipal Manager
3.49.3              |Other City Official
3.49.4              |City Councillor
3.5                 |Sedibeng District Municipality
3.5.1               |Mayor
3.5.2               |Municipal Manager
3.5.3               |Other City Official
3.5.4               |City Councillor
3.50                |Ukhahlamba District Municipality
3.50.1              |Mayor
3.50.2              |Municipal Manager
3.50.3              |Other City Official
3.50.4              |City Councillor
3.51                |Other Municipalities in Eastern Cape
3.51.1              |Mayor
3.51.2              |Municipal Manager
3.51.3              |Other City Official
3.51.4              |City Councillor
3.52                |Polokwane
3.52.1              |Mayor
3.52.2              |Municipal Manager
3.52.3              |Other City Official
3.52.4              |City Councillor
3.53                |Makhado
3.53.1              |Mayor
3.53.2              |Municipal Manager
3.53.3              |Other City Official
3.53.4              |City Councillor
3.54                |Musina
3.54.1              |Mayor
3.54.2              |Municipal Manager
3.54.3              |Other City Official
3.54.4              |City Councillor
3.55                |Greater Giyani
3.55.1              |Mayor
3.55.2              |Municipal Manager
3.55.3              |Other City Official
3.55.4              |City Councillor
3.56                |Greater Letaba
3.56.1              |Mayor
3.56.2              |Municipal Manager
3.56.3              |Other City Official
3.56.4              |City Councillor
3.57                |Greater Tzaneen
3.57.1              |Mayor
3.57.2              |Municipal Manager
3.57.3              |Other City Official
3.57.4              |City Councillor
3.58                |Ba-Phalaborwa
3.58.1              |Mayor
3.58.2              |Municipal Manager
3.58.3              |Other City Official
3.58.4              |City Councillor
3.59                |Bela-Bela
3.59.1              |Mayor
3.59.2              |Municipal Manager
3.59.3              |Other City Official
3.59.4              |City Councillor
3.6                 |West Rand District Municipality
3.6.1               |Mayor
3.6.2               |Municipal Manager
3.6.3               |Other City Official
3.6.4               |City Councillor
3.60                |Greater Marble Hall
3.60.1              |Mayor
3.60.2              |Municipal Manager
3.60.3              |Other City Official
3.60.4              |City Councillor
3.61                |Greater Tubatse
3.61.1              |Mayor
3.61.2              |Municipal Manager
3.61.3              |Other City Official
3.61.4              |City Councillor
3.62                |Capricorn District Municipality
3.62.1              |Mayor
3.62.2              |Municipal Manager
3.62.3              |Other City Official
3.62.4              |City Councillor
3.63                |Greater Sekhukhune District Municipality
3.63.1              |Mayor
3.63.2              |Municipal Manager
3.63.3              |Other City Official
3.63.4              |City Councillor
3.64                |Mopani District Municipality
3.64.1              |Mayor
3.64.2              |Municipal Manager
3.64.3              |Other City Official
3.64.4              |City Councillor
3.65                |Vhembe District Municipality
3.65.1              |Mayor
3.65.2              |Municipal Manager
3.65.3              |Other City Official
3.65.4              |City Councillor
3.66                |Waterberg District Municipality
3.66.1              |Mayor
3.66.2              |Municipal Manager
3.66.3              |Other City Official
3.66.4              |City Councillor
3.67                |Mutale
3.67.1              |Mayor
3.67.2              |Municipal Manager
3.67.3              |Other City Official
3.67.4              |City Councillor
3.68                |Other Municipalities in Limpopo
3.68.1              |Mayor
3.68.2              |Municipal Manager
3.68.3              |Other City Official
3.68.4              |City Councillor
3.69                |Mangaung
3.69.1              |Mayor
3.69.2              |Municipal Manager
3.69.3              |Other City Official
3.69.4              |City Councillor
3.7                 |Merafong
3.7.1               |Mayor
3.7.2               |Municipal Manager
3.7.3               |Other City Official
3.7.4               |City Councillor
3.70                |Maluti a Phofung
3.70.1              |Mayor
3.70.2              |Municipal Manager
3.70.3              |Other City Official
3.70.4              |City Councillor
3.71                |Fezile Dabi District Municipality
3.71.1              |Mayor
3.71.2              |Municipal Manager
3.71.3              |Other City Official
3.71.4              |City Councillor
3.72                |Lejweleputswa District Municipality
3.72.1              |Mayor
3.72.2              |Municipal Manager
3.72.3              |Other City Official
3.72.4              |City Councillor
3.73                |Motheo District Municipality
3.73.1              |Mayor
3.73.2              |Municipal Manager
3.73.3              |Other City Official
3.73.4              |City Councillor
3.74                |Thabo Mofutsanyana District Municipality
3.74.1              |Mayor
3.74.2              |Municipal Manager
3.74.3              |Other City Official
3.74.4              |City Councillor
3.75                |Xhariep District Municipality
3.75.1              |Mayor
3.75.2              |Municipal Manager
3.75.3              |Other City Official
3.75.4              |City Councillor
3.76                |Naledi
3.76.1              |Mayor
3.76.2              |Municipal Manager
3.76.3              |Other City Official
3.76.4              |City Councillor
3.77                |Other Municipalities in Free State
3.77.1              |Mayor
3.77.2              |Municipal Manager
3.77.3              |Other City Official
3.77.4              |City Councillor
3.78                |Bushbuckridge
3.78.1              |Mayor
3.78.2              |Municipal Manager
3.78.3              |Other City Official
3.78.4              |City Councillor
3.79                |Mbombela
3.79.1              |Mayor
3.79.2              |Municipal Manager
3.79.3              |Other City Official
3.79.4              |City Councillor
3.8                 |Other Municipalities in Gauteng
3.8.1               |Mayor
3.8.2               |Municipal Manager
3.8.3               |Other City Official
3.8.4               |City Councillor
3.80                |Albert Luthuli
3.80.1              |Mayor
3.80.2              |Municipal Manager
3.80.3              |Other City Official
3.80.4              |City Councillor
3.81                |Ehlanzeni District Municipality
3.81.1              |Mayor
3.81.2              |Municipal Manager
3.81.3              |Other City Official
3.81.4              |City Councillor
3.82                |Gert Sibande District Municipality
3.82.1              |Mayor
3.82.2              |Municipal Manager
3.82.3              |Other City Official
3.82.4              |City Councillor
3.83                |Nkangala District Municipality
3.83.1              |Mayor
3.83.2              |Municipal Manager
3.83.3              |Other City Official
3.83.4              |City Councillor
3.84                |Delmas
3.84.1              |Mayor
3.84.2              |Municipal Manager
3.84.3              |Other City Official
3.84.4              |City Councillor
3.85                |Other Municipalities in Mpumalanga
3.85.1              |Mayor
3.85.2              |Municipal Manager
3.85.3              |Other City Official
3.85.4              |City Councillor
3.86                |Rustenburg
3.86.1              |Mayor
3.86.2              |Municipal Manager
3.86.3              |Other City Official
3.86.4              |City Councillor
3.87                |Mafikeng
3.87.1              |Mayor
3.87.2              |Municipal Manager
3.87.3              |Other City Official
3.87.4              |City Councillor
3.88                |Greater Taung
3.88.1              |Mayor
3.88.2              |Municipal Manager
3.88.3              |Other City Official
3.88.4              |City Councillor
3.89                |Madibeng
3.89.1              |Mayor
3.89.2              |Municipal Manager
3.89.3              |Other City Official
3.89.4              |City Councillor
3.9                 |City of Cape Town
3.9.1               |Mayor: Dan Plato
3.9.2               |Municipal Manager
3.9.3               |Other City Official
3.9.4               |City Councillor
3.90                |Naledi
3.90.1              |Mayor
3.90.2              |Municipal Manager
3.90.3              |Other City Official
3.90.4              |City Councillor
3.91                |Ventersdorp
3.91.1              |Mayor
3.91.2              |Municipal Manager
3.91.3              |Other City Official
3.91.4              |City Councillor
3.92                |City of Matlosana
3.92.1              |Mayor
3.92.2              |Municipal Manager
3.92.3              |Other City Official
3.92.4              |City Councillor
3.93                |Bojanala Platinum District Municipality
3.93.1              |Mayor
3.93.2              |Municipal Manager
3.93.3              |Other City Official
3.93.4              |City Councillor
3.94                |Bophirima District Municipality
3.94.1              |Mayor
3.94.2              |Municipal Manager
3.94.3              |Other City Official
3.94.4              |City Councillor
3.95                |Dr Kenneth Kaunda District Municipality
3.95.1              |Mayor
3.95.2              |Municipal Manager
3.95.3              |Other City Official
3.95.4              |City Councillor
3.96                |Ngaka Modiri Molema District Municipality
3.96.1              |Mayor
3.96.2              |Municipal Manager
3.96.3              |Other City Official
3.96.4              |City Councillor
3.97                |Other Municipalities in North West
3.97.1              |Mayor
3.97.2              |Municipal Manager
3.97.3              |Other City Official
3.97.4              |City Councillor
3.98                |Sol Plaatjie
3.98.1              |Mayor
3.98.2              |Municipal Manager
3.98.3              |Other City Official
3.98.4              |City Councillor
3.99                |Kgatelopele
3.99.1              |Mayor
3.99.2              |Municipal Manager
3.99.3              |Other City Official
3.99.4              |City Councillor
4                   |Political Parties
4.1                 |African Christian Democratic Party - ACDP
4.1.1               |Rev. Dr. Kenneth Rasalabe Joseph Meshoe
4.1.2               |Ms Jo-Ann Downs
4.1.3               |Chairperson
4.1.4               |Secretary General
4.10                |Labour Party Of South Africa - L.P
4.10.1              |President
4.11                |Minority Front - MF
4.11.1              |President
4.12                |National Alliance - N A
4.12.1              |President
4.13                |National Democratic Convention
4.13.1              |President
4.14                |National Freedom Party
4.14.1              |Zanele Magwaza-Msibi
4.15                |Pan Africanist Congress Of Azania - PAC
4.15.1              |Letlapa Mphahlele
4.15.2              |Mfanelo Skwatsha
4.15.3              |Shadrack Pooe
4.16                |Peace And Development Party - PDP
4.16.1              |President
4.17                |Peace And Justice Congress - PJC
4.17.1              |President
4.18                |Royal Loyal Progress - RLP
4.18.1              |President
4.19                |Sindawonye Progressive Party - SPP
4.19.1              |President
4.2                 |African National Congress - ANC
4.2.1               |Jacob Zuma
4.2.10              |Julius Malema
4.2.11              |ANC Womens League (ANCWL)
4.2.12              |Nosiviwe Mapisa-Nqakula
4.2.2               |Kgalema Motlanthe
4.2.3               |Baleka Mbete
4.2.4               |Gwede Mantashe
4.2.5               |Thandi Modise
4.2.6               |Matthew Phosa
4.2.7               |Nelson Mandela
4.2.8               |Thabo Mbeki
4.2.9               |ANC Youth League (ANCYL)
4.20                |South African Communist Party - SACP
4.20.1              |Blade Nzimande (Sec Gen)
4.20.2              |Jeremy Cronin (Dep Sec Gen)
4.20.3              |Gwede Mantashe (Chairperson)
4.20.4              |Young Communist League
4.20.5              |Buti Manamela
4.21                |United Christian Democratic Party - UCDP
4.21.1              |Kgosi Mangope
4.21.2              |PHK Ditsetelo
4.21.3              |IS Mfundisi
4.21.4              |MN Matladi
4.22                |United Democratic Movement - UDM
4.22.1              |Bantu Holomisa
4.22.2              |Ntopile Kganyago
4.22.3              |Bongani Msomi
4.22.4              |Humphrey Nobongoza
4.23                |Vryheidsfront Plus/Freedom Front Plus - VF+ /FF Plus
4.23.1              |President
4.23.2              |Deputy President
4.23.3              |Chairperson
4.23.4              |Secretary General
4.24                |Other Parties
4.24.1              |President
4.24.2              |Deputy President
4.24.3              |Chairperson
4.24.4              |Secretary General
4.3                 |Azanian People's Organisation - Azapo
4.3.1               |Dr. Mosibudi Mangena
4.3.2               |Pandelani Nefolovhodwe
4.3.3               |Cindi , Zithulele Nyangana Absalom
4.3.4               |Strike Thokoane
4.4                 |Christian Democratic Party - CDP
4.4.1               |President
4.5                 |Congress Of The People - Cope
4.5.1               |Mosiuoa Lekota
4.5.2               |Mbazima Shilowa
4.5.3               |Chairperson
4.5.4               |Secretary General
4.5.6               |Cope Youth Movement
4.5.7               |Anele Mda
4.5.8               |Lekota Faction
4.5.9               |Shilowa Faction
4.6                 |Democratic Alliance/Demokratiese Alliansie - DA
4.6.1               |Helen Zille
4.6.10              |Patricia De Lille
4.6.11              |Lindiwe Mazibuko
4.6.2               |Dr Wilmont James
4.6.3               |Athol Trollip
4.6.4               |Ian Davison
4.6.5               |Dion George
4.6.6               |Natasha Michael
4.6.7               |Anchen Dreyer
4.6.8               |Dianne Kohler Barnard
4.6.9               |Ivan Meyer
4.7                 |Dikwankwetla Party Of South Africa - DPSA
4.7.1               |President
4.8                 |Inkatha Freedom Party - IFP
4.8.1               |Mongosuthu Buthelezi (President)
4.8.2               |Musa Zondi (Sec Gen)
4.8.3               |IFP Youth Brigade
4.8.4               |President (Youth Brigade)
4.8.5               |IFP Youth Brigade
4.8.6               |Pat Lebenya-Ntanzi
4.9                 |Keep It Straight And Simple - Kiss
4.9.1               |President
5                   |International Groups & Donors
5.1                 |Foreign Government
5.10                |OSEAN
5.11                |SADC
5.12                |ECOWAS
5.13                |Arab League
5.14                |IGAD
5.15                |NEPAD
5.16                |International election observers
5.2                 |International Body (other than UN and AU)
5.3                 |International Political Figure
5.4                 |Open Society Foundation
5.5                 |UN
5.6                 |World Bank
5.7                 |IMF
5.8                 |European Union
5.9                 |African Union
6                   |Commisions  & Independent Bodies
6.1                 |Commision on Gender Equality (CGE)
6.1.1               |Mfanozelwe Shozi: Deputy Chairperson (Acting Chairperson)
6.1.2               |Other commissioners
6.2                 |Human Rights Commission
6.2.1               |Adv Mabedle Lawrence Mushwana (Chairperson)
6.2.2               |Dr Pregaluxmi Govender (Deputy Chairperson)
6.2.3               |Adv Bokankatla Joseph Malatji (Commissioner)
6.2.4               |Ms Lindiwe Faith Mokete (Commissioner)
6.2.5               |Ms Janet Love (Commissioner)
6.2.6               |Dr Danfred James (Commissioner)
6.2.7               |Dr Gladstone Sandi Baai (Commissioner)
6.3                 |ICASA
6.3.1               |Paris Mashile (Chaiperson)
6.3.2               |Councillor
6.4                 |IEC (Independent Electoral Commission)
6.4.1               |Dr Brigalia Bam (Chairperson)
6.4.2               |Ms Thoko Mpumlwana (Deputy Chairperson)
6.4.3               |Mr Fanie van der Merwe
6.4.4               |Judge Herbert Qedusizi Msimang
6.4.5               |Mr Terry Tselane
6.4.6               |Pansy Tlakula (Chief Electoral Officer)
7                   |Academics / Experts
7.1                 |Centre for Policy Studies
7.10                |University of Stellenbosch
7.11                |University of the Free State
7.12                |University of the Witwatersrand
7.13                |University of Western Cape
7.14                |Other Universities
7.2                 |Human Sciences Research Council
7.3                 |Other Research Centres/institutes
7.4                 |University of Johannesburg
7.5                 |Rhodes University
7.6                 |UNISA
7.7                 |University of Cape Town
7.8                 |University of KwaZulu-Natal
7.9                 |University of Pretoria
8                   |NGOs / CBOs / FBOs
8.1                 |Media Monitoring Africa
8.1.1               |William Bird (Director)
8.10                |Southern African Media and Gender Institute (SAMGI)
8.11                |The Triangle Project
8.12                |GALA
8.13                |Gay and Lesbian Project
8.14                |IDASA
8.15                |ChildLine
8.16                |Teddy Bear Clinic
8.17                |Oxfam
8.18                |Amnesty International
8.19                |Human Rights Watch
8.2                 |People Opposing Women Abuse (POWA)
8.20                |Gender Links
8.21                |Treatment Action Campaign (TAC)
8.3                 |Centre for the Study of Violence and Reconciliation (CSVR)
8.4                 |Women's Net
8.5                 |Men's Forum
8.5.1               | Mbuyiselo Botha
8.6                 |Men as Partners (MAP)
8.7                 |Media Institute of Southern Africa (MISA)
8.8                 |NISAA
8.9                 |Gender Advocacy Programme (GAP)
9                   |Unions
9.1                 |COSATU
9.1.1               |Sdumo Dlamini (President)
9.1.2               |Zwelenzima Vavi (Sec Gen)
9.10                |SADTU
9.2                 |FEDUSA
9.3                 |NUMSA
9.4                 |SOLIDARITY
9.5                 |NEHAWU
9.6                 |NACTU
9.7                 |NAPTOSA
9.8                 |National Union of Educators
9.9                 |Professional Educators' Union
        """

        individuals = []
        for s in text.strip().split("\n"):
            code, name = s.split("|")
            i = Individual()
            i.code = code.strip()
            i.name = name.strip()
            individuals.append(i)

        return individuals
