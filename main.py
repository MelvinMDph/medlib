#MAIN APPLICATION 
#Calls functions

if __name__=="__main__":
    print("Welcome to the app!")

from md_formulas import *
from md_algorithms import *

def main():
    tag=input("Tag: ").lower()

    if tag == "list":
        list()
    elif tag == "ascites":
        ascites()
    elif tag == "axis":
        qrs_axis()
    elif tag == "bmi":
        bmi_calculator()
    elif tag == "dobu":
        dobutamine()
    elif tag == "dopa":
        dopamine()
    elif tag == "effusion":
        effusion()
    elif tag == "fio2":
        fio2()
    elif tag == "gfr":
        gfr_calculator()
    elif tag == "hemorrhoid":
        hemorrhoid()
    elif tag == "ihd":
        ihd_management()
    elif tag == "k":
        k_correction()
    elif tag == "map":
        map_calculator()
    elif tag == "murmur":
        murmur()
    elif tag == "na":
        na_correction()
    elif tag == "ne":
        norepinephrine()
    elif tag == "note":
        note()
    elif tag == "nyha":
        nyha()
    elif tag == "prenatal":
        prenatal()
    elif tag == "qtc":
        corrected_qt()
    elif tag == "water":
        water_deficit()
    
    new_input=input("Continue? [Y/N]: ").lower()
    if new_input=="y":
        print("\n")
        main()  
    else:
        print("Thank you.")
        exit()

main()