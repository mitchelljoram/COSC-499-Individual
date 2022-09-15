import calculator;

def main():
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
        print("You entered an irregualr formula.")


if __name__ == "__main__":
    main()
