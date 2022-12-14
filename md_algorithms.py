#ALGORITHMS IN MEDICINE
#Defines functions

#pip install tabulate
from tabulate import tabulate

def effusion():
    print("Diagnostic Algorithm of Pleural Effusion")
    print("Pleural effusion \n-> Perform diagnostic thoracentesis. \n-> Measure pleural fluid protein and LDH.")
    exudative=[["Any of following met?"], ["PF/serum protein >0.5 \nPF/serum LDH >0.6 \nPF LDH >2/3 upper normal serum limit"]]
    print(tabulate(exudative, headers="firstrow", tablefmt="fancy_grid"))
    any_met=input("Answer? [y/n]: ")
    if any_met == "n":
        print("Transudate: Treat CHF, cirrhosis, nephrosis")
    elif any_met == "y":
        print("Exudate: Further diagnostic procedures")
        measure=[["Measure PF glucose \nObtain PF cytology \nObtain differential cell count \nCulture, stain PF \nPF marker for TB"]]
        print(tabulate(measure, tablefmt="fancy_grid"))
        glucose=[["Glucose < 60 mg/dL"], ["Consider: \n Malignacy \n Bacterial infection \n Rheumatoid pleuritis"]]
        print(tabulate(glucose, headers="firstrow", tablefmt="fancy_grid"))
        print("If no diagnosis: ")
        options=[["Consider PE (spiral CT or lung scan)", "[Y] Treat for PE. [N] >>"],
                ["PF marker for TB", "[Y] Treat for TB. [N] >>"],
                ["Symptoms improving", "[Y] Observe. [N] >>"],
                ["Consider thoracoscopy or \nimage-guided pleural biopsy"]]
        print(tabulate(options, headers="firstrow", tablefmt="fancy_grid"))

def ascites():
    print("Algorithm for the diagnosis of ascites according to the serum albumin gradient (SAAG)")
    saag=float(input("SAAG g/dL: "))
    if saag >= 1.1:
        ascitic_protein=float(input("Ascitic protein g/dL: "))
        if ascitic_protein >=2.5:
            protein_greater=[["Ascitic protein >=2.5 g/dL \n Heart failure/constrictive pericarditis\n Early Budd-Chiari syndrome\n IVC obstruction\n Sinusoidal obstruction syndrome"]]
            print(tabulate(protein_greater, tablefmt="fancy_grid"))
        elif ascitic_protein <2.5:
            protein_lesser=[["Ascitic protein < 2.5 g/dL \n Cirrhosis \n Late Budd=Chiari syndrome \n Massive liver metastasis"]]
            print(tabulate(protein_lesser, tablefmt="fancy_grid"))
    elif saag <1.1:
        saag_lesser=[["SAAG <1.1 g/dL \n Biliary leak \n Nephrotic syndrome \n Pancreatitis \n Peritoneal carcinomatosis \n Tuberculosis"]]
        print(tabulate(saag_lesser, tablefmt="fancy_grid"))


def prenatal():
    print("Prenatal checkup reminders")
    answer=input("Checkup status (first, second, 20, 24, 28, 33, 37, 38, 39, 40, or 41): ").lower()
    if answer == "first":
        print("\n Labs: CBC, urinalysis, ABO typing. TVS/OB UTZ for unclear LMP or previous CS. \n Meds: \n Folic Acid 5 mg tab OD if <20 weeks. \n Vitamin B complex tab OD. \n MV+Fe tab OD if >20 weeks. \n Calcium 500 mg tab BID, TID if (+) HPN. \n Milk supplement 1 glass BID. ")
    elif answer == "second":
        print("\n Labs: PAP smear, FBS, HIV, VDRL. \n ")
    elif answer == "20":
        print("\n Imaging: OB UTZ (anatomy scan). \n Check Tetanus immunization status: If none or unrecalled: Start 1st dose today, 2nd dose after 4 weeks, and 3rd dose after 6 months)")
    elif answer == "24":
        print("\n Lab: 75 g OGTT.")
    elif answer == "28":
        print("\n Labs: HBsAg-MEIA, CBC (repeat hematocrit).")
    elif answer == "33":
        print("\n Labs: repeat urinalysis. \n Advise walking exercises and fetal kick counting (>10 in 2 h after eating). \n If low-lying placenta/placenta previa: repeat OB UTZ. ")
    elif answer == "37":
        print("\n Remind to seek admission if with signs of labor: \n Watery vaginal discharge \n Bloody vaginal discharge \n Uterine contraction every 5 minutes")
    elif answer == "38":
        print("\n IE and cervical stripping. \n DO NOT DO IE IF PLACENTA PREVIA. ")
    elif answer == "39":
        print("NST, IE and cervical stripping.")
    elif answer == "40":
        print("\n IE and cervical stripping. \n Biophysical profile.")
    elif answer == "41":
        print("\n IE and repeat biophysical profile if 1 week after the 1st.")
    else:
        print("Info: \n PNC follow-up schedule: \n 0 - 27 weeks: every 4 weeks \n 28 - 36 weeks: every 2 weeks \n 36 - 39 weeks: every week \n >=40 weeks: every 3 days")

def hemorrhoid():
    print("The Staging and Treatment of Hemorrhoids")
    table_data=[["Stage", "Description of Classification", "Treatment"],
                ["I", "Enlargement with bleeding", "Fiber supplementation \nShort course of cortisone suppository \nSclerotherapy \nInfrared coagulation"],
                ["II", "Protrusion with spontaneous \nreduction", "Fiber supplementation \nShort course of cortisone suppository \nSclerotherapy \nInfrared coagulation"],
                ["III", "Protrusion requireing manual \nreduction", "Fiber supplementation \nShort course of cortisone suppository \nRubber band ligation \nOperative hemorrhoidectomy"],
                ["IV", "Irreducible protrusion", "Fiber supplementation \nCortisone suppository \nOperative hemorrhoidectomy"]]
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

def murmur():
    print("Evaluation of Heart Murmur")
    answer=input("Presence of cardiac murmur? [sys/dias/cont]: ").lower()
    if answer == "sys":
        grade=int(input("What grade? [1-6]: "))
        if grade <=2:
            symptoms=input("Symptomatic? [y/n]: ").lower()
            if symptoms == "y":
                print("Do ECG and CXR.")
                result=input("Is ECG and CXR normal? [y/n]: ").lower()
                if result == "y":
                    print("No further workup.")
                elif result =="n": 
                    print("Do echocardiography. Cardiac consult if appropriate.")
            elif symptoms =="n":
                print("No further workup.")
        elif grade >=3:
            print("Grade III or >, holosystolic, or late systolic: Do echocardiography. Cardiac consult if appropriate.")
    else:
        print("Diastolic or Continuous murmur: Do Echocardiography. Cardiac consult if appropriate.")

def nyha():
    print("New York Heart Association Functional Classificaiton")
    table_data=[["Class 1 \n No limitaion of physical activity. \n No symptoms with ordinary exertion.", "Class 3 \n Marked limitation of physical activity. \n Less than ordinary activity causes symptoms. \n Asymptomatic at rest."],
                ["Class 2 \n Slight limitation of physical activity. \n Ordinary activity causes symptoms.", "Class 4 \n Inability to carry out any physical activity \n without discomfort. \n Symptoms at rest."] ]
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

def ihd_evaluation():
        print("Evaluation of the patient with known or suspected IHD")
        indications=[["Possible indications for stress testing:"], ["1. Dx of IHD uncertain \n2. Assess functional capacity of patient. \n3. Assess adequacy of treatment program for IHD. \n4. Markedly abnormal calcium score on EBCT."]]
        print(tabulate(indications, headers="firstrow", tablefmt="fancy_grid"))
        exercise=input("Can patient exercise adequately? [y/n]: ").lower()
        
        def imaging():
            print("An imaging study should be performed.")
            imaging_studies=[["2D-echocardiography", "ECHO"], 
            ["Nuclear perfusion scan", "MIBI, Methoxyisobutyl isonitrite"],
            ["Cardiac MR scan", "CMR"],
            ["Cardiac PET scan", "PET"]]
            print(tabulate(imaging_studies, headers="firstrow", tablefmt="fancy_grid"))

        if exercise == "n":
            imaging()
        elif exercise == "y":
            confounding=input(("Are confounding features present on resting ECG? [y/n]: ")).lower()
            if confounding == "n":
                print("Perform treadmill exercise with ECG monitoring.")
            elif confounding == "y":
                imaging()

def ihd_management():
        print("Management of Patient with Ischemic Heart Disease")
        initiate=[["Initiate medical therapy:"], ["1. Decrease demand ischemia \n2. Minimize IHD risk factors \n3. ASA (clopidogrel if ASA intolerant)"]]
        print(tabulate(initiate, headers="firstrow", tablefmt="fancy_grid"))
        risk_factors=[["Any high-risk features?"],["Low exercise or ischemia at low workload, \nlarge area of ischemic myocardium, \nEF <40%, ACS presentation"]]
        print(tabulate(risk_factors, headers="firstrow", tablefmt="fancy_grid"))
        any=input("Any high-risk features? [y/n]: ").lower()
        
        def coroangiogram():
                print("Refer for coronary arteriography")
                suitable=input("Anatomy suitable for revascularization? [y/n]: ").lower()
                if suitable == "y":
                    procedure=[["Single vessel disease", "PCI"], ["LM +/or multi vessel", "Assess: PCI vs CABG"]]
                    print(tabulate(procedure, headers="firstrow", tablefmt="fancy_grid"))
                    print("Continue medical therapy periodic stress assessment.")
                    see=input("See IHD evaluation algorithm? [y/n]: ").lower()
                    if see == "y":
                        ihd_evaluation()
                    else:
                        any
                elif suitable == "n":
                    print("Consider unconventional treatments.")
                    print("Continue medical therapy periodic stress assessment.")
                    see=input("See IHD evaluation algorithm? [y/n]: ").lower()
                    if see == "y":
                        ihd_evaluation()
                    else:
                        any
        
        if any == "y":
            coroangiogram()
        elif any == "n":
            exertional_symptoms=input("Are exertional symptoms controlled? [y/n]: ")
            if exertional_symptoms == "y":
                    print("Continue medical therapy periodic stress assessment.")
                    see=input("See IHD evaluation algorithm? [y/n]: ").lower()
                    if see == "y":
                        ihd_evaluation()
            if exertional_symptoms == "n":
                coroangiogram()


