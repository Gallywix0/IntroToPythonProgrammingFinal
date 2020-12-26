# Damien Drkae
# December 11, 2020
# # FinalProject.py

# Create a program that can decide if two numbers input by user can be divided by 3, 5, or both.




#Function for division by 3 or 5
def divisibleBy3(number):
    if number % 3 == 0:
        return True
    else:
        return False








def divisibleBy5(number):
    if number % 5 == 0:
        return True
    else:
        return False





# Asking user for input numbers
startNumber = int(input('Enter your first number!'))
lastNumber = int(input('Enter your second number!'))
print('-'*25)
for num in range(startNumber,lastNumber + 1):
    if divisibleBy3(num) and divisibleBy5(num):
        print(num, '-- Both!')
    elif divisibleBy3(num):
        print(num, '-- 3')
    elif divisibleBy5(num):
            print(num, '-- 5')
    else:
                print(num)
