import random

def main():
    state = encryptOrdecrypt()
    userInput = getUserInputs(state)
    if state == "Decrypt":
        decryptionProcess(userInput)
    else:
        encryptionProcess(userInput)

def getUserInputs(state):
    print("Welcome to the Python Ascii Caesar Cipher")
    userInput = input("Enter the sentence you would like to {} : ".format(state))
    return userInput

def encryptOrdecrypt():
    flag = True
    while flag:
        userState = input("To encrypt press E if you want to decrypt press D: ")
        if userState == "E" or userState == "e":
            state = "Encrypt"
            return state
        elif userState == "D" or userState == "d":
            state = "Decrypt"
            return state

def getUsershiftKey():
    while True:
        userShiftKey = input("Enter your shiftKey decryption Key: ")
        if userShiftKey.isalpha():
            print("Only digits are allowed.")
        else:
            shiftKey = list(userShiftKey)
            return shiftKey

def decryptionProcess(userInput):
    shiftKey = getUsershiftKey()

    decryptedText = decryptionStart(userInput, shiftKey)
    print("Your Encrypted Message is: {}".format(decryptedText))

def decryptionStart(userInput, shiftKey):
    userInputSplit = list(userInput)

    for i in range(0, len(shiftKey)):
        shiftKey[i] = int(shiftKey[i])

    asciiNum = []

    for postion in range(len(userInput)):
        asciiNum.append(ord(userInputSplit[postion]) - shiftKey[postion % len(shiftKey)])


    encryptedText = []

    for postion in range(len(userInput)):
        encryptedText.append(chr(asciiNum[postion]))

    finalEncryptedText = ''.join(encryptedText)
    return finalEncryptedText

def shiftKeyLength():
    shiftKeyLength = input("How long would you like your shift key to be: ")
    while not shiftKeyLength.isnumeric():
        print("Enter a number")
        shiftKeyLength = input("Enter again: ")
    return int(shiftKeyLength)

def encryptionProcess(userInput):
    keyNY = input("Would you like a Random Key(Yes/Y) or make your Own(No/N)?")
    if keyNY == "yes" or keyNY == "Yes" or keyNY == "Y":
        userShiftKeyLength = shiftKeyLength()
        shiftKey = shiftKeyGenorator(userShiftKeyLength)
    else:
        shiftKey = getUsershiftKey()
        for i in range(0, len(shiftKey)):
            shiftKey[i] = int(shiftKey[i])

    print("Your shiftKey is {} you will need this for decryption!".format(shiftKey))

    encryptedText = encryptionStart(userInput, shiftKey)

    print(encryptedText)

def encryptionStart(userInput, shiftKey):
    userInputSplit = list(userInput)

    asciiNum = []

    for postion in range(len(userInput)):
        asciiNum.append(ord(userInputSplit[postion]) + shiftKey[(postion) % len(shiftKey)])


    encryptedText = []

    for postion in range(len(userInput)):
        encryptedText.append(chr(asciiNum[postion]))

    finalEncryptedText = ''.join(encryptedText)
    return finalEncryptedText

def shiftKeyGenorator(shiftKeyLength):
    shiftKey = []
    for i in range(shiftKeyLength):
        shiftValue = random.randint(0, 9)
        shiftKey.append(shiftValue)

    return shiftKey

main()