#MAIN APPLICATION 
#Calls functions

if __name__=="__main__":
    print("Welcome to the App!")

from md_formulas import *

def main():
    list()
    tag=input("Enter keyword: ").lower()

    if tag == "axis":
        qrs_axis()
    elif tag == "bmi":
        bmi_calculator()
    elif tag == "gfr":
        gfr_calculator()
    elif tag == "k":
        k_correction()
    elif tag == "map".lower():
        map_calculator()
    elif tag == "qtc":
        corrected_qt()
    
    new_input=input("Continue? [Y/N]: ").lower()
    if new_input=="y":
        print("\n")
        main()  
    else:
        print("Thank you.")
        exit()

main()
