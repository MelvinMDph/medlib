#FORMULAS IN MEDICINE
def list():
    list=["bmi", "gfr"]
    print("Tags:", list)


def new_file():
    name=input("Name: ")
    age=input("Age: ")
    gender=input("Gender [M/F]: ")
    room=input("Room No.: ")


def bmi_calculator():
    print("Body Mass Index Calculator")
    weight=float(input("Wt (kg): "))
    height=float(input("Ht (cm): "))
    ht_meter=height/100
    ht_sq=ht_meter*ht_meter
    bmi=weight/ht_sq
    print("BMI =", round (bmi, 2))
    if bmi <18.5:
        print("Underweight")
    elif bmi >=30:
        print("Obese 2")
    elif bmi >=25 <30:
        print("Obese 1")
    elif bmi >=23 <25:
        print("At risk")
    elif bmi >=18 <23: 
        print("Normal")


def gfr_calculator():
    print("CKD-EPI Creatinine Equation 2021")
    gender=input("Gender [M/F]: ")
    age=float(input("Age: "))
    creatinine=float(input("Creatinine (mg/dL): "))

    K=float(0.7)
    if gender == "m" or "M":
        K=float(0.9)
    
    ScrK=float(creatinine/K)
    if ScrK <=1:
        min=ScrK
        max=1
    else:
        min=1
        max=ScrK
    
    alpha=float(-0.241)
    if gender == "m" or "M":
        alpha=float(-0.302)
    
    constant=float(0.9938)
    negativeexponent=float(-1.200)

    mintoalpha=min**alpha
    maxtonegexponent=max**negativeexponent
    constanttoage=constant**age
    
    femalevariable=float(1.012)
    if gender == "m" or "M":
        femalevariable=1
    
    GFR=142*mintoalpha*maxtonegexponent*constanttoage*femalevariable
    print("eGFR =", round(GFR))
    
    if GFR <15:
        print("Stage 5, kidney failure")
    elif GFR >=90:
        print("Stage 1, normal or high")
    elif GFR >=60 <90:
        print("Stage 2, mildly decreased")
    elif GFR >=45 <60:
        print("Stage 3a, mildly to moderately decreased")
    elif GFR >=30 <45:
        print("Stage 3b, moderately to severely decreased")
    elif GFR >=15 <30:
        print("Stage 4, severely decreased")
