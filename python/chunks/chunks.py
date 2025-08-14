import json
import os

# Example input list (you can load this from a file if needed)
data = [
    {
        "position": "multiple positions nocma national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "lead geomarketing research analytics airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "head national sales airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "manager regional sales airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "manager regional sales airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "lead hbb marketing airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "lead hbb experience airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "lead hbb installation and maintenance airtel malawi",
        "companyName": "airtel malawi"
    },
    {
        "position": "expert in nature-based tourism and conservation southern and eastern africa tds-group",
        "companyName": "tds-group"
    },
    {
        "position": "clinical officer malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "research nurse malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "research clinical officer malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "executive administrative assistant puma energy",
        "companyName": "puma energy"
    },
    {
        "position": "data officer intern old mutual",
        "companyName": "old mutual"
    },
    {
        "position": "school library manager phoenix international primary school",
        "companyName": "phoenix international primary school"
    },
    {
        "position": "school administrator phoenix international primary school",
        "companyName": "phoenix international primary school"
    },
    {
        "position": "pharmacist bethesida community pharmacy",
        "companyName": "bethesida community pharmacy"
    },
    {
        "position": "waiters waitresses kitchen support staff private",
        "companyName": "private"
    },
    {
        "position": "warehouse operations supervisor one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "warehouse operations senior supervisor one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "malawi logistics data supervisor one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "malawi inventory data senior coordinator one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "project manager ministry of energy",
        "companyName": "ministry of energy"
    },
    {
        "position": "vehicle asset finance vaf and mortgage manager nbs bank plc",
        "companyName": "nbs bank plc"
    },
    {
        "position": "product analyst nbs bank plc",
        "companyName": "nbs bank plc"
    },
    {
        "position": "bancassurance officer nbs bank plc",
        "companyName": "nbs bank plc"
    },
    {
        "position": "principal nursing officer pirimiti hospital",
        "companyName": "pirimiti hospital"
    },
    {
        "position": "health and nutrition officer sparkle foundation malawi",
        "companyName": "sparkle foundation malawi"
    },
    {
        "position": "education in emergencies eie project manager save the children",
        "companyName": "save the children"
    },
    {
        "position": "meal coordinator echo arise save the children",
        "companyName": "save the children"
    },
    {
        "position": "student success coordinator astria learning limited unima e-campus",
        "companyName": "astria learning limited unima e-campus"
    },
    {
        "position": "accounts receivables officerdebt collector dekha hr consultancy",
        "companyName": "dekha hr consultancy"
    },
    {
        "position": "front desk supervisor matundu cottage beach resort",
        "companyName": "matundu cottage beach resort"
    },
    {
        "position": "reservations officer matundu cottage beach resort ltd",
        "companyName": "matundu cottage beach resort ltd"
    },
    {
        "position": "food server waiterwaitress matundu cottage beach resort ltd",
        "companyName": "matundu cottage beach resort ltd"
    },
    {
        "position": "chef matundu cottage beach resort",
        "companyName": "matundu cottage beach resort"
    },
    {
        "position": "finance and admin officer mbulo enterprises ltd",
        "companyName": "mbulo enterprises ltd"
    },
    {
        "position": "personal assistant paychangu",
        "companyName": "paychangu"
    },
    {
        "position": "commissioned sales agents lifeco life insurance limited",
        "companyName": "lifeco life insurance limited"
    },
    {
        "position": "quantity surveyor milanzi interiors",
        "companyName": "milanzi interiors"
    },
    {
        "position": "architect milanzi interiors",
        "companyName": "milanzi interiors"
    },
    {
        "position": "administrative assistant milanzi interiors",
        "companyName": "milanzi interiors"
    },
    {
        "position": "feedlot supervisor demeter farm",
        "companyName": "demeter farm"
    },
    {
        "position": "veterinary technician demeter farm",
        "companyName": "demeter farm"
    },
    {
        "position": "accounting clerk demeter farm",
        "companyName": "demeter farm"
    },
    {
        "position": "branch manager ecobank",
        "companyName": "ecobank"
    },
    {
        "position": "senior internal audit officer ecobank",
        "companyName": "ecobank"
    },
    {
        "position": "scale clerks x30 lujeri tea estates limited",
        "companyName": "lujeri tea estates limited"
    },
    {
        "position": "senior programme manager-echo arise save the children",
        "companyName": "save the children"
    },
    {
        "position": "purchase supervisor shayona cement corporation",
        "companyName": "shayona cement corporation"
    },
    {
        "position": "teachers joyce banda foundation school",
        "companyName": "joyce banda foundation school"
    },
    {
        "position": "temporary office assistant national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "temporary depot operator national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "assistant security officer national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "temporary depot supervisor national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "temporary sap systems accountant national oil company of malawi nocma",
        "companyName": "national oil company of malawi nocma"
    },
    {
        "position": "quality assurance officer holy family college of heath sciences",
        "companyName": "holy family college of heath sciences"
    },
    {
        "position": "gender officer undp",
        "companyName": "undp"
    },
    {
        "position": "learning culture intern heifer international",
        "companyName": "heifer international"
    },
    {
        "position": "hr and talent acquisition intern heifer international",
        "companyName": "heifer international"
    },
    {
        "position": "people and culture officer cure international",
        "companyName": "cure international"
    },
    {
        "position": "invoice validation repair order processing associate tiderise technologies inc",
        "companyName": "tiderise technologies inc"
    },
    {
        "position": "events planner internship lilongwe wildlife trust",
        "companyName": "lilongwe wildlife trust"
    },
    {
        "position": "senior officer agriculture gift of the givers foundation",
        "companyName": "gift of the givers foundation"
    },
    {
        "position": "quality control supervisor rab processors ltd",
        "companyName": "rab processors ltd"
    },
    {
        "position": "regional marketing and communications officer africa water for people",
        "companyName": "water for people"
    },
    {
        "position": "finance manager planet green africa",
        "companyName": "planet green africa"
    },
    {
        "position": "beef production manager demeter farm",
        "companyName": "demeter farm"
    },
    {
        "position": "workshop manager demeter farm",
        "companyName": "demeter farm"
    },
    {
        "position": "dam expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip"
    },
    {
        "position": "hydrological expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip"
    },
    {
        "position": "geotechinical expert malawi watershed services improvement project mwasip",
        "companyName": "malawi watershed services improvement project mwasip"
    },
    {
        "position": "laboratory assistant kapaza christian private secondary school",
        "companyName": "kapaza christian private secondary school"
    },
    {
        "position": "field operations manager mount mulanje conservation trust",
        "companyName": "mount mulanje conservation trust"
    },
    {
        "position": "cyber security analyst centenary bank",
        "companyName": "centenary bank"
    },
    {
        "position": "university vice president exploits university",
        "companyName": "exploits university"
    },
    {
        "position": "behavioural change communication intervention officer banja la mtsogolo",
        "companyName": "banja la mtsogolo"
    },
    {
        "position": "safety and compliance officer mega signs and media limited",
        "companyName": "mega signs and media limited"
    },
    {
        "position": "gis operations support technician tiderise technologies inc",
        "companyName": "tiderise technologies inc"
    },
    {
        "position": "early childhood educatorteacher and teacher assistant st jay international christian academy",
        "companyName": "st jay international christian academy"
    },
    {
        "position": "site supervisor intercity building contractors",
        "companyName": "intercity building contractors"
    },
    {
        "position": "administrative assistant intern gogo malawi",
        "companyName": "gogo malawi"
    },
    {
        "position": "customer care representative intern gogo malawi",
        "companyName": "gogo malawi"
    },
    {
        "position": "head of merl southern africa plan international",
        "companyName": "plan international"
    },
    {
        "position": "head of business development southern africa plan international",
        "companyName": "plan international"
    },
    {
        "position": "head of internal control southern africa plan international",
        "companyName": "plan international"
    },
    {
        "position": "head of it southern africa plan international",
        "companyName": "plan international"
    },
    {
        "position": "sales representatives mudi sacco ltd",
        "companyName": "mudi sacco ltd"
    },
    {
        "position": "driver nyasa tobacco buying limited",
        "companyName": "nyasa tobacco buying limited"
    },
    {
        "position": "principal labour officer karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "chief irrigation engineer karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "chief social welfare and child officer karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "chief nutrition hiv aids officer karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "assistant administrative officer karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "clinical officer orthopaedics karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "clinical officer surgery karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "clinical officer obstetrics gynaecology karonga district council",
        "companyName": "karonga district council"
    },
    {
        "position": "programs manager malawi scotland partnership masp",
        "companyName": "malawi scotland partnership masp"
    },
    {
        "position": "head of performance management and impact african institute for development policy afidep",
        "companyName": "african institute for development policy afidep"
    },
    {
        "position": "director of human capital development programmes african institute for development policy afidep",
        "companyName": "african institute for development policy afidep"
    },
    {
        "position": "director of sustainable growth governance african institute for development policy afidep",
        "companyName": "african institute for development policy afidep"
    },
    {
        "position": "hygiene supervisor mothers holdings ltd",
        "companyName": "mothers holdings ltd"
    },
    {
        "position": "human resources officers x2 mothers holdings ltd",
        "companyName": "mothers holdings ltd"
    },
    {
        "position": "biosampling officer multiple positions meiru",
        "companyName": "meiru"
    },
    {
        "position": "field officer multiple positions meiru",
        "companyName": "meiru"
    },
    {
        "position": "quality analyst presscane limited",
        "companyName": "presscane limited"
    },
    {
        "position": "finance and administration manager ufulu gardens",
        "companyName": "ufulu gardens"
    },
    {
        "position": "procurement officer malawi energy regulatory authority mera",
        "companyName": "malawi energy regulatory authority mera"
    },
    {
        "position": "chief operations officer lifeco life insurance company",
        "companyName": "lifeco life insurance company"
    },
    {
        "position": "finance officer pyxus agriculture limited",
        "companyName": "pyxus agriculture limited"
    },
    {
        "position": "project officer green livelihoods gl",
        "companyName": "green livelihoods gl"
    },
    {
        "position": "research assistants kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "site supervisor kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "research nurse 3 positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "research nurse intern 2 positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "booster study mac-cdac -various positions kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "senior maintenance manager malawi fertilizer company",
        "companyName": "malawi fertilizer company"
    },
    {
        "position": "stores manager malawi fertilizer company",
        "companyName": "malawi fertilizer company"
    },
    {
        "position": "security guard x2 gardener x2 mbwabwa holdings",
        "companyName": "mbwabwa holdings"
    },
    {
        "position": "human resource officer youth initiative for community development-malawi",
        "companyName": "youth initiative for community development-malawi"
    },
    {
        "position": "resource mobilisation officer youth initiative for community development-malawi",
        "companyName": "youth initiative for community development-malawi"
    },
    {
        "position": "accounts assistant youth initiative for community development",
        "companyName": "youth initiative for community development"
    },
    {
        "position": "it applications administrator enterprise services telekom networks malawi plc",
        "companyName": "telekom networks malawi plc"
    },
    {
        "position": "account relationship manager telekom networks malawi plc",
        "companyName": "telekom networks malawi plc"
    },
    {
        "position": "field officers x3 hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "epicenter project officers x2 hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "project accountant hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "senior grants officer hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "grants partnerships and advocacy coordinator hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "legal practitioner kalekeni kaphale lawyers",
        "companyName": "kalekeni kaphale lawyers"
    },
    {
        "position": "multiple positions hunger project malawi hunger project malawi",
        "companyName": "hunger project malawi"
    },
    {
        "position": "business enterprise services director amg global",
        "companyName": "amg global"
    },
    {
        "position": "aircraft maintenance technicians malawi airlines limited",
        "companyName": "malawi airlines limited"
    },
    {
        "position": "monitoring evaluation learning and membership coordinator civil society education coalition csec",
        "companyName": "civil society education coalition csec"
    },
    {
        "position": "accountant civil society education coalition csec",
        "companyName": "civil society education coalition csec"
    },
    {
        "position": "multiple positions infracon limited infracon limited",
        "companyName": "infracon limited"
    },
    {
        "position": "member service officers msilikali sacco",
        "companyName": "msilikali sacco"
    },
    {
        "position": "business strategy officer msilikali sacco",
        "companyName": "msilikali sacco"
    },
    {
        "position": "multiple positions partners in hope proffessional positions partners in hope pih",
        "companyName": "partners in hope pih"
    },
    {
        "position": "multiple positions partners in hope pih partners in hope pih",
        "companyName": "partners in hope pih"
    },
    {
        "position": "administration and finance assistant unv ltd",
        "companyName": "unv ltd"
    },
    {
        "position": "child protection technical coordinator save the children",
        "companyName": "save the children"
    },
    {
        "position": "multiple positions machinga district council machinga district counc",
        "companyName": "machinga district counc"
    },
    {
        "position": "case management clinical linkages specialist project hope",
        "companyName": "project hope"
    },
    {
        "position": "ovc program officer project hope",
        "companyName": "project hope"
    },
    {
        "position": "social welfare officer project hope",
        "companyName": "project hope"
    },
    {
        "position": "community linkages coordinator x25 project hope",
        "companyName": "project hope"
    },
    {
        "position": "monitoring evaluation learning mel specialist project hope",
        "companyName": "project hope"
    },
    {
        "position": "district monitoring evaluation and learning mel officer x8 project hope",
        "companyName": "project hope"
    },
    {
        "position": "assistant mel officer x16 project hope",
        "companyName": "project hope"
    },
    {
        "position": "district team lead project hope",
        "companyName": "project hope"
    },
    {
        "position": "receptionist project hope",
        "companyName": "project hope"
    },
    {
        "position": "driver x9 project hope",
        "companyName": "project hope"
    },
    {
        "position": "multiple positions project hope project hope",
        "companyName": "project hope"
    },
    {
        "position": "paralegal officer tiderise technologies inc",
        "companyName": "tiderise technologies inc"
    },
    {
        "position": "marketing coordinator rainbow agro zambia",
        "companyName": "rainbow agro zambia"
    },
    {
        "position": "multiple positions gateway way mall gate way mall",
        "companyName": "gate way mall"
    },
    {
        "position": "stores clerk stephanos foundation",
        "companyName": "stephanos foundation"
    },
    {
        "position": "security guard stephanos foundation",
        "companyName": "stephanos foundation"
    },
    {
        "position": "housekeeper stephanos foundation",
        "companyName": "stephanos foundation"
    },
    {
        "position": "assistant benefits administration officer public service pension trust fund",
        "companyName": "public service pension trust fund"
    },
    {
        "position": "public relations officer public service pension trust fund",
        "companyName": "public service pension trust fund"
    },
    {
        "position": "prestige relationship officer first capital bank",
        "companyName": "first capital bank"
    },
    {
        "position": "seed program zambia and malawi mennonite central committee",
        "companyName": "mennonite central committee"
    },
    {
        "position": "senior field officer innovations for poverty action ipa",
        "companyName": "innovations for poverty action ipa"
    },
    {
        "position": "field officer innovations for poverty action ipa",
        "companyName": "innovations for poverty action ipa"
    },
    {
        "position": "malawi senior field officer one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "billing assistant mwaiwathu private hospital limited",
        "companyName": "mwaiwathu private hospital limited"
    },
    {
        "position": "international desk assistant mwaiwathu private hospital limited",
        "companyName": "mwaiwathu private hospital limited"
    },
    {
        "position": "medical equipment inventory controller mwaiwathu private hospital",
        "companyName": "mwaiwathu private hospital"
    },
    {
        "position": "senior manager nonprofit business development africa water for people",
        "companyName": "water for people"
    },
    {
        "position": "regional marketing and communications officer africa water for people",
        "companyName": "water for people"
    },
    {
        "position": "project accountant the diocese of karonga",
        "companyName": "the diocese of karonga"
    },
    {
        "position": "finance and administration coordinator islamic relief worldwide irw",
        "companyName": "islamic relief worldwide irw"
    },
    {
        "position": "internal auditor technical roads authority",
        "companyName": "roads authority"
    },
    {
        "position": "temporary drivers x5 electricity supply corporation of malawi escom",
        "companyName": "electricity supply corporation of malawi escom"
    },
    {
        "position": "electrician realsim",
        "companyName": "realsim"
    },
    {
        "position": "plumber realsim",
        "companyName": "realsim"
    },
    {
        "position": "manager business standard bank plc",
        "companyName": "standard bank plc"
    },
    {
        "position": "research nurse malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "finance manager malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "senior hr services coordinator malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "safety officer burn",
        "companyName": "burn"
    },
    {
        "position": "full stack developer inga",
        "companyName": "inga"
    },
    {
        "position": "funded traineeship for young graduates at the eu delegation to malawi european external action service eeas",
        "companyName": "european external action service eeas"
    },
    {
        "position": "pharmacist mch investments limited",
        "companyName": "mch investments limited"
    },
    {
        "position": "operations officer tmm",
        "companyName": "tmm"
    },
    {
        "position": "multiple positions salima sugar company ltd salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "agriculture manager salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "service engineer salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "mechanical engineer salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "receptionist salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "marketing manager salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "public relations officer salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "procurement specialist salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "ict manager salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "warehouse manager salima sugar company ltd",
        "companyName": "salima sugar company ltd"
    },
    {
        "position": "ehs specialist jti japan tobacco international",
        "companyName": "jti japan tobacco international"
    },
    {
        "position": "administrative assistantdriver mphunzitsi sacco",
        "companyName": "mphunzitsi sacco"
    },
    {
        "position": "chief laboratory technician pirimiti hospital",
        "companyName": "pirimiti hospital"
    },
    {
        "position": "farm manager precision recruitment international",
        "companyName": "precision recruitment international"
    },
    {
        "position": "chefs and housekeepers ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "front office staff ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "international bus drivers ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "human resource officer ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "operations supervisor ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "multiple positions ulemu bus services ubs ulemu bus services ubs",
        "companyName": "ulemu bus services ubs"
    },
    {
        "position": "senior manager technology and digital transformation tony blair institute for global change",
        "companyName": "tony blair institute for global change"
    },
    {
        "position": "operations and security coordinator maternity cover tony blair institute for global change",
        "companyName": "tony blair institute for global change"
    },
    {
        "position": "terms of reference for baseline study of the project girls initiative for resilient learning and support in malawi rwanda and zambia oxfam",
        "companyName": "oxfam"
    },
    {
        "position": "administrative assistant galloway co",
        "companyName": "galloway co"
    },
    {
        "position": "farm workshops manager precision recruitment international",
        "companyName": "precision recruitment international"
    },
    {
        "position": "training coordinator spark microgrants",
        "companyName": "spark microgrants"
    },
    {
        "position": "district coordinators nutrition international",
        "companyName": "nutrition international"
    },
    {
        "position": "research assistant unc project",
        "companyName": "unc project"
    },
    {
        "position": "consultancy to facilitate the development of a monitoring and evaluation framework for communications and public engagement department malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "operations manager savanna finacial services",
        "companyName": "savanna finacial services"
    },
    {
        "position": "assistant financial accountant public procurement and disposal of assets authority",
        "companyName": "public procurement and disposal of assets authority"
    },
    {
        "position": "finance officer unitrans malawi limited",
        "companyName": "unitrans malawi limited"
    },
    {
        "position": "pharmacist wholesale pharmaexpress",
        "companyName": "pharmaexpress"
    },
    {
        "position": "civil engineer amg global",
        "companyName": "amg global"
    },
    {
        "position": "operations manager administration marymount catholic secondary school",
        "companyName": "marymount catholic secondary school"
    },
    {
        "position": "administrative assistant umunthu plus",
        "companyName": "umunthu plus"
    },
    {
        "position": "administrative assistant umunthu plus",
        "companyName": "umunthu plus"
    },
    {
        "position": "loan officers united civil servants sacco",
        "companyName": "united civil servants sacco"
    },
    {
        "position": "loan officers united civil servants sacco",
        "companyName": "united civil servants sacco"
    },
    {
        "position": "loan officers united civil servants sacco",
        "companyName": "united civil servants sacco"
    },
    {
        "position": "resource mobilization officer umunthu plus",
        "companyName": "umunthu plus"
    },
    {
        "position": "pharmacy assistantnurse august medicine store",
        "companyName": "august medicine store"
    },
    {
        "position": "lodge manager boutique lodge",
        "companyName": "boutique lodge"
    },
    {
        "position": "production manager choice products limited",
        "companyName": "choice products limited"
    },
    {
        "position": "driver x2 mhc-henan guoji development co ltd",
        "companyName": "mhc-henan guoji development co ltd"
    },
    {
        "position": "administrativeaccounts assistant pvt health clinic",
        "companyName": "pvt health clinic"
    },
    {
        "position": "pre-school teacher when the saints malawi",
        "companyName": "when the saints malawi"
    },
    {
        "position": "ward attendant pvt health clinic",
        "companyName": "pvt health clinic"
    },
    {
        "position": "receptionistsecretary pvt health clinic",
        "companyName": "pvt health clinic"
    },
    {
        "position": "machine operator plasticycle ltd",
        "companyName": "plasticycle ltd"
    },
    {
        "position": "junior data entry clerk ori meat products",
        "companyName": "ori meat products"
    },
    {
        "position": "waiter the road trip",
        "companyName": "the road trip"
    },
    {
        "position": "swimming pool attendant the road trip",
        "companyName": "the road trip"
    },
    {
        "position": "chef the road trip",
        "companyName": "the road trip"
    },
    {
        "position": "bartender the road trip",
        "companyName": "the road trip"
    },
    {
        "position": "security officer credit data crb limited",
        "companyName": "credit data crb limited"
    },
    {
        "position": "uiux developer mindful metrics",
        "companyName": "mindful metrics"
    },
    {
        "position": "maintenance supervisor blantyre sports club",
        "companyName": "blantyre sports club"
    },
    {
        "position": "food beverage manager blantyre sports club",
        "companyName": "blantyre sports club"
    },
    {
        "position": "senior program manager health systems strengthening clinton health access initiative",
        "companyName": "clinton health access initiative"
    },
    {
        "position": "driver office of the ombudsman",
        "companyName": "office of the ombudsman"
    },
    {
        "position": "data collectors enumerators catholic relief services",
        "companyName": "catholic relief services"
    },
    {
        "position": "multiple positions portland cement malawi limited portland cement malawi limited",
        "companyName": "portland cement malawi limited"
    },
    {
        "position": "technical advisor social protection giz",
        "companyName": "giz"
    },
    {
        "position": "technical advisor for endev giz",
        "companyName": "giz"
    },
    {
        "position": "procrument supervisor plasticycle ltd",
        "companyName": "plasticycle ltd"
    },
    {
        "position": "head of strategy data digital old mutual",
        "companyName": "old mutual"
    },
    {
        "position": "marketing and sales intern kuwala travel and tours ltd",
        "companyName": "kuwala travel and tours ltd"
    },
    {
        "position": "finance officer spark microgrants",
        "companyName": "spark microgrants"
    },
    {
        "position": "temporary software developer elizabeth glaser pediatric aids foundation",
        "companyName": "elizabeth glaser pediatric aids foundation"
    },
    {
        "position": "loan officer lolc finance limited",
        "companyName": "lolc finance limited"
    },
    {
        "position": "research fellow university of malawi",
        "companyName": "university of malawi"
    },
    {
        "position": "electronics informatics intern university of malawi",
        "companyName": "university of malawi"
    },
    {
        "position": "laboratory technician um 10 university of malawi",
        "companyName": "university of malawi"
    },
    {
        "position": "call for applications for internship positions re-advertised university of malawi",
        "companyName": "university of malawi"
    },
    {
        "position": "human resources manager readymix concrete company",
        "companyName": "readymix concrete company"
    },
    {
        "position": "intern administrative assistant synergy capital partners",
        "companyName": "synergy capital partners"
    },
    {
        "position": "chief executive officer teachers council of malawi tcm",
        "companyName": "teachers council of malawi tcm"
    },
    {
        "position": "director of compliance services teachers council of malawi tcm",
        "companyName": "teachers council of malawi tcm"
    },
    {
        "position": "coordinator for basic education church of central africa presbyterian ccap",
        "companyName": "church of central africa presbyterian ccap"
    },
    {
        "position": "production manager choice products limited",
        "companyName": "choice products limited"
    },
    {
        "position": "office assistantmessenger agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret"
    },
    {
        "position": "motor vehicle driver agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret"
    },
    {
        "position": "financial accountant agricultural research and extension trust aret",
        "companyName": "agricultural research and extension trust aret"
    },
    {
        "position": "general manager property old mutual",
        "companyName": "old mutual"
    },
    {
        "position": "courier manager agma holdings limited",
        "companyName": "agma holdings limited"
    },
    {
        "position": "finance officer agma holdings limited",
        "companyName": "agma holdings limited"
    },
    {
        "position": "marketing sales officer ccap nkhoma synod",
        "companyName": "ccap nkhoma synod"
    },
    {
        "position": "operations officer ccap nkhoma synod",
        "companyName": "ccap nkhoma synod"
    },
    {
        "position": "junior accountant central poultry 2000 ltd",
        "companyName": "central poultry 2000 ltd"
    },
    {
        "position": "leaf processing supervisor jti japan tobacco international",
        "companyName": "jti japan tobacco international"
    },
    {
        "position": "malware analyst officer malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "legal enforcement manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "security and safety manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "information communication technology ict manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "management accountant malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "economics regulation manager malawi communications regulatory authority macra",
        "companyName": "malawi communications regulatory authority macra"
    },
    {
        "position": "intern compliance officer edukans",
        "companyName": "edukans"
    },
    {
        "position": "strategic process support volunteer edukans",
        "companyName": "edukans"
    },
    {
        "position": "driveroffice assistant edukans",
        "companyName": "edukans"
    },
    {
        "position": "driver winrock international",
        "companyName": "winrock international"
    },
    {
        "position": "call for pre-phd internship applications stremm project malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "call for pre-phd internship applications impact-malawi project malawi liverpool wellcome trust",
        "companyName": "malawi liverpool wellcome trust"
    },
    {
        "position": "information technology manager centenary bank",
        "companyName": "centenary bank"
    },
    {
        "position": "network support officer centenary bank",
        "companyName": "centenary bank"
    },
    {
        "position": "driver linde hotel",
        "companyName": "linde hotel"
    },
    {
        "position": "administrative assistant maya private school",
        "companyName": "maya private school"
    },
    {
        "position": "junior accountant plasticycle ltd",
        "companyName": "plasticycle ltd"
    },
    {
        "position": "program manager disabled women in africa - diwa",
        "companyName": "disabled women in africa - diwa"
    },
    {
        "position": "engineering shift controller mechanical alliance one tobacco malawi limited",
        "companyName": "alliance one tobacco malawi limited"
    },
    {
        "position": "green leaf services superintendent alliance one tobacco malawi limited",
        "companyName": "alliance one tobacco malawi limited"
    },
    {
        "position": "field officer x2 fincoop savings and credit cooperative limited",
        "companyName": "fincoop savings and credit cooperative limited"
    },
    {
        "position": "accountant angsoma development commission",
        "companyName": "angsoma development commission"
    },
    {
        "position": "monitoring evaluation and learning mel officer angsoma development commission",
        "companyName": "angsoma development commission"
    },
    {
        "position": "principal maone technical college",
        "companyName": "maone technical college"
    },
    {
        "position": "assistant nursery and primary education timotheos foundation",
        "companyName": "timotheos foundation"
    },
    {
        "position": "human resources manager timotheos foundation",
        "companyName": "timotheos foundation"
    },
    {
        "position": "school feeding officers marys meals malawi",
        "companyName": "marys meals malawi"
    },
    {
        "position": "head driver 2 positions castel malawi limited",
        "companyName": "castel malawi limited"
    },
    {
        "position": "agent-purchasing protea hotels",
        "companyName": "protea hotels"
    },
    {
        "position": "technical commercialization director path",
        "companyName": "path"
    },
    {
        "position": "head of operations care malawi",
        "companyName": "care malawi"
    },
    {
        "position": "chef waitress moments garden lodge",
        "companyName": "moments garden lodge"
    },
    {
        "position": "business specialist undp",
        "companyName": "undp"
    },
    {
        "position": "odel centre coordinator luanar",
        "companyName": "luanar"
    },
    {
        "position": "driver luanar",
        "companyName": "luanar"
    },
    {
        "position": "quality assurance officer luanar",
        "companyName": "luanar"
    },
    {
        "position": "presenter x2 nyanthepa community radio",
        "companyName": "nyanthepa community radio"
    },
    {
        "position": "receptionist nyanthepa community radio",
        "companyName": "nyanthepa community radio"
    },
    {
        "position": "reporterx2 nyanthepa community radio",
        "companyName": "nyanthepa community radio"
    },
    {
        "position": "guard x2 nyanthepa community radio",
        "companyName": "nyanthepa community radio"
    },
    {
        "position": "chief editor nyanthepa community radio",
        "companyName": "nyanthepa community radio"
    },
    {
        "position": "tally clerk etg agri inputs malawi",
        "companyName": "etg agri inputs malawi"
    },
    {
        "position": "academic positions university of blantyre synod",
        "companyName": "university of blantyre synod"
    },
    {
        "position": "systems transformation specialist agri-impact malawi",
        "companyName": "agri-impact malawi"
    },
    {
        "position": "learning and capacity development specialist agri-impact malawi",
        "companyName": "agri-impact malawi"
    },
    {
        "position": "short-term organisation development specialist x5 agri-impact malawi",
        "companyName": "agri-impact malawi"
    },
    {
        "position": "team leader agri-impact malawi",
        "companyName": "agri-impact malawi"
    },
    {
        "position": "finance and awards coordinator-gfc project save the children",
        "companyName": "save the children"
    },
    {
        "position": "human resources officer crossroads hotel",
        "companyName": "crossroads hotel"
    },
    {
        "position": "senior quality assurance officer malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "senior internal auditor malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "head of research malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "assistant librarian malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "assistant registrar academic malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "assistant registrar hr admin malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "ict technicians malawi college of accountancy",
        "companyName": "malawi college of accountancy"
    },
    {
        "position": "security officer mm operations limited",
        "companyName": "mm operations limited"
    },
    {
        "position": "senior safeguarding officer camfed - campaign for female education",
        "companyName": "camfed - campaign for female education"
    },
    {
        "position": "procurement clerk limbe leaf tobacco company limited",
        "companyName": "limbe leaf tobacco company limited"
    },
    {
        "position": "stores buyer limbe leaf tobacco company limited",
        "companyName": "limbe leaf tobacco company limited"
    },
    {
        "position": "imports officer limbe leaf tobacco co ltd",
        "companyName": "limbe leaf tobacco co ltd"
    },
    {
        "position": "head driver 2 positions castel malawi limited",
        "companyName": "castel malawi limited"
    },
    {
        "position": "business development manager first capital bank",
        "companyName": "first capital bank"
    },
    {
        "position": "multiple positions raiply malawi limited raiply malawi limited",
        "companyName": "raiply malawi limited"
    },
    {
        "position": "academic positions readvertised kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "associate director regional social marketing msi reproductive choices",
        "companyName": "msi reproductive choices"
    },
    {
        "position": "regional sales and trade marketing manager msi reproductive choices",
        "companyName": "msi reproductive choices"
    },
    {
        "position": "regional product launch manager msi reproductive choices",
        "companyName": "msi reproductive choices"
    },
    {
        "position": "procurement officer mpatamanga hydro power limited",
        "companyName": "mpatamanga hydro power limited"
    },
    {
        "position": "director of compliance services non-governmental organizations regulatory authority ngora",
        "companyName": "non-governmental organizations regulatory authority ngora"
    },
    {
        "position": "director of corporate services non-governmental organizations regulatory authority ngora",
        "companyName": "non-governmental organizations regulatory authority ngora"
    },
    {
        "position": "chief enviromental officer nkhotakota district council",
        "companyName": "nkhotakota district council"
    },
    {
        "position": "principal environmental health officer nkhotakota district council",
        "companyName": "nkhotakota district council"
    },
    {
        "position": "senior medical officer nkhotakota district council",
        "companyName": "nkhotakota district council"
    },
    {
        "position": "sanitation officer nkhotakota district council",
        "companyName": "nkhotakota district council"
    },
    {
        "position": "business training officer smedi",
        "companyName": "smedi"
    },
    {
        "position": "business information and advisory services officer smedi",
        "companyName": "smedi"
    },
    {
        "position": "assistant accountant 2 positions smedi",
        "companyName": "smedi"
    },
    {
        "position": "driver smedi",
        "companyName": "smedi"
    },
    {
        "position": "production assistant non-established smedi",
        "companyName": "smedi"
    },
    {
        "position": "office assistant smedi",
        "companyName": "smedi"
    },
    {
        "position": "communications and advocacy officer resident coordinator system",
        "companyName": "resident coordinator system"
    },
    {
        "position": "chef chatonda lodge",
        "companyName": "chatonda lodge"
    },
    {
        "position": "tours consultant the travel centre",
        "companyName": "the travel centre"
    },
    {
        "position": "drivermessenger wella medical aid society ltd",
        "companyName": "wella medical aid society ltd"
    },
    {
        "position": "head of operations care",
        "companyName": "care"
    },
    {
        "position": "human resource supervisor electricity supply corporation of malawi escom limited",
        "companyName": "electricity supply corporation of malawi escom limited"
    },
    {
        "position": "salesman namadzi bottlers",
        "companyName": "namadzi bottlers"
    },
    {
        "position": "chief operating officer lowama malawi",
        "companyName": "lowama malawi"
    },
    {
        "position": "waitress intern lodge host kalibu-lek",
        "companyName": "kalibu-lek"
    },
    {
        "position": "chef ndau lodge",
        "companyName": "ndau lodge"
    },
    {
        "position": "associate lecturers skyway university su",
        "companyName": "skyway university su"
    },
    {
        "position": "britam edge graduate trainee program britam",
        "companyName": "britam"
    },
    {
        "position": "sales and operations director sparc systems ltd",
        "companyName": "sparc systems ltd"
    },
    {
        "position": "head teacher fairview private secondary school",
        "companyName": "fairview private secondary school"
    },
    {
        "position": "enumerators national statistical office",
        "companyName": "national statistical office"
    },
    {
        "position": "driver center for international forestry research cifor",
        "companyName": "center for international forestry research cifor"
    },
    {
        "position": "implementation specialist revenue development foundation",
        "companyName": "revenue development foundation"
    },
    {
        "position": "trade marketing representative bat",
        "companyName": "bat"
    },
    {
        "position": "agricultural and value chain specialist undp",
        "companyName": "undp"
    },
    {
        "position": "full stack developer ruby on rails vitalite malawi",
        "companyName": "vitalite malawi"
    },
    {
        "position": "counter sales clerk agricultural trading company limited atc",
        "companyName": "agricultural trading company limited atc"
    },
    {
        "position": "concrete operations executive ready mix concrete company",
        "companyName": "ready mix concrete company"
    },
    {
        "position": "digital marketing content creator ready mix concrete company",
        "companyName": "ready mix concrete company"
    },
    {
        "position": "concrete pump operator jobsinlilongwegmailcom",
        "companyName": "jobsinlilongwegmailcom"
    },
    {
        "position": "heavy vehicle mechanic trucks machinery ready mix concrete company",
        "companyName": "ready mix concrete company"
    },
    {
        "position": "driver construction company",
        "companyName": "construction company"
    },
    {
        "position": "stores clerk construction company",
        "companyName": "construction company"
    },
    {
        "position": "hse and ims coordinator bayer",
        "companyName": "bayer"
    },
    {
        "position": "assistant registrar ict catholic university of malawi",
        "companyName": "catholic university of malawi"
    },
    {
        "position": "academic positions catholic university of malawi catholic university of malawi",
        "companyName": "catholic university of malawi"
    },
    {
        "position": "east and southern africa regional director idinsight",
        "companyName": "idinsight"
    },
    {
        "position": "procurement and supply chain management director tnm telekom networks malawi",
        "companyName": "tnm telekom networks malawi"
    },
    {
        "position": "macadamia post-harvest systems expert adam smith international",
        "companyName": "adam smith international"
    },
    {
        "position": "medical coordinator mdecins sans frontires",
        "companyName": "mdecins sans frontires"
    },
    {
        "position": "office and administration assistant mwaiwathu private hospital limited",
        "companyName": "mwaiwathu private hospital limited"
    },
    {
        "position": "chief executive officer readers investments limited",
        "companyName": "readers investments limited"
    },
    {
        "position": "photocopier technician gestetner limited",
        "companyName": "gestetner limited"
    },
    {
        "position": "project finance and administrative officer ministry of natural resources and climate change",
        "companyName": "ministry of natural resources and climate change"
    },
    {
        "position": "finance management assistant ministry of energy",
        "companyName": "ministry of energy"
    },
    {
        "position": "finance management specialist ministry of energy",
        "companyName": "ministry of energy"
    },
    {
        "position": "geographic information system gis specialist ministry of energy",
        "companyName": "ministry of energy"
    },
    {
        "position": "product officer systems spark microgrants",
        "companyName": "spark microgrants"
    },
    {
        "position": "office assistant united general insurance",
        "companyName": "united general insurance"
    },
    {
        "position": "operations manager beyond water malawi",
        "companyName": "beyond water malawi"
    },
    {
        "position": "resource mobilization officer centre for human rights and rehabilitation",
        "companyName": "centre for human rights and rehabilitation"
    },
    {
        "position": "finance officer centre for human rights and rehabilitation",
        "companyName": "centre for human rights and rehabilitation"
    },
    {
        "position": "deputy headteacher academic kamuzu academy",
        "companyName": "kamuzu academy"
    },
    {
        "position": "director mehboob memorial centre malawi a",
        "companyName": "mehboob memorial centre malawi a"
    },
    {
        "position": "team leader forex bureau nbs bank",
        "companyName": "nbs bank"
    },
    {
        "position": "sales analyst nbs bank",
        "companyName": "nbs bank"
    },
    {
        "position": "graphic and poster design united nations volunteers",
        "companyName": "united nations volunteers"
    },
    {
        "position": "mill manager premier food industries mw",
        "companyName": "premier food industries mw"
    },
    {
        "position": "grown units internal audit lead one acre fund",
        "companyName": "one acre fund"
    },
    {
        "position": "financial controller world bicycle relief",
        "companyName": "world bicycle relief"
    },
    {
        "position": "etp supervisor plasticycle ltd",
        "companyName": "plasticycle ltd"
    },
    {
        "position": "pastry chefs max sherry dine and lounge",
        "companyName": "max sherry dine and lounge"
    },
    {
        "position": "monitoring and evaluation me assistant kamuzu university of health sciences",
        "companyName": "kamuzu university of health sciences"
    },
    {
        "position": "manager private banking blantyre suite standard bank plc",
        "companyName": "standard bank plc"
    },
    {
        "position": "construction officer good people international",
        "companyName": "good people international"
    },
    {
        "position": "child sponsorship program assistant good people international",
        "companyName": "good people international"
    },
    {
        "position": "lead revenue planning research geomarketing airtel",
        "companyName": "airtel"
    },
    {
        "position": "self service executive save the children",
        "companyName": "save the children"
    },
    {
        "position": "customer experience analyst airtel",
        "companyName": "airtel"
    },
    {
        "position": "customer relationship executive airtel",
        "companyName": "airtel"
    },
    {
        "position": "mpbn ps core operations engineer airtel",
        "companyName": "airtel"
    },
    {
        "position": "front office supervisor crossroads hotels blantyre",
        "companyName": "crossroads hotels blantyre"
    },
    {
        "position": "network engineer limbe leaf tobacco company limited",
        "companyName": "limbe leaf tobacco company limited"
    },
    {
        "position": "workshop mechanic ulemu bus services",
        "companyName": "ulemu bus services"
    },
    {
        "position": "data entry clerks malawi national examinations board",
        "companyName": "malawi national examinations board"
    },
    {
        "position": "admissions counselor astria learning limited unima e-campus",
        "companyName": "astria learning limited unima e-campus"
    },
    {
        "position": "maintenance officer casino marina",
        "companyName": "casino marina"
    },
    {
        "position": "chef casino marina",
        "companyName": "casino marina"
    },
    {
        "position": "records officer exploits university",
        "companyName": "exploits university"
    },
    {
        "position": "receptionist exploits university",
        "companyName": "exploits university"
    },
    {
        "position": "senior quantity surveyor fidelis building contractors",
        "companyName": "fidelis building contractors"
    },
    {
        "position": "disease control surveillance assistants local government service commission",
        "companyName": "local government service commission"
    },
    {
        "position": "hospital attendants local government service commission",
        "companyName": "local government service commission"
    },
    {
        "position": "statistical clerks local government service commission",
        "companyName": "local government service commission"
    },
    {
        "position": "procurement operations officer african development bank",
        "companyName": "african development bank"
    },
    {
        "position": "poultry farm manager central poultry 2000 limited",
        "companyName": "central poultry 2000 limited"
    },
    {
        "position": "marketing manager mwos malawi",
        "companyName": "mwos malawi"
    },
    {
        "position": "project manager adam smith international",
        "companyName": "adam smith international"
    },
    {
        "position": "motor vehicle driver national registration bureau",
        "companyName": "national registration bureau"
    },
    {
        "position": "recruitment of health workers ministry of health",
        "companyName": "ministry of health"
    },
    {
        "position": "farm manager precision recruitment international",
        "companyName": "precision recruitment international"
    },
    {
        "position": "operations manager weafrica technologies",
        "companyName": "weafrica technologies"
    },
    {
        "position": "vehicle inspector weafrica technologies",
        "companyName": "weafrica technologies"
    },
    {
        "position": "receptionist weafrica technologies",
        "companyName": "weafrica technologies"
    },
    {
        "position": "customer experience officer weafrica technologies",
        "companyName": "weafrica technologies"
    },
    {
        "position": "climate and resilience specialist southern africa plan international",
        "companyName": "plan international"
    },
    {
        "position": "producerspresenters radio one 3 positions malawi broadcasting corporation mbc",
        "companyName": "malawi broadcasting corporation mbc"
    },
    {
        "position": "producerspresenters radio two fm 3 positions malawi broadcasting corporation mbc",
        "companyName": "malawi broadcasting corporation mbc"
    },
    {
        "position": "chief producer light entertainment and drama development broadcasting unit malawi broadcasting corporation mbc",
        "companyName": "malawi broadcasting corporation mbc"
    },
    {
        "position": "producers presenters 2onthego 5 positions malawi broadcasting corporation mbc",
        "companyName": "malawi broadcasting corporation mbc"
    },
    {
        "position": "principal producers presenters for television 2 positions malawi broadcasting corporation mbc",
        "companyName": "malawi broadcasting corporation mbc"
    },
    {
        "position": "monitoring evaluation accountability and learning meal manager -gcf project save the children",
        "companyName": "save the children"
    },
    {
        "position": "gender equity and social inclusion specialist gesi-gcf project save the children",
        "companyName": "save the children"
    },
    {
        "position": "programme coordinator -teacher professional development save the children",
        "companyName": "save the children"
    },
    {
        "position": "district coordinator 6 positions save the children",
        "companyName": "save the children"
    },
    {
        "position": "multiple positions solid construction and civil engineering ltd solid construction and civil engineering ltd",
        "companyName": "solid construction and civil engineering ltd"
    },
    {
        "position": "draftsmandraughtsman shayona cement",
        "companyName": "shayona cement"
    },
    {
        "position": "community development facilitator x10 malawi red cross society",
        "companyName": "malawi red cross society"
    },
    {
        "position": "drivers malawi red cross society",
        "companyName": "malawi red cross society"
    },
    {
        "position": "security guards malawi red cross society",
        "companyName": "malawi red cross society"
    },
    {
        "position": "office assistant malawi red cross society",
        "companyName": "malawi red cross society"
    },
    {
        "position": "gender and protection officer malawi red cross society",
        "companyName": "malawi red cross society"
    },
    {
        "position": "quality assurance officer autolube garage",
        "companyName": "autolube garage"
    },
    {
        "position": "administrationfront desk officers x2 autolube garage",
        "companyName": "autolube garage"
    },
    {
        "position": "mechanic autolube garage",
        "companyName": "autolube garage"
    },
    {
        "position": "chief administrative officer chiradzulu district council",
        "companyName": "chiradzulu district council"
    },
    {
        "position": "chief nursing officer chiradzulu district council",
        "companyName": "chiradzulu district council"
    },
    {
        "position": "principal land resource conservation officer chiradzulu district council",
        "companyName": "chiradzulu district council"
    },
    {
        "position": "principal environmental health officer chiradzulu district council",
        "companyName": "chiradzulu district council"
    },
    {
        "position": "projects accountant roads fund administration",
        "companyName": "roads fund administration"
    },
    {
        "position": "director of agriculture chiradzulu district council",
        "companyName": "chiradzulu district council"
    },
    {
        "position": "reservations clerk sunbird lilongwe",
        "companyName": "sunbird lilongwe"
    },
    {
        "position": "plumber sunbird lilongwe",
        "companyName": "sunbird lilongwe"
    },
    {
        "position": "electrician sunbird lilongwe",
        "companyName": "sunbird lilongwe"
    },
    {
        "position": "accounting technician unc project malawi",
        "companyName": "unc project malawi"
    },
    {
        "position": "territory sales officer malawi police sacco",
        "companyName": "malawi police sacco"
    },
    {
        "position": "social and behaviour change sbc specialist msi reproductive choices",
        "companyName": "msi reproductive choices"
    },
    {
        "position": "podcast producer paid intern podcast malawi",
        "companyName": "podcast malawi"
    },
    {
        "position": "air conditioner refrigeration technician cooling systems",
        "companyName": "cooling systems"
    },
    {
        "position": "student success coordinator astria learning limited unima e-campus",
        "companyName": "astria learning limited unima e-campus"
    },
    {
        "position": "research assistant malawi university of business and applied sciences mubas",
        "companyName": "malawi university of business and applied sciences mubas"
    },
    {
        "position": "communication and civic education officer pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "principal systems analyst pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "monitoring and enforcement officers 3 positions pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "internal auditor pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "driver pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "registrar pesticides control board pcb",
        "companyName": "pesticides control board pcb"
    },
    {
        "position": "technical implementation support officer x2 imagine worldwide",
        "companyName": "imagine worldwide"
    },
    {
        "position": "education technology coordinator edtec imagine worldwide",
        "companyName": "imagine worldwide"
    },
    {
        "position": "sales administrator nico life insurance company limited",
        "companyName": "nico life insurance company limited"
    },
    {
        "position": "risk analyst nico life insurance company limited",
        "companyName": "nico life insurance company limited"
    },
    {
        "position": "monitoring and evaluation me assistant kamuzu university of health sciences kuhes",
        "companyName": "kamuzu university of health sciences kuhes"
    },
    {
        "position": "industrial development specialist export development fund edf",
        "companyName": "export development fund edf"
    },
    {
        "position": "internal audit officer export development fund edf",
        "companyName": "export development fund edf"
    },
    {
        "position": "credit underwriter first capital bank",
        "companyName": "first capital bank"
    },
    {
        "position": "it projects lead sparc systems limited",
        "companyName": "sparc systems limited"
    },
    {
        "position": "chief executive officer malawi accountants board",
        "companyName": "malawi accountants board"
    },
    {
        "position": "disaster resilience engineer national local government finance committee nlgfc",
        "companyName": "national local government finance committee nlgfc"
    },
    {
        "position": "district engineer x28 national local government finance committee nlgfc",
        "companyName": "national local government finance committee nlgfc"
    },
    {
        "position": "primary school teaching assistant physical education hillview international school",
        "companyName": "hillview international school"
    },
    {
        "position": "finance manager ngo regulatory authority ngora",
        "companyName": "ngo regulatory authority ngora"
    },
    {
        "position": "pr and stakeholder engagement officer ngo regulatory authority ngora",
        "companyName": "ngo regulatory authority ngora"
    },
    {
        "position": "assistant accountant ngo regulatory authority ngora",
        "companyName": "ngo regulatory authority ngora"
    },
    {
        "position": "administrative assistant ngo regulatory authority ngora",
        "companyName": "ngo regulatory authority ngora"
    },
    {
        "position": "driver x3 ngo regulatory authority ngora",
        "companyName": "ngo regulatory authority ngora"
    },
    {
        "position": "claims manager nyasa insurance limited",
        "companyName": "nyasa insurance limited"
    },
    {
        "position": "underwriting manager nyasa insurance limited",
        "companyName": "nyasa insurance limited"
    },
    {
        "position": "chief operating officer nyasa insurance limited",
        "companyName": "nyasa insurance limited"
    },
    {
        "position": "chief finance officer nyasa insurance limited",
        "companyName": "nyasa insurance limited"
    },
    {
        "position": "graphic designer for the 2024 un annual country results report for malawi united nations secretariat un",
        "companyName": "united nations secretariat un"
    },
    {
        "position": "coco site manager puma energy",
        "companyName": "puma energy"
    },
    {
        "position": "poultry export sales specialistmanager africa markets central poultry 2000 limited",
        "companyName": "central poultry 2000 limited"
    },
    {
        "position": "corporate finance analyst non-mgmt bat",
        "companyName": "bat"
    }
]


def split_into_chunks(data, chunk_size=25):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


# Create output directory if needed
output_dir = "chunks"
os.makedirs(output_dir, exist_ok=True)

# Split and write to separate files
for idx, chunk in enumerate(split_into_chunks(data, 25), start=1):
    filename = os.path.join(output_dir, f"chunk_{idx}.json")
    with open(filename, "w") as f:
        json.dump(chunk, f, indent=4)

print("Chunks created successfully.")
