
from django.shortcuts import render



Decimal_Input = 0
Decimal_Hour = 0
Binary_Input = ""
Binary_Hour = ""
Period_Input = "Am"
Conversion_Format = ""



# Create your views here.
def Home (request):
        
    return render(request, "Home_Page.html")



def Result (request):
    
    State = "R"
    
    global Conversion_Format
    global Decimal_Input
    global Binary_Input
    global Period_Input
    global Decimal_Hour
    global Binary_Hour
    
    Conversion_Format = str(request.POST.get("format"))
    
    Period_Input = str(request.POST.get("period"))
    
    if Conversion_Format == "decimal":
        Decimal_Input = int(request.POST.get("time"))
        Convert_Decimal_to_Binary(Decimal_Input)
        if Decimal_Input > 12:
            Decimal_Hour = Decimal_Input - 12
            Period_Input = "Pm"
        else:
            Decimal_Hour = Decimal_Input
    
    else :
        Binary_Input = str(request.POST.get("time"))
        Read_Binary_Clock(Binary_Input)
    
    
    Context = {
        "State": State,
        "Conversion_Format": Conversion_Format,
        "Decimal_Input": Decimal_Input,
        "Binary_Input": Binary_Input,
        "Period_Input": Period_Input,
        "Decimal_Hour": Decimal_Hour,
        "Binary_Hour": Binary_Hour,
    }
    
    return render(request, "Home_Page.html", Context)







# Function to convert a decimal number to a binary representation with a fixed length of 5 bits.
def Convert_Decimal_to_Binary(Decimal_Num: int):
    global Binary_Hour
    
    Binary_List = [0] * 5  # Initialize a list of 5 zeros.
    i = 0
    while Decimal_Num > 0:  # Loop until the decimal number is reduced to 0.
        Binary_List[i] = Decimal_Num % 2  # Store the remainder of Decimal_Num divided by 2 (either 0 or 1).
        Decimal_Num = Decimal_Num // 2  # Use integer division to halve the Decimal_Num.
        i += 1
    Binary_List.reverse()  # Reverse the list to match the correct binary order.
    
    Binary_Hour = ''.join(str(i) for i in Binary_List)  # Return the binary list.



# Function to convert a binary list back to a decimal number.
def Convert_Binary_to_Decimal(Binary_List: list):
    global Period_Input
    
    Decimal_Num = 0
    for i in range(len(Binary_List)):  # Iterate over the binary list.
        Decimal_Num += Binary_List[i] * 2**(len(Binary_List) - i - 1)  # Convert binary to decimal using powers of 2.
    if Decimal_Num > 12:  # If the decimal number exceeds 12, it's PM.
        Decimal_Num -= 12
        Period_Input = "Pm"
    else:
        Period_Input = "Am"
    return Decimal_Num  # Return the decimal number.



# Function to read and process a binary time input.
def Read_Binary_Clock(String_Number: str):
    global Binary_Hour
    global Decimal_Hour
    
    Binary_List = [int(i) for i in String_Number]  # Convert each character in the string to an integer to form the binary list.
    
    # Ensure the binary list is exactly 5 bits long.
    if len(Binary_List) < 5:
        Binary_List.reverse()  # Reverse for easier manipulation.
        for i in range(5 - len(Binary_List)):  # Append zeros to make length 5.
            Binary_List.append(0)
        Binary_List.reverse()  # Reverse back to original order.
    elif len(Binary_List) > 5:
        Binary_List = Binary_List[-5:]  # Trim to the last 5 digits if longer.
    
    Binary_Hour = ''.join(str(i) for i in Binary_List)
    
    Decimal_Hour = Convert_Binary_to_Decimal(Binary_List)  # Convert to decimal.
    