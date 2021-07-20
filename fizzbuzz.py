number = 1
while(number <= 20):
    if(number % 15 == 0):
        print("FizzBuzz!")
    elif(number % 3 == 0):
        print("Fizz!")
    elif(number % 5 == 0):
        print("Buzz!")
    else:
        print(str(number))
    number = number + 1