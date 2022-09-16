import calculator;

def main():
    while(True):
        try:
            formula = input("Input a simple calculation: ")
            formulaArray = formula.split()
            num1 = int(formulaArray[0])
            operation = formulaArray[1]
            num2 = int(formulaArray[0])

            if operation == "+":
                print(str(formula+" = "+str(calculator.add(num1,num2))))
            elif operation == "-":
                print(str(formula+" = "+str(calculator.subtract(num1,num2))))
            elif operation == "*":
                print(str(formula+" = "+str(calculator.multiply(num1,num2))))
            elif operation == "/":
                print(str(formula+" = "+str(calculator.divide(num1,num2))))
            else:
                print("You entered an irregualr formula. Make sure the formula has a valid operator.")
            break
        except Exception:
            print("You entered an irregualr formula. Make sure the formula has real numbers, a valid operator, and is separated by a space between each part.")


if __name__ == "__main__":
    main()
