
spec_char = "!@#$%^&*()_+"
alphanums = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

# Performed manual for alphanumeric to ignore special characters
def checkAlpha(checkString=""):
    characterlist = list(alphanums)
    stringlist = list(checkString)

    contains_alphan = False

    for data in stringlist:
        for cc in characterlist:
            if data == cc:
                contains_alpha = True

    return contains_alpha


username_input = input("Enter username: ")
passwords_input = input("Enter a series of passwords separated by comma: ")

if(len(passwords_input) > 0):

    passwords = passwords_input.split(',')

    valid_pwd = []

    if len(passwords) > 0:

        for passw in passwords:

            print("Checking: ",passw)

            if len(passw) >= 6 and len(passw) <= 12:
                print(passw, " passed")
                if checkAlpha(passw):
                    print(passw, " passed 2")
                    for character in passw:
                        # check if it contains special character
                        for specc in spec_char:
                            if character == specc:
                                print(passw, "passed the final check.")
                                valid_pwd.append(passw)
                                break


        print("Valid passwords: ", valid_pwd)

