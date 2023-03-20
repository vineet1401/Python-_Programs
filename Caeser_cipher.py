

upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
		 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def encrypt(word):
    shift =int(input("Enter shift number : "))
    encrypt = []
    for i in word:
        if(i.isupper() == True):
            index = upper_alpha.index(i)
            index += shift
            if(index > 25):
                index -= round((index//26) * 26)
            encrypt.append(upper_alpha[index])
        elif (i == " "):
            encrypt.append(i)
        else:
            index = lower_alpha.index(i)
            index += shift
            if (index > 25):
                index -= round((index//26) * 26)
            encrypt.append(lower_alpha[index])
            
    joinword = "".join(encrypt)
    return joinword


def decrypt(word):
    shift = int(input("Enter shift number : "))
    decrypt = []
    for i in word:
        if (i.isupper() == True):
            index = upper_alpha.index(i)
            index -= (shift)
            if (index < 0):
                index -= round((index//26) * 26)
            decrypt.append(upper_alpha[index])
        elif(i == " "):
            decrypt.append(i)
        else:
            index = lower_alpha.index(i)
            index -= shift
            if (index < 0):
                index -= round((index//26) * 26)
            decrypt.append(lower_alpha[index])

    joinword = "".join(decrypt)
    return joinword

  
word = input("Enter the word: ")
print("*** \t 1 : Encrypt Word \t *** \n*** \t 2 : Decrypt Word \t *** ")
choice = int(input("Enter Choice : "))
if(choice == 1):
    print (f"Your Encrypted Message is ; {encrypt(word)}")
elif(choice == 2):
    print(f"Your Decrypted Message is ; {decrypt(word)}")
else:
    print("Enter valid choice.")

    

            



        
        
    