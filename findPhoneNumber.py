def findPhoneNumber(phonenumber):
    if len(phonenumber) != 12:
        return False

    for i in range(0,3):
        if not phonenumber[i].isdecimal():
            return False

    if phonenumber[3] not '-':
        return False

    for i in range(5,7):
        if not phonenumber[i].isdecimal():
            return False

    if phonenumber[8] not '-':
        return False

    for i in range(9,12):
        if not phonenumber[i].isdecimal()
        return False

    return True

message = "This is my phone number 123-456-7890, and this is her phone number 098-765-4321"

for i in range(len(message)):
    chunk = message[i, i+12]
    if findPhoneNumber(chunk):
        print("We found phone number, " + str(chunk))


    
