import math

#function to get rid of all spaces in equation

#find numbers from string
def find_number(equation, index, command):
    #for finding the entirety of the left hand side number
    if (command == "left"):
        #cut string in half before math operator
        new_string = equation[:index]
        i = 0

        #finding next non-digit so full number can be found
        for char in reversed(new_string):
            if char.isdigit() == False:
                break
            i+=1

        #if went through entire string
        if i==len(new_string):
            i=0
        
        #if not, find non-reverse indice to splice
        else:
            i = len(new_string)-i

        number = new_string[i: len(new_string)]

    #for finding the entirety of the right-hand side number
    elif command == "right":
        #obtain right half
        new_string = equation[index:]
        i = 0

        #to obtain next non-digit indice
        for char in new_string:
            if char.isdigit() == False:
                break
            i+=1
        number = new_string[0:i]

    return int(number)




#equation for multiplication
#handles integers (so far)
def multiply(equation):
    index = equation.find("*")

    if equation[len(equation) -1] == "*" or index == 0:
        return "invalid"
    else:
        while (index != -1):
            left_index = equation[index - 1]
            right_index = equation[index + 1]
            #checks if left and right
            if left_index.isdigit() and right_index.isdigit():
                print(left_index, right_index)

                left_number = find_number(equation, index, "left")
                right_number = find_number(equation, index + 1, "right")

                print(left_number, right_number)

                ans = left_number * right_number
                equation = equation.replace(equation[index-len(str(left_number)): index+len(str(right_number))+1], str(ans))
                index = equation.find("*")

            #finding undefined non-digits
            else:
                return "non-digit found"
        return equation
    return "nothing changed" #keep until all cases pass
		
		


equation = input("Enter equation: ")

print("Current:", equation)

equation = multiply(equation)

print("Equation now:", equation)

