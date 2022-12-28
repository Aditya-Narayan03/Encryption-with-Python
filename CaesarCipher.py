import random

print("-------------------------------------------")
mode = input('\nDo you want to encode or decode : ').lower().strip()
if mode == "encode":
    val = "E"

elif mode == "decode":
    val = "D"

else:
    print("\nPLEASE DO NOT ENTER INVALID ARGUMENT!!!!!")
    quit()


string = input(f"Enter the string to be {mode}d : ")
shift = int(input("Enter the shift Value : "))

print("\n-------------------------------------------")
encoded = ''
decoded = ''

if val == 'E':
    for line in string:

        if line.isalpha() == True:

            if line.islower():
                value = (ord(line) + shift - 97) % 26
                encoded += chr(value + 97)

            elif line.isupper():
                value = (ord(line) + shift - 65) % 26
                encoded += chr(value + 65)

        else:
            encoded += line


elif val == 'D':

    for line in string:

        if line.isalpha() == True:

                if line.islower():
                    value = (ord(line) - shift - 97) % 26
                    encoded += chr(value + 97)

                elif line.isupper():
                    value = (ord(line) - shift - 65) % 26
                    encoded += chr(value + 65)

        else:
            encoded += line


else:
    print("\nInvalid Argument!!!")
    print("\n-------------------------------------------")
    quit()


if encoded:
    print(f'\nEncoded : {encoded}')
    print("\n-------------------------------------------")

elif decoded:
    print(f"\nDecoded : {decoded}")
    print("\n-------------------------------------------")