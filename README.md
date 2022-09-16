# Individual GitHub Exercise
## Install Python
Use the following link to install the latest version of python.
https://www.python.org/downloads/

## calculator.py
The calculator.py file contains 4 functions. Each take two variables *num1* and *num2* then apply their designated operation onto them and return the answer.
* add(num1, num2) - Returns the sum of *num1* and *num2* -- *num1* + *num2*
* subtract(num1, num2) - Returns the difference of *num1* and *num2* -- *num1* - *num2*
* multiply(num1, num2) - Returns the product of *num1* and *num2* -- *num1* * *num2*
* divide(num1, num2) - Returns the quotient of *num1* and *num2* -- *num1* / *num2*

## main.py
The main.py file contains a main function that asks the user for an input of a simple calculation. The simple calculation syntax is as follows,

*num1* *operation* *num2*

Each piece of the syntax is serparated by a space (" ").

Next, the function checks if the operator is valid (+, -, *, or /) or else it prints *"You entered an irregualr formula. Make sure the formula has a valid operator and is separated by a space between each part."* to tell the user they inputed their formula incorrectly. If the operator is valid, it will apply the appropriate operation onto the numbers by sending them to the appropriate function in the calculator.py file.
