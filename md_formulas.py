#FORMULAS IN MEDICINE
def list():
    list=("bmi,")
    print("Tags:", list)

def new_file():
    name=input("Name: ")
    age=input("Age: ")
    sex=input("Sex: ")
    room=input("Room: ")

def new_input():
    new_input=input("Continue? [Y/N]: ").lower()
    if new_input=="y":
        print("\n")
        list()

    else:
        print("Thank you.")
        exit()


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

