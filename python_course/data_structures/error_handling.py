try:
    num=int(input("Enter a number: "))
    result = 10/ num
    print("result:",result)

except ValueError:
    print("invalid input:please enter a number.")
except ZeroDivisionError:
    print("you cannot divide by zero.")
finally:
    print("program over.")
    
