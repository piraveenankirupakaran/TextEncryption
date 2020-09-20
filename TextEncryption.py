import random #It will aid me to generate random numbers
import sys  #It allows the user to exit the program when there is an error with the files
import time #It allows the programs to wait for a few seconds after diplaying something
import math # It alows you to undertake mathematical functions


#this is a function that I have made and I can call this back anywhere in the program
def EncryptMessage():       
    Eight_Num = []
    # I have for the eight random numbers variable. This is because the eight numbers will be stored into a list
    offsetFactor = 0
    # I have made this variable: offsetFactor equal to zero as the value will chnage once the program is executed
    RandomNumber = range(33, 126)
    # A random number is set in the range of 33- 126
    time.sleep(2)
    # It waits for 2 seconds
    Eight_Num = random.sample((RandomNumber), 8)
    #It generates 8 random numbers in that certain range
    print (Eight_Num)
    # The generated eight numbers are displayed
    offsetFactor = int(sum(Eight_Num) / 8 )- 32
    #The offsetFactor variable will now alter its value as eight numbers generated are added together and the sum is divided by 8 and the value is rounded down to the nearest number and it is subtracted by 32 in order to generate an offset factor
    print ("This is your Offset Factor: ")
    #It will first display a message and then the offsetFactor will be displayed
    print (offsetFactor)
    time.sleep(2)
    # It waits for 2 seconds
    Code = ''.join(map(chr, (Eight_Num)))
    # The the eight numbers are joined together and it is converted into its corresponding ASCII code in order to create the encryption key
    print("You will need the following key when decrypting the message:  ")
    #A message is diplayed to the user and then the encryption key is displayed to the user.
    print("Your encryption key is: " + (Code))
    

    inputfilename = open(input("Enter the name of the text file you want to encrypt (include the extension): "), mode="r").read()
    # This allows the user to type in the name of the file containing the plaintext
    print ("Code that will be encrypted:")
    # A message will be displayed and the message inside the file containing the plaintext will be displayed
    print (inputfilename)
    number = 0
    # I have made this variable 0 as the value will change once the program is executed
    Converted_message = ""
    # this varaible will be string hence this is to store each line and letter fo the text is converted
    for char in Code:       # Getting back the generated code
        number = number + ord(char)
        # Here the charcters in the code are converted into numbers so that the offset_factor can be calculated. 
    offset_factor = math.floor(number / 8) - 32
    for char in inputfilename:      #It is checking for the string/characters inside the plaintext file
        if char == " ":
            #if the plaintext file is empty it will then convert message but it will be blank/emty string. This code does not convert space to the ASCII "32", but leaves it as a space
            Converted_message = Converted_message + " "
        else:
            plusoffset = ord(char) + offsetFactor
            # here the offset_factor calculated before in the for loop is added onto the number representation of the plaintext. This is put under a variable called plusoffset 
            if plusoffset > 126:
                #If plusoffset is greater than 126, it will subtract 94 from plusoffset
                plusoffset = plusoffset - 94
            Converted_message = Converted_message + str(chr(plusoffset))
            #If not the Converted_message variable will be added to the ASCII representation of the plusoffset variable
    outputfilename = open(input("Enter name of the new text file so that the ciphered text can be saved with the ending '.txt': "), mode="w").write(Converted_message)
    # then once the name of the new file (containg the ciphered text) is typed in the message converted is written onto the file
    print ("Encryption Finished.....")
    # This message is displayed to the user to notify them that the plaintext message has been encrypted
    
def ExtendedEncryption():
    offsetFactor = 0
    # I have made this variable: offsetFactor equal to zero as the value will chnage once the program is executed
    RandomNumber = range(33, 126)
    # A random number is set in the range of 33- 126
    time.sleep(2)
    # It waits for 2 seconds
    Eight_Num = random.sample((RandomNumber), 8)
    #It generates 8 random numbers in that certain range
    print (Eight_Num)
    # The generated eight numbers are displayed
    offsetFactor = int(sum(Eight_Num) / 8 )- 32
    #The offsetFactor variable will now alter its value as eight numbers generated are added together and the sum is divided by 8 and the value is rounded down to the nearest number and it is subtracted by 32 in order to generate an offset factor
    print ("This is your Offset Factor: ")
    #It will first display a message and then the offsetFactor will be displayed
    print (offsetFactor)
    time.sleep(2)
    # It waits for 2 seconds
    Code = ''.join(map(chr, (Eight_Num)))
    # The the eight numbers are joined together and it is converted into its corresponding ASCII code in order to create the encryption key
    print("You will need the following key when decrypting the message:  ")
    #A message is diplayed to the user and then the encryption key is displayed to the user.
    print("Your encryption key is: " + (Code))

    inputfilename = open(input("Enter the name of the text file you want to encrypt (include the extension): "), mode="r").read()
    print ("Code that will be encrypted:")
    print (inputfilename)
    number = 0
    # I have made this variable 0 as the value will change once the program is executed
    Converted_message = ""
    # this varaible will be string hence this is to store each line and letter fo the text is converted
    for char in Code:       # Getting back the generated code
        number = number + ord(char)
        # Here the charcters in the code are converted into numbers so that the offset_factor can be calculated. 
    offset_factor = math.floor(number / 8) - 32
    for char in inputfilename:      #It is checking for the string/characters inside the plaintext file
        if char == " ":
            #if the plaintext file is empty it will then convert message but it will be blank/emty string. This code does not convert space to the ASCII "32", but leaves it as a space
            Converted_message = Converted_message + " "
        else:
            plusoffset = ord(char) + offsetFactor
            # here the offset_factor calculated before in the for loop is added onto the number representation of the plaintext. This is put under a variable called plusoffset 
            if plusoffset > 126:
                #If plusoffset is greater than 126, it will subtract 94 from plusoffset
                plusoffset = plusoffset - 94
            Converted_message = Converted_message + str(chr(plusoffset))
    Converted_message = Converted_message.replace(" ", "")
    # The converted message gets replaced as an emtpy string
    Converted_message = ' '.join([Converted_message[i:i+5] for i in range(0, len(Converted_message), 5)])
    #converted message will be joined into five characters with a space separating each group. This is so that it is harder to crack the encrypted message
    #this will make it harder for the user to crack the message
    outputfilename = open(input("Enter name of the new text file so that the ciphered text can be saved with the ending '.txt': "), mode="w").write(Converted_message)


def DecryptMessage():
    inputfilename = open(input("Name the file and directory you want to load that contains the ciphered text with the ending '.txt': "), mode="r").read()
    # the name of the file containing the ciphered text file is inputted by the user and the program reads the file
    offset_Factor = 0
    #A varibale has been created and I have set the value of the offset_Factor to zero, as the value will change once the program is executed. The variable will store the offset factor
    decrypted_message = ""
    # this variable will be string hence this is when each line and letter of the converted text to gain the original plaintext
    inputCode = input("Type into the eight character key: ")
    #Then the user enters in the eight character key. The user will type the code on the next line
    tries = 0
    # number = len(inputCode) - inputCode.count(" ")
    if (len(inputCode)- inputCode.count(" ")) == 8:# if the numbers of characters in the eight character key entereed by the user is 8 and with no spaces
        print ("The text will now be now  encrypted")# the message will be printed  and the code will carry on and pass the if statement
    else:
        while tries < 5: # If not the user has 5 tries, and if tries are greater than 5
            inputCode = input("You have not entered 8 characters and you only have 5 tries, please try again: ") # the user will be displayed this mesage each time 8 characters is not used 
            if (len(inputCode)- inputCode.count(" ")) == 8: # if the encryption key entered is eight character the message will be encrypted
                print ("The text will now be now  encrypted") # if the arguaments are bpassed in the if statement the message will be printed
                break # it will carry on with the rest of the code
            tries = tries + 1 # each time the encryption key is entered incorrectly, the tries will increase by 1
            if tries == 5: # when the variable tries is equal to 5 the program exits
                sys.exit(0)

    for char in inputCode:
            offset_Factor = offset_Factor + int(ord(char))
            # Here the characters in the code entered by the user are converted into numbers so that the offset_factor can be calculated. 
    offset_Factor = math.floor(offset_Factor / 8) - 32
    print ("This is your Offset Factor: ")
    print (offset_Factor)
            
    #The offset_Factor variable will now alter its value as eight numbers generated are added together and the sum is divided by 8 and the value is rounded down to the nearest number and it is subtracted by 32
    for char in inputfilename:  #It is checking for the string/characters inside the ciphered text file
        if char == " ":
            # If the file is empty the variable will also be an empty string and therefore nothing will be decrypted
            decrypted_message = decrypted_message + " "
        else:
            minusoffset = ord(char) - offset_Factor
            #A variable called minusoffset is created and this is the number representation of the string inside the ciphered text file
            if minusoffset < 33:
                minusoffset = minusoffset + 94      # If minusoffset is less than 33, 94 is added to this variable. 
            decrypted_message = decrypted_message + str(chr(minusoffset))
            # Then the decrypted message is added on with the ASCII representation of minusoffset, and finally the message is displayed. 
    print(decrypted_message)


def menu(): #This function will be called at the end of the page as this is for the different options
    time.sleep(2)  #It will then display the welcome screen then this function will be run after 2 seconds
    selection = int(input("please enter your selection:  "))#ask user to enter their option
    # The input should be an interger so therefore when 1,2,3,4 is pressed it directly you to that certain page.
    if selection == 1:
             # When 1 is entered into the program it directs you to the Encrypt a Message page
             print (" ......Encrypt a message...... ")
             # It therefore displays the message "......Encrypt a message......"
             #This notifies the user what page they are on, so therefore it is user friendly
             print(EncryptMessage())
             # it runs the function: EncryptMessage


    elif selection ==2:
            #When 2 is entered into the program it directs you to the Decrypt a Message page
            print (" ......Extended Encryption...... ")
            # It therefore displays the message "......Extended Encryption......" 
           #This notifies the user what page they are on, so therefore it is user friendly
            print(ExtendedEncryption())
            # it runs the function: ExtendedEncryption
            
            

    elif selection ==3:
            #When 3 is entered into the program it directs you to the Decrypt a Message page
            print (" ......Decrypt a message...... ")
            # It therefore displays the message "......Decrypt a message......"
            #This notifies the user what page they are on, so therefore it is user friendly
            print(DecryptMessage())
            # it runs the function: DecryptMessage
 
            

    elif selection ==4:
             #When 4 is entered into the program it exits the program.
             print("Closing program....")
             # It therefore displays the message "Closing program...."
             time.sleep(1)
             #It will wait for 1 second and then exit the program
             exit()
             # Exiting the program
    else:
             print("invalid selection (you must choose 1 or 2 or 3 or 4)")
             # when a invalid input is entered it will display a message

    
print("-_-_-_Welcome to the Text Encryption Application-_-_-_")
# this is the Welcome screen that fistly displays the title
print("------------------------------------------------------")
print("|                     Main Menu                      |")
print("|               The different Options:               |")
print("|                  [1]... Encrypt a message          |")
print("|                  [2]... Extended Encryption        |")
print("|                  [3]... Decrypt a message          |")
print("|                  [4]... Exit the program           |")
# It displays the different options of the program


menu()
# The menu() function has been called so that the user can navigate to the certain pages

