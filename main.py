#Opens calculator
if __name__=="__main__":
    print("Welcome to the App!")

from md_formulas import *

def main():
    list()
    tag=input("Formula tag: ")

    if tag == "bmi":
        bmi_calculator()
    elif tag == "gfr":
        gfr_calculator()
    
    new_input=input("Continue? [Y/N]: ").lower()
    if new_input=="y":
        print("\n")
        main()  
    else:
        print("Thank you.")
        exit()

main()