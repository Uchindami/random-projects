import csv
import json

# Sample JSON data
data = [
    {
        "position": "risk analyst",
        "companyName": "nico life insurance company limited",
        "category": "Finance & Economics",
        "sub-category": "Insurance"
    },
    {
        "position": "monitoring and evaluation me assistant",
        "companyName": "kamuzu university of health sciences kuhes",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "industrial development specialist",
        "companyName": "export development fund edf",
        "category": "Business & Management",
        "sub-category": "Consultancy"
    },
    {
        "position": "internal audit officer",
        "companyName": "export development fund edf",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "credit underwriter",
        "companyName": "first capital bank",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    },
    {
        "position": "it projects lead",
        "companyName": "sparc systems limited",
        "category": "Technology & Engineering",
        "sub-category": "Software Development"
    },
    {
        "position": "chief executive officer",
        "companyName": "malawi accountants board",
        "category": "Business & Management",
        "sub-category": "Consultancy"
    },
    {
        "position": "principal environmental health officer",
        "companyName": "nkhotakota district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "senior medical officer",
        "companyName": "nkhotakota district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "sanitation officer",
        "companyName": "nkhotakota district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "business training officer",
        "companyName": "smedi",
        "category": "Education & Research",
        "sub-category": "Vocational Training"
    },
    {
        "position": "business information and advisory services officer",
        "companyName": "smedi",
        "category": "Business & Management",
        "sub-category": "Consultancy"
    },
    {
        "position": "assistant accountant 2 positions",
        "companyName": "smedi",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "driver",
        "companyName": "smedi",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "production assistant non-established",
        "companyName": "smedi",
        "category": "Creative & Communication",
        "sub-category": "Media Production"
    },
    {
        "position": "office assistant",
        "companyName": "smedi",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "communications and advocacy officer",
        "companyName": "resident coordinator system",
        "category": "Creative & Communication",
        "sub-category": "Public Relations"
    },
    {
        "position": "chef",
        "companyName": "chatonda lodge",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "tours consultant",
        "companyName": "the travel centre",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "drivermessenger",
        "companyName": "wella medical aid society ltd",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "head of operations",
        "companyName": "care",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "human resource supervisor",
        "companyName": "electricity supply corporation of malawi escom limited",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "salesman",
        "companyName": "namadzi bottlers",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "chief operating officer",
        "companyName": "lowama malawi",
        "category": "Business & Management",
        "sub-category": "Consultancy"
    },
    {
        "position": "waitress intern",
        "companyName": "kalibu-lek",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "chef",
        "companyName": "ndau lodge",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "associate lecturers",
        "companyName": "skyway university su",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "britam edge graduate trainee program",
        "companyName": "britam",
        "category": "Finance & Economics",
        "sub-category": "Insurance"
    },
    {
        "position": "sales and operations director",
        "companyName": "sparc systems ltd",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "head teacher",
        "companyName": "fairview private secondary school",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "enumerators",
        "companyName": "national statistical office",
        "category": "Social Sciences & Humanities",
        "sub-category": "Demography"
    },
    {
        "position": "driver",
        "companyName": "center for international forestry research cifor",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "producerspresenters radio two fm 3 positions",
        "companyName": "malawi broadcasting corporation mbc",
        "category": "Creative & Communication",
        "sub-category": "Media Production"
    },
    {
        "position": "chief producer light entertainment and drama development broadcasting unit",
        "companyName": "malawi broadcasting corporation mbc",
        "category": "Creative & Communication",
        "sub-category": "Media Production"
    },
    {
        "position": "monitoring evaluation accountability and learning meal manager -gcf project",
        "companyName": "save the children",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "gender equity and social inclusion specialist gesi-gcf project",
        "companyName": "save the children",
        "category": "Social Sciences & Humanities",
        "sub-category": "Gender Studies"
    },
    {
        "position": "programme coordinator -teacher professional development",
        "companyName": "save the children",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "draftsmandraughtsman",
        "companyName": "shayona cement",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "community development facilitator x10",
        "companyName": "malawi red cross society",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "gender and protection officer",
        "companyName": "malawi red cross society",
        "category": "Social Sciences & Humanities",
        "sub-category": "Gender Studies"
    },
    {
        "position": "quality assurance officer",
        "companyName": "autolube garage",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "chief administrative officer",
        "companyName": "chiradzulu district council",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "chief nursing officer",
        "companyName": "chiradzulu district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "principal land resource conservation officer",
        "companyName": "chiradzulu district council",
        "category": "Environmental Sciences",
        "sub-category": "Conservation"
    },
    {
        "position": "principal environmental health officer",
        "companyName": "chiradzulu district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "projects accountant",
        "companyName": "roads fund administration",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "director of agriculture",
        "companyName": "chiradzulu district council",
        "category": "Environmental Sciences",
        "sub-category": "Agriculture & Forestry"
    },
    {
        "position": "reservations clerk",
        "companyName": "sunbird lilongwe",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "plumber",
        "companyName": "sunbird lilongwe",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "accounting technician",
        "companyName": "unc project malawi",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "territory sales officer",
        "companyName": "malawi police sacco",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "social and behaviour change sbc specialist",
        "companyName": "msi reproductive choices",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "podcast producer paid intern",
        "companyName": "podcast malawi",
        "category": "Creative & Communication",
        "sub-category": "Media Production"
    },
    {
        "position": "student success coordinator",
        "companyName": "astria learning limited unima e-campus",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "research assistant",
        "companyName": "malawi university of business and applied sciences mubas",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "communication and civic education officer",
        "companyName": "pesticides control board pcb",
        "category": "Creative & Communication",
        "sub-category": "Public Relations"
    },
    {
        "position": "sales administrator",
        "companyName": "nico life insurance company limited",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "multiple positions nocma national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "lead geomarketing research analytics airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "head national sales airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "manager regional sales airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "manager regional sales airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "lead hbb marketing airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "lead hbb experience airtel malawi",
        "companyName": "airtel malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "lead hbb installation and maintenance airtel malawi",
        "companyName": "airtel malawi",
        "category": "Technology & Engineering",
        "sub-category": "Information Technology"
    },
    {
        "position": "expert in nature-based tourism and conservation southern and eastern africa tds-group",
        "companyName": "tds-group",
        "category": "Environmental Sciences",
        "sub-category": "Conservation"
    },
    {
        "position": "clinical officer malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "research nurse malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "research clinical officer malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "executive administrative assistant puma energy",
        "companyName": "puma energy",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "data officer intern old mutual",
        "companyName": "old mutual",
        "category": "Technology & Engineering",
        "sub-category": "Data Science"
    },
    {
        "position": "school library manager phoenix international primary school",
        "companyName": "phoenix international primary school",
        "category": "Education & Research",
        "sub-category": "Library Sciences"
    },
    {
        "position": "school administrator phoenix international primary school",
        "companyName": "phoenix international primary school",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "pharmacist bethesida community pharmacy",
        "companyName": "bethesida community pharmacy",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "waiters waitresses kitchen support staff private",
        "companyName": "private",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "warehouse operations supervisor one acre fund",
        "companyName": "one acre fund",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "warehouse operations senior supervisor one acre fund",
        "companyName": "one acre fund",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "malawi logistics data supervisor one acre fund",
        "companyName": "one acre fund",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "malawi inventory data senior coordinator one acre fund",
        "companyName": "one acre fund",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "project manager ministry of energy",
        "companyName": "ministry of energy",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "vehicle asset finance vaf and mortgage manager nbs bank plc",
        "companyName": "nbs bank plc",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    },
    {
        "position": "product analyst nbs bank plc",
        "companyName": "nbs bank plc",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    }, {
        "position": "teachers joyce banda foundation school",
        "companyName": "joyce banda foundation school",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "temporary office assistant national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "temporary depot operator national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "assistant security officer national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Legal & Security",
        "sub-category": "Corporate Security"
    },
    {
        "position": "temporary depot supervisor national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "temporary sap systems accountant national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "quality assurance officer holy family college of heath sciences",
        "companyName": "holy family college of heath sciences",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "gender officer undp",
        "companyName": "undp",
        "category": "Social Sciences & Humanities",
        "sub-category": "Gender Studies"
    },
    {
        "position": "learning culture intern heifer international",
        "companyName": "heifer international",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "hr and talent acquisition intern heifer international",
        "companyName": "heifer international",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "people and culture officer cure international",
        "companyName": "cure international",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "invoice validation repair order processing associate tiderise technologies inc",
        "companyName": "tiderise technologies inc",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "events planner internship lilongwe wildlife trust",
        "companyName": "lilongwe wildlife trust",
        "category": "Logistics & Operations",
        "sub-category": "Hospitality"
    },
    {
        "position": "senior officer agriculture gift of the givers foundation",
        "companyName": "gift of the givers foundation",
        "category": "Environmental Sciences",
        "sub-category": "Agriculture & Forestry"
    },
    {
        "position": "quality control supervisor rab processors ltd",
        "companyName": "rab processors ltd",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "regional marketing and communications officer africa water for people",
        "companyName": "water for people",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "finance manager planet green africa",
        "companyName": "planet green africa",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "beef production manager demeter farm",
        "companyName": "demeter farm",
        "category": "Environmental Sciences",
        "sub-category": "Agriculture & Forestry"
    },
    {
        "position": "workshop manager demeter farm",
        "companyName": "demeter farm",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "dam expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "hydrological expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "geotechinical expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "laboratory assistant kapaza christian private secondary school",
        "companyName": "kapaza christian private secondary school",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "field operations manager mount mulanje conservation trust",
        "companyName": "mount mulanje conservation trust",
        "category": "Environmental Sciences",
        "sub-category": "Conservation"
    },
    {
        "position": "cyber security analyst centenary bank",
        "companyName": "centenary bank",
        "category": "Technology & Engineering",
        "sub-category": "Cybersecurity"
    },
    {
        "position": "university vice president exploits university",
        "companyName": "exploits university",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "behavioural change communication intervention officer banja la mtsogolo",
        "companyName": "banja la mtsogolo",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "safety and compliance officer mega signs and media limited",
        "companyName": "mega signs and media limited",
        "category": "Legal & Security",
        "sub-category": "Corporate Security"
    },
    {
        "position": "gis operations support technician tiderise technologies inc",
        "companyName": "tiderise technologies inc",
        "category": "Technology & Engineering",
        "sub-category": "Information Technology"
    },
    {
        "position": "early childhood educatorteacher and teacher assistant st jay international christian academy",
        "companyName": "st jay international christian academy",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "site supervisor intercity building contractors",
        "companyName": "intercity building contractors",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "administrative assistant intern gogo malawi",
        "companyName": "gogo malawi",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "customer care representative intern gogo malawi",
        "companyName": "gogo malawi",
        "category": "Logistics & Operations",
        "sub-category": "Retail"
    },
    {
        "position": "head of merl southern africa plan international",
        "companyName": "plan international",
        "category": "Social Sciences & Humanities",
        "sub-category": "International Relations"
    },
    {
        "position": "head of business development southern africa plan international",
        "companyName": "plan international",
        "category": "Business & Management",
        "sub-category": "Consultancy"
    },
    {
        "position": "head of internal control southern africa plan international",
        "companyName": "plan international",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "head of it southern africa plan international",
        "companyName": "plan international",
        "category": "Technology & Engineering",
        "sub-category": "Information Technology"
    },
    {
        "position": "sales representatives mudi sacco ltd",
        "companyName": "mudi sacco ltd",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "driver nyasa tobacco buying limited",
        "companyName": "nyasa tobacco buying limited",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "principal labour officer karonga district council",
        "companyName": "karonga district council",
        "category": "Social Sciences & Humanities",
        "sub-category": "Political Science"
    },
    {
        "position": "chief irrigation engineer karonga district council",
        "companyName": "karonga district council",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "chief social welfare and child officer karonga district council",
        "companyName": "karonga district council",
        "category": "Social Sciences & Humanities",
        "sub-category": "Political Science"
    },
    {
        "position": "chief nutrition hiv aids officer karonga district council",
        "companyName": "karonga district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "assistant administrative officer karonga district council",
        "companyName": "karonga district council",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "clinical officer orthopaedics karonga district council",
        "companyName": "karonga district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "clinical officer surgery karonga district council",
        "companyName": "karonga district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "clinical officer obstetrics gynaecology karonga district council",
        "companyName": "karonga district council",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "programs manager malawi scotland partnership masp",
        "companyName": "malawi scotland partnership masp",
        "category": "Social Sciences & Humanities",
        "sub-category": "International Relations"
    },
    {
        "position": "head of performance management and impact african institute for development policy afidep",
        "companyName": "african institute for development policy afidep",
        "category": "Finance & Economics",
        "sub-category": "Economics"
    },
    {
        "position": "director of human capital development programmes african institute for development policy afidep",
        "companyName": "african institute for development policy afidep",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "director of sustainable growth governance african institute for development policy afidep",
        "companyName": "african institute for development policy afidep",
        "category": "Social Sciences & Humanities",
        "sub-category": "Political Science"
    },
    {
        "position": "hygiene supervisor mothers holdings ltd",
        "companyName": "mothers holdings ltd",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "human resources officers x2 mothers holdings ltd",
        "companyName": "mothers holdings ltd",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "biosampling officer multiple positions meiru",
        "companyName": "meiru",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "field officer multiple positions meiru",
        "companyName": "meiru",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "quality analyst presscane limited",
        "companyName": "presscane limited",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "finance and administration manager ufulu gardens",
        "companyName": "ufulu gardens",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "procurement officer malawi energy regulatory authority mera",
        "companyName": "malawi energy regulatory authority mera",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "chief operations officer lifeco life insurance company",
        "companyName": "lifeco life insurance company",
        "category": "Finance & Economics",
        "sub-category": "Insurance"
    },
    {
        "position": "finance officer pyxus agriculture limited",
        "companyName": "pyxus agriculture limited",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "project officer green livelihoods gl",
        "companyName": "green livelihoods gl",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "research assistants kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences",
        "category": "Education & Research",
        "sub-category": "Academic Instruction"
    },
    {
        "position": "site supervisor kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "research nurse 3 positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "research nurse intern 2 positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "booster study mac-cdac -various positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "senior maintenance manager malawi fertilizer company",
        "companyName": "malawi fertilizer company",
        "category": "Technology & Engineering",
        "sub-category": "Construction & Engineering"
    },
    {
        "position": "stores manager malawi fertilizer company",
        "companyName": "malawi fertilizer company",
        "category": "Logistics & Operations",
        "sub-category": "Transportation"
    },
    {
        "position": "security guard x2 gardener x2 mbwabwa holdings",
        "companyName": "mbwabwa holdings",
        "category": "Legal & Security",
        "sub-category": "Public Safety"
    },
    {
        "position": "human resource officer youth initiative for community development-malawi",
        "companyName": "youth initiative for community development-malawi",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "resource mobilisation officer youth initiative for community development-malawi",
        "companyName": "youth initiative for community development-malawi",
        "category": "Business & Management",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "accounts assistant youth initiative for community development",
        "companyName": "youth initiative for community development",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "it applications administrator enterprise services telekom networks malawi plc",
        "companyName": "telekom networks malawi plc",
        "category": "Technology & Engineering",
        "sub-category": "Information Technology"
    },
    {
        "position": "account relationship manager telekom networks malawi plc",
        "companyName": "telekom networks malawi plc",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    },
    {
        "position": "field officers x3 hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "epicenter project officers x2 hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Business & Management",
        "sub-category": "Project Management"
    },
    {
        "position": "project accountant hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "senior grants officer hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Finance & Economics",
        "sub-category": "Grants & Fundraising"
    },
    {
        "position": "grants partnerships and advocacy coordinator hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Social Sciences & Humanities",
        "sub-category": "Advocacy"
    },
    {
        "position": "legal practitioner kalekeni kaphale lawyers",
        "companyName": "kalekeni kaphale lawyers",
        "category": "Legal & Security",
        "sub-category": "Legal Services"
    },
    {
        "position": "multiple positions hunger project malawi hunger project malawi",
        "companyName": "hunger project malawi",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "business enterprise services director amg global",
        "companyName": "amg global",
        "category": "Business & Management",
        "sub-category": "Consulting"
    },
    {
        "position": "aircraft maintenance technicians malawi airlines limited",
        "companyName": "malawi airlines limited",
        "category": "Technology & Engineering",
        "sub-category": "Aviation"
    },
    {
        "position": "monitoring evaluation learning and membership coordinator civil society education coalition csec",
        "companyName": "civil society education coalition csec",
        "category": "Education & Research",
        "sub-category": "Monitoring & Evaluation"
    },
    {
        "position": "accountant civil society education coalition csec",
        "companyName": "civil society education coalition csec",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "multiple positions infracon limited infracon limited",
        "companyName": "infracon limited",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "member service officers msilikali sacco",
        "companyName": "msilikali sacco",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    },
    {
        "position": "business strategy officer msilikali sacco",
        "companyName": "msilikali sacco",
        "category": "Business & Management",
        "sub-category": "Strategic Planning"
    },
    {
        "position": "multiple positions partners in hope proffessional positions partners in hope pih",
        "companyName": "partners in hope pih",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "multiple positions partners in hope pih partners in hope pih",
        "companyName": "partners in hope pih",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "administration and finance assistant unv ltd",
        "companyName": "unv ltd",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "child protection technical coordinator save the children",
        "companyName": "save the children",
        "category": "Social Sciences & Humanities",
        "sub-category": "Child Protection"
    },
    {
        "position": "multiple positions machinga district council machinga district counc",
        "companyName": "machinga district counc",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "case management clinical linkages specialist project hope",
        "companyName": "project hope",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Clinical Care"
    },
    {
        "position": "ovc program officer project hope",
        "companyName": "project hope",
        "category": "Social Sciences & Humanities",
        "sub-category": "Child Protection"
    },
    {
        "position": "social welfare officer project hope",
        "companyName": "project hope",
        "category": "Social Sciences & Humanities",
        "sub-category": "Social Work"
    },
    {
        "position": "community linkages coordinator x25 project hope",
        "companyName": "project hope",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Public Health"
    },
    {
        "position": "monitoring evaluation learning mel specialist project hope",
        "companyName": "project hope",
        "category": "Education & Research",
        "sub-category": "Monitoring & Evaluation"
    },
    {
        "position": "district monitoring evaluation and learning mel officer x8 project hope",
        "companyName": "project hope",
        "category": "Education & Research",
        "sub-category": "Monitoring & Evaluation"
    },
    {
        "position": "assistant mel officer x16 project hope",
        "companyName": "project hope",
        "category": "Education & Research",
        "sub-category": "Monitoring & Evaluation"
    },
    {
        "position": "temporary drivers x5 electricity supply corporation of malawi escom",
        "companyName": "electricity supply corporation of malawi escom",
        "category": "Logistics & Transport",
        "sub-category": "Driving"
    },
    {
        "position": "electrician realsim",
        "companyName": "realsim",
        "category": "Technology & Engineering",
        "sub-category": "Electrical"
    },
    {
        "position": "plumber realsim",
        "companyName": "realsim",
        "category": "Technology & Engineering",
        "sub-category": "Plumbing"
    },
    {
        "position": "manager business standard bank plc",
        "companyName": "standard bank plc",
        "category": "Finance & Economics",
        "sub-category": "Banking"
    },
    {
        "position": "research nurse malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Nursing"
    },
    {
        "position": "finance manager malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "senior hr services coordinator malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "safety officer burn",
        "companyName": "burn",
        "category": "Legal & Security",
        "sub-category": "Occupational Safety"
    },
    {
        "position": "full stack developer inga",
        "companyName": "inga",
        "category": "ICT & Software",
        "sub-category": "Software Development"
    },
    {
        "position": "funded traineeship for young graduates at the eu delegation to malawi european external action service eeas",
        "companyName": "european external action service eeas",
        "category": "Other",
        "sub-category": "Internship"
    },
    {
        "position": "pharmacist mch investments limited",
        "companyName": "mch investments limited",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Pharmacy"
    },
    {
        "position": "operations officer tmm",
        "companyName": "tmm",
        "category": "Business & Management",
        "sub-category": "Operations"
    },
    {
        "position": "multiple positions salima sugar company ltd salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "agriculture manager salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Agriculture & Environment",
        "sub-category": "Agricultural Management"
    },
    {
        "position": "service engineer salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Technology & Engineering",
        "sub-category": "Engineering"
    },
    {
        "position": "mechanical engineer salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Technology & Engineering",
        "sub-category": "Mechanical Engineering"
    },
    {
        "position": "receptionist salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "marketing manager salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Business & Management",
        "sub-category": "Marketing"
    },
    {
        "position": "public relations officer salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Social Sciences & Humanities",
        "sub-category": "Public Relations"
    },
    {
        "position": "procurement specialist salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Business & Management",
        "sub-category": "Procurement"
    },
    {
        "position": "ict manager salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "ICT & Software",
        "sub-category": "IT Management"
    },
    {
        "position": "warehouse manager salima sugar company ltd",
        "companyName": "salima sugar company ltd",
        "category": "Logistics & Transport",
        "sub-category": "Warehouse Management"
    },
    {
        "position": "ehs specialist jti japan tobacco international",
        "companyName": "jti japan tobacco international",
        "category": "Legal & Security",
        "sub-category": "Environmental Health & Safety"
    },
    {
        "position": "administrative assistantdriver mphunzitsi sacco",
        "companyName": "mphunzitsi sacco",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "chief laboratory technician pirimiti hospital",
        "companyName": "pirimiti hospital",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Laboratory Science"
    },
    {
        "position": "farm manager precision recruitment international",
        "companyName": "precision recruitment international",
        "category": "Agriculture & Environment",
        "sub-category": "Agricultural Management"
    },
    {
        "position": "chefs and housekeepers ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Hospitality & Tourism",
        "sub-category": "Catering & Housekeeping"
    },
    {
        "position": "front office staff ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Business & Management",
        "sub-category": "Customer Service"
    },
    {
        "position": "international bus drivers ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Logistics & Transport",
        "sub-category": "Driving"
    },
    {
        "position": "human resource officer ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "operations supervisor ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Business & Management",
        "sub-category": "Operations"
    },
    {
        "position": "multiple positions ulemu bus services ubs ulemu bus services ubs",
        "companyName": "ulemu bus services ubs",
        "category": "Other",
        "sub-category": "Multiple Roles"
    },
    {
        "position": "senior manager technology and digital transformation tony blair institute for global change",
        "companyName": "tony blair institute for global change",
        "category": "ICT & Software",
        "sub-category": "Digital Transformation"
    },
    {
        "position": "operations and security coordinator maternity cover tony blair institute for global change",
        "companyName": "tony blair institute for global change",
        "category": "Legal & Security",
        "sub-category": "Security Coordination"
    },
    {
        "position": "terms of reference for baseline study of the project girls initiative for resilient learning and support in malawi rwanda and zambia oxfam",
        "companyName": "oxfam",
        "category": "Research & Development",
        "sub-category": "Baseline Study"
    },
    {
        "position": "administrative assistant galloway co",
        "companyName": "galloway co",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "farm workshops manager precision recruitment international",
        "companyName": "precision recruitment international",
        "category": "Agriculture & Environment",
        "sub-category": "Agricultural Equipment Management"
    },
    {
        "position": "training coordinator spark microgrants",
        "companyName": "spark microgrants",
        "category": "Education & Training",
        "sub-category": "Training"
    },
    {
        "position": "district coordinators nutrition international",
        "companyName": "nutrition international",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Nutrition"
    },
    {
        "position": "research assistant unc project",
        "companyName": "unc project",
        "category": "Research & Development",
        "sub-category": "Research Assistant"
    },
    {
        "position": "consultancy to facilitate the development of a monitoring and evaluation framework for communications and public engagement department malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Research & Development",
        "sub-category": "Monitoring & Evaluation"
    },
    {
        "position": "operations manager savanna finacial services",
        "companyName": "savanna finacial services",
        "category": "Finance & Economics",
        "sub-category": "Financial Operations"
    },
    {
        "position": "assistant financial accountant public procurement and disposal of assets authority",
        "companyName": "public procurement and disposal of assets authority",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "finance officer unitrans malawi limited",
        "companyName": "unitrans malawi limited",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "pharmacist wholesale pharmaexpress",
        "companyName": "pharmaexpress",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Pharmacy"
    },
    {
        "position": "civil engineer amg global",
        "companyName": "amg global",
        "category": "Technology & Engineering",
        "sub-category": "Civil Engineering"
    },
    {
        "position": "operations manager administration marymount catholic secondary school",
        "companyName": "marymount catholic secondary school",
        "category": "Education & Training",
        "sub-category": "School Administration"
    },
    {
        "position": "administrative assistant umunthu plus",
        "companyName": "umunthu plus",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "administrative assistant umunthu plus",
        "companyName": "umunthu plus",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "loan officers united civil servants sacco",
        "companyName": "united civil servants sacco",
        "category": "Finance & Economics",
        "sub-category": "Microfinance"
    },
    {
        "position": "technical advisor social protection giz",
        "companyName": "giz",
        "category": "Government & NGO",
        "sub-category": "Social Protection"
    },
    {
        "position": "technical advisor for endev giz",
        "companyName": "giz",
        "category": "Energy & Environment",
        "sub-category": "Renewable Energy"
    },
    {
        "position": "procrument supervisor plasticycle ltd",
        "companyName": "plasticycle ltd",
        "category": "Business & Management",
        "sub-category": "Procurement & Supply Chain"
    },
    {
        "position": "head of strategy data digital old mutual",
        "companyName": "old mutual",
        "category": "ICT & Software",
        "sub-category": "Digital Strategy"
    },
    {
        "position": "marketing and sales intern kuwala travel and tours ltd",
        "companyName": "kuwala travel and tours ltd",
        "category": "Hospitality & Tourism",
        "sub-category": "Sales & Marketing"
    },
    {
        "position": "finance officer spark microgrants",
        "companyName": "spark microgrants",
        "category": "Finance & Economics",
        "sub-category": "Financial Management"
    },
    {
        "position": "temporary software developer elizabeth glaser pediatric aids foundation",
        "companyName": "elizabeth glaser pediatric aids foundation",
        "category": "ICT & Software",
        "sub-category": "Software Development"
    },
    {
        "position": "loan officer lolc finance limited",
        "companyName": "lolc finance limited",
        "category": "Finance & Economics",
        "sub-category": "Microfinance"
    },
    {
        "position": "research fellow university of malawi",
        "companyName": "university of malawi",
        "category": "Research & Development",
        "sub-category": "Academic Research"
    },
    {
        "position": "electronics informatics intern university of malawi",
        "companyName": "university of malawi",
        "category": "ICT & Software",
        "sub-category": "Electronics & Informatics"
    },
    {
        "position": "laboratory technician um 10 university of malawi",
        "companyName": "university of malawi",
        "category": "Healthcare & Life Sciences",
        "sub-category": "Laboratory Technology"
    },
    {
        "position": "call for applications for internship positions re-advertised university of malawi",
        "companyName": "university of malawi",
        "category": "Education & Training",
        "sub-category": "Internships"
    },
    {
        "position": "human resources manager readymix concrete company",
        "companyName": "readymix concrete company",
        "category": "Business & Management",
        "sub-category": "Human Resources"
    },
    {
        "position": "intern administrative assistant synergy capital partners",
        "companyName": "synergy capital partners",
        "category": "Business & Management",
        "sub-category": "Administration"
    },
    {
        "position": "chief executive officer teachers council of malawi tcm",
        "companyName": "teachers council of malawi tcm",
        "category": "Education & Training",
        "sub-category": "Leadership & Governance"
    },
    {
        "position": "director of compliance services teachers council of malawi tcm",
        "companyName": "teachers council of malawi tcm",
        "category": "Legal & Security",
        "sub-category": "Regulatory Compliance"
    },
    {
        "position": "coordinator for basic education church of central africa presbyterian ccap",
        "companyName": "church of central africa presbyterian ccap",
        "category": "Education & Training",
        "sub-category": "Basic Education"
    },
    {
        "position": "production manager choice products limited",
        "companyName": "choice products limited",
        "category": "Manufacturing & Production",
        "sub-category": "Production Management"
    },
    {
        "position": "office assistantmessenger agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret",
        "category": "Business & Management",
        "sub-category": "Office Support"
    },
    {
        "position": "motor vehicle driver agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret",
        "category": "Logistics & Transport",
        "sub-category": "Driving"
    },
    {
        "position": "financial accountant agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "general manager property old mutual",
        "companyName": "old mutual",
        "category": "Real Estate & Property",
        "sub-category": "Property Management"
    },
    {
        "position": "courier manager agma holdings limited",
        "companyName": "agma holdings limited",
        "category": "Logistics & Transport",
        "sub-category": "Courier Services"
    },
    {
        "position": "finance officer agma holdings limited",
        "companyName": "agma holdings limited",
        "category": "Finance & Economics",
        "sub-category": "Financial Management"
    },
    {
        "position": "marketing sales officer ccap nkhoma synod",
        "companyName": "ccap nkhoma synod",
        "category": "Marketing & Communications",
        "sub-category": "Sales & Promotion"
    },
    {
        "position": "operations officer ccap nkhoma synod",
        "companyName": "ccap nkhoma synod",
        "category": "Business & Management",
        "sub-category": "Operations"
    },
    {
        "position": "junior accountant central poultry 2000 ltd",
        "companyName": "central poultry 2000 ltd",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "leaf processing supervisor jti japan tobacco international",
        "companyName": "jti japan tobacco international",
        "category": "Manufacturing & Production",
        "sub-category": "Processing & Quality Control"
    },
    {
        "position": "malware analyst officer malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "ICT & Software",
        "sub-category": "Cybersecurity"
    },
    {
        "position": "legal enforcement manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "Legal & Security",
        "sub-category": "Law Enforcement"
    },
    {
        "position": "security and safety manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "Legal & Security",
        "sub-category": "Security Management"
    },
    {
        "position": "information communication technology ict manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "ICT & Software",
        "sub-category": "IT Management"
    },
    {
        "position": "management accountant malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "economics regulation manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra",
        "category": "Government & NGO",
        "sub-category": "Economic Policy"
    },
    {
        "position": "intern compliance officer edukans",
        "companyName": "edukans",
        "category": "Legal & Security",
        "sub-category": "Compliance"
    },
    {
        "position": "strategic process support volunteer edukans",
        "companyName": "edukans",
        "category": "NGO & Volunteering",
        "sub-category": "Strategy & Planning"
    },
    {
        "position": "driveroffice assistant edukans",
        "companyName": "edukans",
        "category": "Logistics & Transport",
        "sub-category": "Driving & Support"
    },
    {
        "position": "driver winrock international",
        "companyName": "winrock international",
        "category": "Logistics & Transport",
        "sub-category": "Driving"
    },
    {
        "position": "call for pre-phd internship applications stremm project malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Education & Training",
        "sub-category": "Internships & Research"
    },
    {
        "position": "call for pre-phd internship applications impact-malawi project malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust",
        "category": "Education & Training",
        "sub-category": "Internships & Research"
    },
    {
        "position": "information technology manager centenary bank",
        "companyName": "centenary bank",
        "category": "ICT & Software",
        "sub-category": "IT Management"
    },
    {
        "position": "network support officer centenary bank",
        "companyName": "centenary bank",
        "category": "ICT & Software",
        "sub-category": "Network Administration"
    },
    {
        "position": "driver linde hotel",
        "companyName": "linde hotel",
        "category": "Logistics & Transport",
        "sub-category": "Driving"
    },
    {
        "position": "administrative assistant maya private school",
        "companyName": "maya private school",
        "category": "Education & Training",
        "sub-category": "Administration"
    },
    {
        "position": "junior accountant plasticycle ltd",
        "companyName": "plasticycle ltd",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    },
    {
        "position": "program manager disabled women in africa - diwa",
        "companyName": "disabled women in africa - diwa",
        "category": "NGO & Volunteering",
        "sub-category": "Program Management"
    },
    {
        "position": "engineering shift controller mechanical alliance one tobacco malawi limited",
        "companyName": "alliance one tobacco malawi limited",
        "category": "Engineering & Technical",
        "sub-category": "Mechanical Engineering"
    },
    {
        "position": "green leaf services superintendent alliance one tobacco malawi limited",
        "companyName": "alliance one tobacco malawi limited",
        "category": "Agriculture & Environment",
        "sub-category": "Agribusiness"
    },
    {
        "position": "field officer x2 fincoop savings and credit cooperative limited",
        "companyName": "fincoop savings and credit cooperative limited",
        "category": "Finance & Economics",
        "sub-category": "Field Operations"
    },
    {
        "position": "accountant angsoma development commission",
        "companyName": "angsoma development commission",
        "category": "Finance & Economics",
        "sub-category": "Accountancy"
    }
]


def convert_to_csv_string(data_list):
    """
    Converts a list of dictionaries to a list of CSV formatted strings.
    Each string contains the 'position' and 'category' fields.
    """
    csv_strings = []
    for item in data_list:
        # Use .get() for safety if key might be missing
        position = item.get("position", "")
        category = item.get("category", "")
        # Enclose each field in double quotes and join with a comma
        csv_row = f'"{position}","{category}"'
        csv_strings.append(csv_row)
    return csv_strings


def write_to_csv_file(data_list, filename="output.csv"):
    """
    Converts data and writes it to a CSV file.
    Each row will contain the 'position' and 'category'.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write header (optional, uncomment if needed)
        # csv_writer.writerow(["position", "category"])
        for item in data_list:
            position = item.get("position", "")
            category = item.get("category", "")
            csv_writer.writerow([position, category])
    print(f"Data successfully written to {filename}")


# --- Option 1: Get a list of CSV formatted strings ---
csv_output_strings = convert_to_csv_string(data)

# Print the CSV strings
print("--- CSV Formatted Strings ---")
for row_string in csv_output_strings:
    print(row_string)

# --- Option 2: Write directly to a CSV file ---
# This is generally the recommended way to create CSV files.
output_file_name = "job_postings.csv"
write_to_csv_file(data, output_file_name)

print(f"\n--- CSV File Output ---")
print(f"The data has been written to '{output_file_name}'.")
print("It will look like this inside the file:")
# To demonstrate the file content:
with open(output_file_name, 'r', encoding='utf-8') as f:
    print(f.read())
