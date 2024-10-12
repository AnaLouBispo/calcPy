def Addition(n1, n2):
    return n1 + n2

def Subtraction(n1, n2):
    if n1 < n2:
        print('Your result will be negative:')
    return n1 - n2

def Multiplication(n1, n2):
    return n1 * n2

def Division(n1, n2):
    if n2 == 0:
        print("Division by zero is not allowed!")
        return None
    return n1 / n2



while True:
    nOne = float(input("Enter the first number: "))
    nTwo = float(input("Enter the second number: "))
    print('----------------------------------------')
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Close calculator")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Result: " + str(Addition(nOne, nTwo)))
    elif choice == '2':
        print("Result: " + str(Subtraction(nOne, nTwo)))
    elif choice == '3':
        print("Result: " + str(Multiplication(nOne, nTwo)))
    elif choice == '4':
        result = Division(nOne, nTwo)
        if result is not None:
            print("Result: " + str(result))
    elif choice == '5':
        break
    else:
        print("Invalid, please try again.")


#str() -> serve para converte o resultado da função em string para que seja exibido com o print