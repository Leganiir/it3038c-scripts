# Isaac Leganik Python Calculator. Idea from https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3.

def Get_Operation():
    #Get Operation
    print("Please enter your desired operation: \n+ Addition \n- Subtraction \n* Multiplication \n/ Division \n** Power \n% Modulo")
    Operation = str(input())
    
    #List of valid accepted operations.
    valid = ["+", "-", "*", "/", "**", "%"]
    
    #Check to make sure operation is valid.
    while True:
        if Operation in valid:
            break
        else:
            print("Please select only an accepted operation, +, -, *, /, **, %")
            Operation = str(input())
            
    # Return
    return Operation
    
def Do_The_Math(Operation, Number_1, Number_2):
    #Simple math calculations.
    
    if Operation == "+":
        Calculated_Number = Number_1 + Number_2
    elif Operation == "-":
        Calculated_Number = Number_1 - Number_2
    elif Operation == "*":
        Calculated_Number = Number_1 * Number_2
    elif Operation == "/":
        Calculated_Number = Number_1 / Number_2
    elif Operation == "**":
        Calculated_Number = Number_1 ** Number_2
    else:
        Calculated_Number = Number_1 % Number_2
    
    #Print and return value.
    print(str(Number_1) + " " + Operation + " " + str(Number_2) + " = " + str(Calculated_Number))    
    return Calculated_Number
    
while True:
    Operation = Get_Operation()
    
    #Input numbers
    print("Please input your first number")
    Number_1 = int(input())
    print("Please input your second number")
    Number_2 = int(input())
    
    Calculated_Number = Do_The_Math(Operation, Number_1, Number_2)
    
    #Loop to continue making calculations.
    while True:
        print("Do you wish to continue with another operation? Press Y if for yes and N for no.")
        To_Continue = str(input())
        
        #Get new number, send that, new operation, and old calculated number back through function.
        if To_Continue.lower() == "y":
            Operation = Get_Operation()
            print("Please enter another number.")
            Number_2 = int(input())
            Number_1 = Calculated_Number
            Calculated_Number = Do_The_Math(Operation, Number_1, Number_2)
            
        elif To_Continue.lower() == "n":
            break
        
        else:
            print("Please enter only Y or N")
    
    break