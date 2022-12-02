#MAIN APPLICATION 
#Calls functions

if __name__=="__main__":
    print("Welcome to the App!")

from md_formulas import *

def main():
    list()
    tag=input("Formula tag: ")

    if tag.lower() == "bmi":
        bmi_calculator()
    elif tag.lower() == "gfr":
        gfr_calculator()
    elif tag.lower() == "k":
        k_correction()
    
    new_input=input("Continue? [Y/N]: ").lower()
    if new_input=="y":
        print("\n")
        main()  
    else:
        print("Thank you.")
        exit()

main()