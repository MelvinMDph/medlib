#FORMULAS IN MEDICINE
#Defines functions

def list():
    list=["AXIS", "BMI", "DOPA", "DOBU", "FiO2", "NA", "NE", "GFR", "K", "MAP", "QTc", "WATER"]
    print("Keys:", list)

def new_file():
    name=input("Name: ")
    age=input("Age: ")
    gender=input("Gender: [M/F] ").lower()
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
    gender=input("Gender: [M/F] ").lower()
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
        added_k_serum=float(round(kcl_iv*0.4, 2))
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
    
    check_wt=(input("Use patient weight? [y/n] ")).lower()
    if check_wt == "y":
        wt=float(input("Patient wt. (kg): "))
    else:
        wt=1
    
    desired_dose=float(input("Desired dose (mcg/kg/m) or (mcg/m): "))
    if desired_dose >=15:
        print("Are you sure? If systemic perfusion or SBP cannot be maintained at >90 mmHg with a dose of 15 mcg/min, it is unlikely that further increases in dose will be of benefit.")
    
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

def na_correction():
    print("calculates Na+ deficit...")
    na_current=float(input("Serum Na: "))
    na_desired=float(input("Desired Na: "))
    wt=float(input("Wt. (kg): "))
    deficit=(na_desired-na_current)*wt*0.6
    print("Na deficit =", round(deficit), "mEqs")
    infusion_time=(na_desired-na_current)/0.5
    print("Time needed to infuse =", round(infusion_time), "h")
    pnss_needed=deficit/154
    print("PNSS needed =", round(pnss_needed, 1), "L")
    drip_rate=(pnss_needed*1000)/infusion_time
    print("Drip rate =", round(drip_rate), "cc/h")
    print("\n IVF: PNSS 1L x", round(drip_rate), "cc/h for a total of", round(pnss_needed, 1), "L, re-check serum Na (e.g. q6h).")
    see=input("See note? [y/n] ").lower()
    if see == "y":
        print("Note: frequent Na+ monitoring needed (correction is unpredictable). Na+ should not be corrected >10nM within the first 24h in chronic hyponatremia due to increased risk of osmotic demyelination syndrome (central pontine myelinolysis).")

def water_deficit():
    print("calculates water deficit in hypernatremia...")
    gender=input("Gender: [M/F] ").lower()
    na=float(input("Serum Na: "))
    wt=float(input("Wt. (kg): "))
    insensible=float(input("Insensible water loss (ml/kg/d): "))
    tbw=0.5
    if gender == "m":
        tbw = 0.6
    
    difference=na-140
    deficit=(difference/140)*wt*tbw
    print("Water deficit =", round(deficit, 1), "L")
    insensible_loss=(insensible*wt)/1000
    print("Insensible losses =", round(insensible_loss, 1), "L")
    ml=deficit*1000
    po_rate=ml/12
    iv_rate=ml/48
    print("Option 1: Give", round(po_rate), "ml free-water flushes q4h in between feedings.")
    print("Option 2: IVF D5W (or 0.3 NaCl) 1 L x", round(iv_rate), "cc/h")
    print("Re-check serum Na (e.g. q6h).")
    see=input("See note? [y/n] ").lower()
    if see == "y":
        print("Note: free water should be administered PO/NGT unless contraindicated (D5W alternative or 0.3 NaCl). Correct water deficit over 48-72 h with daily incorporation of insensible losses and ongoing water losses.")
        print("Normal intake: 2500 ml/d (35 mg/kg/d in afebrile 70 kg) Liquids: 1500 ml. Foods: 700 ml. Metabolic (endogenous): 300 ml.")
        print("Normal output: 1400-2300 ml/d. Insensible loss: 600-900 ml (lungs (decreased during MV due to free water gain during humidified ventilation) and skin) + 2.5 ml/kg/d each degree > normal. Urine: 800-1500 ml. Stool: 250 ml.")

def fio2():
    print("calculates Desired FiO2...")
    age=float(input("Age: "))
    current_FiO2=float(input("Current FiO2: "))
    current_PaO2=float(input("Current PaO2: "))

    if age <60:
        desired_PaO2=104-(0.43*age)
    elif age >=60:
        desired_PaO2=80-(age-60)
    
    desired_FiO2=(current_FiO2*desired_PaO2)/current_PaO2
    print("Desired FiO2 =", round(desired_FiO2))
    if desired_FiO2 >=60:
        print("Suggest: Face mask 7-8 LPM (FiO2 = 60%) or higher O2 flow system.")
    elif desired_FiO2 >=50 <60:
        print("Suggest: Face mask 6-7 LMP (FiO2 = 50%).")
    elif desired_FiO2 >=40 <50:
        print("Suggest: Nasal cannula 5 or 6 LPM (FiO2 = 40 and 44%) or Face mask 5-6 LPM (FiO2 = 40%).")
    elif desired_FiO2 >=36 <40:
        print("Suggest: Nasal cannula 4 LPM (FiO2 = 36%).")
    elif desired_FiO2 >=32 <36:
        print("Suggest: Nasal cannula 3 LPM (FiO2 = 32%).")
    elif desired_FiO2 >=28 <32:
        print("Suggest: Nasal cannula 2 LPM (FiO2 = 28%).")
    elif desired_FiO2 >=24 <28:
        print("Suggest: Nasal cannula 1 LPM (FiO2 = 24%).")
    else:
        print("FiO2 at room air is 21%.")

    see=input("See note? [y/n] ")
    print("O2 flow system, O2 flow rate, Estimated FiO2:")
    print("Nasal cannula    1       24 %")
    print("Nasal cannula    2       28 %")
    print("Nasal cannula    3       32 %")
    print("Nasal cannula    4       36 %")
    print("Nasal cannula    5       40 %")
    print("Nasal cannula    6       44 %")
    print("Simple face mask 5-6     40 %")
    print("Simple face mask 6-7     50 %")
    print("Simple face mask 7-8     60 %")

