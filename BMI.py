
print("Choose your race group:")
race_group = int(input("Enter your choice, 1 for US/EU or 2 for Asian: "))

if race_group == 1:
    print("Input values: ")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    print("Choose measurement system:")
    m_system = int(input("Enter your choice, 1 for metric or 2 for imperial system: "))

    if m_system == 1:
            
        bmi = weight / (height**2)

        print("Your BMI:", bmi)
        if bmi < 16.0:
            print("Severely underweight")
        elif bmi < 18.5:
            print("Underweight")
        elif bmi < 25.0:
            print("Normal")
        elif bmi < 30.0:
            print("Overweight")
        elif bmi < 35.0:
            print("Obese")
        else:
                print("Extremely obese")

    elif m_system == 2:
        bmi = weight * 703 / (height**2)
        print("Your BMI:", bmi)

        if bmi < 16.0:
            print("Severely underweight")
        elif bmi < 18.5:
            print("Underweight")
        elif bmi < 25.0:
            print("Normal")
        elif bmi < 30.0:
            print("Overweight")
        elif bmi < 40.0:
            print("Obese")
        else:
            print("Extremely obese")

    else:
        print("Invalid choice, there are 1 and 2 options only")

elif race_group == 2:
    print("Input values: ")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    print("Choose measurement system:")
    m_system = int(input("Enter your choice, 1 for metric or 2 for imperial system: "))
    if m_system == 1:
        bmi = weight / (height**2)

        print("Your BMI:", bmi)

        if bmi < 18.5:
            print("Underweight")
        elif bmi < 23.0:
            print("Normal")
        elif bmi < 25.0:
            print("Overweight")
        else:
            print("Obese")

    elif m_system == 2:
        bmi = weight * 703 / (height**2)

        print("Your BMI:", bmi)

        if bmi < 18.5:
            print("Underweight")
        elif bmi < 23.0:
            print("Normal")
        elif bmi < 25.0:
            print("Overweight")
        else:
            print("Obese")

    else:
        print("Invalid choice")

else:
    print("Invalid choice, there are 1 and 2 options only ")













    






