username = input("Enter your preferred name: ")

print("Hello " + username + "!")

numb1 = int(input("Enter your first number: "))
numb2 = int(input("Enter your second number:"))

option = input("Enter your option(A,B,C,D): ")

A = numb1+numb2
B = numb1-numb2
C = numb1*numb2
D = numb1/numb2
E = numb1%numb2

if option == "A":
    print("The sum of the two numbers is: " + str(A))
    if option == "B":
        print("The difference of the two numbers is: " + str(B))
        if option == "C":
            print("The product of the two numbers is: " + str(C))
            if option == "D":
                print("The quotient of the two numbers is: " + str(D))
                if option == "E":
                    print("The remainder of the two numbers is: " + str(E))
else:
    print("Invalid option")
