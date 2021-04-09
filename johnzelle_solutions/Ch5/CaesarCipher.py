def main():


    Original = input("Please enter your message:")

    key = 2

    encode =""
    for ch in Original:
        encode = encode+chr(ord(ch)+key)

    print("The ciphered message is: ",encode)

    decode = ""
    for ch1 in encode:
        decode = decode+chr(ord(ch1)-key)

    print("The deciphered message is: ",decode)

main() 
    
