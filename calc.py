import math
#so far, can't handle:
#   - decimals
#   - negative numbers
#   - parathesises
#   - exponents
#   - common irrationals and imaginaries (i.e. pi, e, i, etc)
#   - any variable assignment (e.g. x = 5; 5x + 1 = 26)


#function to get rid of all types of whitespace in equation
def delete_spaces(equation):
    equation = "".join(equation.split())
    return equation

#find numbers from string
def find_number(equation, index, command):
    #for finding the entirety of the left hand side number
    if (command == "left"):
        #cut string in half before math operator
        new_string = equation[:index]
        i = 0
        
        #MIGHT BE TEMP
        #if left length == 0
        if len(new_string) == 0:
            return False

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


#function for multiplication
#handles integers (so far)
def multiply(equation):
    index = equation.find("*")

    #checks if multuplication symbol is used at start or end of equation
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
		

#function for division
#handles integers (so far)
def divide(equation):
    index = equation.find("/")

    #checks if division symbol is used at start or end of equation
    if equation[len(equation) -1] == "/" or index == 0:
        return "invalid"
    else:
        while (index != -1):
            left_index = equation[index - 1]
            right_index = equation[index + 1]
            #checks if left and right
            if left_index.isdigit() and right_index.isdigit() and right_index != "0":
                print(left_index, right_index)

                left_number = find_number(equation, index, "left")
                right_number = find_number(equation, index + 1, "right")

                print(left_number, right_number)

                #integer division - for now
                ans = left_number // right_number
                equation = equation.replace(equation[index-len(str(left_number)): index+len(str(right_number))+1], str(ans))
                index = equation.find("/")
            
            #dividing by zero error
            elif right_index == "0":
                return "cannot divide by zero"
            
            #finding undefined non-digits
            else:
                return "non-digit found"
        return equation


#function for additon
#handles integers (so far)
def add(equation):
    index = equation.find("+")

    #checks if addition symbol is used at start or end of equation
    if equation[len(equation) -1] == "+" or index == 0:
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

                ans = left_number + right_number
                equation = equation.replace(equation[index-len(str(left_number)): index+len(str(right_number))+1], str(ans))
                index = equation.find("+")

            #finding undefined non-digits
            else:
                return "non-digit found"
        return equation


#function for subtraction
#handles integers (so far)
def subtract(equation):
    index = equation.find("-")

    #checks if addition symbol is used at start or end of equation
    if equation[len(equation) -1] == "-" or (index == 0 and len(equation) < 2):
        return "invalid"
    else:
        while (index != -1):
            left_index = equation[index - 1]
            right_index = equation[index + 1]
            #checks if left and right
            if left_index.isdigit() and right_index.isdigit():
                print(left_index, right_index)

                #return if result is just one negative number
                if find_number(equation, index, "left") == False:
                    return equation

                left_number = find_number(equation, index, "left")
                right_number = find_number(equation, index + 1, "right")

                print(left_number, right_number)

                ans = left_number - right_number
                equation = equation.replace(equation[index-len(str(left_number)): index+len(str(right_number))+1], str(ans))
                index = equation.find("-")

            #finding undefined non-digits
            else:
                return "non-digit found"
        return equation



#main part/function calling
equation = input("Enter equation: ")

#if equation not given
if len(equation) == 0:
    print("equation does not exist")
    quit()

equation = delete_spaces(equation)

print("Current:", equation)

#PEMDAS
equation = multiply(equation)
equation = divide(equation)
equation = add(equation)
equation = subtract(equation)

print("Equation now:", equation)

