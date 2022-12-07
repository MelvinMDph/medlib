#FORMULAS IN MEDICINE
#Defines functions

def list():
    list=["AXIS", "BMI", "DOPA", "DOBU", "NE", "GFR", "K", "MAP", "QTc"]
    print("Keys:", list)


def new_file():
    name=input("Name: ")
    age=input("Age: ")
    gender=input("Gender [M/F]: ").lower()
    room=input("Room No.: ")


def bmi_calculator():
    print("calculates Body Mass Index (BMI)...")
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
    gender=input("Gender [M/F]: ").lower()
    age=float(input("Age: "))
    creatinine=float(input("Creatinine (mg/dL): "))
    K=float(0.7)
    if gender == "m":
        K=float(0.9)
    
    ScrK=float(creatinine/K)
    min=1
    max=1
    if ScrK <=1:
        min=ScrK
    elif ScrK >1:
        max=ScrK
    
    alpha=float(-0.241)
    if gender == "m":
        alpha=float(-0.302)
    
    constant=float(0.9938)
    negativeexponent=float(-1.200)
    mintoalpha=min**alpha
    maxtonegexponent=max**negativeexponent
    constanttoage=constant**age
    femalevariable=float(1.012)
    if gender == "m":
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

def k_correction():
    print("calculates K+ deficit...")
    k_current=float(input("Serum K: "))
    k_desired=float(input("Desired K: "))
    k_difference=k_desired-k_current
    constantvariable=k_difference/0.27
    deficit=constantvariable*100
    print("K Deficit =", round(deficit), "mEqs" "\n")
    kcl_tablets=deficit/10
    print("Suggestion:" "\n" "May need", round(kcl_tablets), "KCl tab. (10 mEqs/tab),")
    kcl_iv=deficit/40
    if k_current >2.5 <3.5:
        added_k_serum=float(round(round(kcl_iv)*0.4), 2)
        print("or", round(kcl_iv), "cycles of 40 mEq/L KCl correction." "\n")
        print(round(kcl_iv), "cycles of 40 mEqs KCl/L will add", added_k_serum, "mEqs K to serum (10 mEqs KCl IV increases serum K by ~0.1 mEq/L.")
    elif k_current <=2.5:
        print("or", round(kcl_iv), "cycles of 40 mEq/h KCl correction via central line." "\n")
        print("K <2.5 mEq/L or symptomatic: 40 mEq/h max infusion rate (central line), continuous ECG monitoring, and K monitoring. Patients may require up to 400 mEq/24h.")

    if kcl_iv >3 <6:
        print("Give half in 24h, monitof K, correct remaining in 1-2 days." "\n")
    elif kcl_iv >=6:
        print("Give <1/2 in 24h, monitor K, correct remaining in 1-2 days." "\n")

    print("K 2.5 - 3.5 mEq/L: 10 mEq/h max infusion rate; 40 mEq/L max concentration; not to exceed 200 mEq dose/24h." "\n")

def map_calculator():
    print("calculates Mean Arterial Pressure (MAP)...")
    sbp=float(input("Systolic BP: "))
    dbp=float(input("Diastolic BP: "))
    numerator=(2*dbp)+sbp
    map=numerator/3
    print("MAP =", round(map))

def corrected_qt():
    print("calculates corrected QT interval (QTc)...")
    QT_interval=float(input("QT interval (sm. boxes): "))
    QT_sec=QT_interval*0.04
    heart_rate=float(input("Heart rate (bpm): "))
    RR_interval=1500/heart_rate
    RR_sec=RR_interval*0.04
    sqroot_RR=RR_sec**0.5
    if heart_rate >100:
        print("Framingham formula. . .")
        oneminusRR=1-(round(RR_sec, 2))
        corrected_qt=QT_sec+(0.154*oneminusRR)
    else:
        print("Bazett's Formula. . .")
        corrected_qt=QT_sec/sqroot_RR

    print("Corrected QT =", round(corrected_qt, 2), "sec or ", 1000*(round(corrected_qt, 2)), "msec")
    if corrected_qt >0.45:
        print("QTc is prolonged.")
    elif corrected_qt <0.45:
        print("QTC is normal.")

    print("\n \n Normal: </= 440 to 450 msec.\n Upper limit: 460 msec in women or 450 msec in men.")

def qrs_axis():
    print("calculates QRS axis...")
    lead_I=float(input("lead I: " ))
    aVF=float(input("aVF: "))
    numerator=90*aVF
    denominator=abs(lead_I)+abs(aVF)
    axis=round(numerator/denominator)
    print("QRS axis =", axis)
    if axis >90 <180:
        print("Right Axis Deviation (RAD).")
    elif axis >=-30 <=90:
        print("Normal axis.")    
    elif axis >=-90 <-30: 
        print("Left Axis Deviation (LAD).")
    elif axis >-180 <-90:
        print ("Extreme Axis Deviation.")

def norepinephrine():
    print("calculates Norepinephrine drip...")
    mL=float(input("D5W vol (mL): "))
    mg=float(input("Norepinephrine (mg): "))
    concentration=(mg/mL)*1000
    
    check_wt=(input("Use patient weight? [Y/N]")).lower()
    if check_wt == "y":
        wt=float(input("Patient wt. (kg): "))
    else:
        wt=1
    
    desired_dose=float(input("Desired dose (mcg/kg/m) or (mcg/m): "))
    if desired_dose >=15:
        print("Are you sure? If systemic perfusion of SBP cannot be maintained at >90 mmHg with a dose of 15 mcg/min, it is unlikely that further increases in dose will be of benefit.")
    
    drip_rate=desired_dose*wt*60/concentration
    print("Drip rate =", drip_rate, "ml/hr (or cc/hr or ugtt/m)")
    print("Start norepinephrine drip:", mg, "mg NE +", mL, "cc D5W x", drip_rate, "cc/hr", "(dose:", desired_dose, "mcg/kg/m or mcg/m dose)")

def dopamine():
    print("calculates Dopamine drip...")
    mL=float(input("D5W vol (mL): "))
    mg=float(input("Dopamine (mg): "))
    concentration=(mg/mL)*1000
    wt=float(input("Patient wt. (kg): "))
    desired_dose=float(input("Desired dose (mcg/kg/m): "))
    drip_rate=desired_dose*wt*60/concentration
    print("Drip rate =", drip_rate, "ml/hr (or cc/hr or ugtt/m)")
    print("Start dopamine drip:", mg, "mg dopamine +", mL, "cc D5W x", drip_rate, "cc/hr", "(dose:", desired_dose, "mcg/kg/m)")

def dobutamine():
    print("calculates Dobutamine drip...")
    mL=float(input("D5W vol (mL): "))
    mg=float(input("Dobutamine (mg): "))
    concentration=(mg/mL)*1000
    wt=float(input("Patient wt. (kg): "))
    desired_dose=float(input("Desired dose (mcg/kg/m): "))
    drip_rate=desired_dose*wt*60/concentration
    print("Drip rate =", drip_rate, "ml/hr (or cc/hr or ugtt/m)")
    print("Start dobutamine drip:", mg, "mg dobutamine +", mL, "cc D5W x", drip_rate, "cc/hr", "(dose:", desired_dose, "mcg/kg/m)")

