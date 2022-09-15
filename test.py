import numpy as np
import calculator;

def main():
    nums = np.array([[1,1],[2,2],[10,10],[50,50],[1000,1000],[365,256],[420,69],[99,1],[17,38],[600,66]])
    addAns = [1+1,2+2,10+10,50+50,1000+1000,365+256,420+69,99+1,17+38,600+66]
    subAns = [1-1,2-2,10-10,50-50,1000-1000,365-256,420-69,99-1,17-38,600-66]
    mulAns = [1*1,2*2,10*10,50*50,1000*1000,365*256,420*69,99*1,17*38,600*66]
    divAns = [1/1,2/2,10/10,50/50,1000/1000,365/256,420/69,99/1,17/38,600/66]

    testAns = []
    for i in range(0,len(nums)):
        num1 = nums[i][0]
        num2 = nums[i][1]
        testAns.append(calculator.add(num1,num2))
    print("Test: " + str(testAns))
    print("Answers: " + str(addAns))
    if testAns == addAns:
        print("Addition test was successful!",end="\n\n")
    else:
        print("Addition test failed!",end="\n\n")
    
    testAns = []
    for i in range(0,len(nums)):
        num1 = nums[i][0]
        num2 = nums[i][1]
        testAns.append(calculator.subtract(num1,num2))
    print("Test: " + str(testAns))
    print("Answers: " + str(subAns))
    if testAns == subAns:
        print("Subtraction test was successful!",end="\n\n")
    else:
        print("Subtraction test failed!",end="\n\n")
    
    testAns = []
    for i in range(0,len(nums)):
        num1 = nums[i][0]
        num2 = nums[i][1]
        testAns.append(calculator.multiply(num1,num2))
    print("Test: " + str(testAns))
    print("Answers: " + str(mulAns))
    if testAns == mulAns:
        print("Multiplication test was successful!",end="\n\n")
    else:
        print("Multiplication test failed!",end="\n\n")
    
    testAns = []
    for i in range(0,len(nums)):
        num1 = nums[i][0]
        num2 = nums[i][1]
        testAns.append(calculator.divide(num1,num2))
    print("Test: " + str(testAns))
    print("Answers: " + str(divAns))
    if testAns == divAns:
        print("Division test was successful!")
    else:
        print("Division test failed!",end="\n\n")

if __name__ == "__main__":
    main()