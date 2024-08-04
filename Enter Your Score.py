user_number = input("Your score: ")
#selain menggunakan try, bisa juga menggunakan user_number = int(user_number)
try:
    user_number = int(user_number)

    if user_number >= (90):
        age = int(input("What is your age? "))
        if age <10:
            print("Your Grade is A+")
        else:
            print("Your Grade is A")
    elif user_number >= (80): 
        age = int(input("What is your age? "))
        if age < 10:
            print("Your Grade is B+")
        else:
            print("Your Grade is B")
    elif user_number >= (70):
        age = int(input("What is your age? "))
        if age < 10:
            print("Your Grade is C+")
        else:
            print("Your Grade is C")
    elif user_number >= (60):
        age = int(input("What is your age? "))
        if age < 10:
            print("Your grade is D+")
        else:
            print("Your grade is D")
    else:
        print("Grade F")
    
except ValueError:
    print("Format yang anda masukan salah")
