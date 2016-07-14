'''
Created on 11-Jul-2016

@author: zeeshan
'''
from decimal import DivisionByZero
while True:
    try:
        number = int(input("What's your favourite number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and Enter a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except:
        print("Exception occured")
    finally:
        print("Loop completed")