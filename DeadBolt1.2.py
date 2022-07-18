import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



###### encryption with pass ######

def encryptpass():
    if options == "1":
        input("Are u sure u want to do this? If the pass is gone your file is dead. I dont want to code it in so press CTRL+C to abort to continue enter")
        file = input("Type file path\n")
        password_provided = input("Type password\n")
        password = password_provided.encode()

        salt = b'\xd1\x95K\xcbsjG\x1e\\\xad\xce\n3>5_'
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
        key = base64.urlsafe_b64encode(kdf.derive(password))
    
    
        with open(file, "rb") as thefile:
            content = thefile.read()
            content_encrypted = Fernet(key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)
            print("file has been encrypted")
            final = input("Press enter to exit")
            quit()


###### decryption with pass ######

def decryptpass():
    if options == "1":
        file = input("Type file path\n")
        print("Remember pass?")
        password_provided = input("Type password\n")
        password = password_provided.encode()

        salt = b'\xd1\x95K\xcbsjG\x1e\\\xad\xce\n3>5_'
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
        key = base64.urlsafe_b64encode(kdf.derive(password))


        with open(file, "rb") as thefile:
            content = thefile.read()
            content_decrypted = Fernet(key).decrypt(content)
    

        with open(file, "wb") as thefile:
            thefile.write(content_decrypted)
            print("file has been decrypted")
            final = input("Press enter to exit")
            quit()


###### encryption ######

def encryptkey():
    if options == "2":
        answer = input("Are you sure to proceed? If you loose your key file your file is dead!! Type y to accept\n")
        proceed = "y"

        if answer != proceed:
            print("no files have been encrypted")
            final = input("Press enter to exit")
            quit()

        else:
            file = input("Enter path to file to encrypt\n")
            unlock = input("Enter custom keyname\n")
            keynm = unlock+".key"    

            key = Fernet.generate_key()
            with open(keynm, "wb") as thekey:
                thekey.write(key)
            with open(file, "rb") as thefile:
                content = thefile.read()
                content_encrypted = Fernet(key).encrypt(content)
            with open(file, "wb") as thefile:
                thefile.write(content_encrypted)
            print("file has been encrypted")
            final = input("Press enter to exit")
            quit()



def decryptkey():
    if options == "2":
        print("***!!!NO KEYFILE, NO DECRYPTION!!!***")
        file = input("Enter path to file to decrypt\n")
        unlocker = input("Enter path to key\n")    


        with open(unlocker, "rb") as key:
            secretkey = key.read()

        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypted = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypted)
            print("file has been decrypted")
            final = input("Press enter to exit")
            quit()




print("""\n
                with the shitty icon
\________            ________________      __________ 
___  __ \__________ ______  /__  __ )________  /_  /_
__  / / /  _ \  __ `/  __  /__  __  |  __ \_  /_  __/
_  /_/ //  __/ /_/ // /_/ / _  /_/ // /_/ /  / / /_  
/_____/ \___/\__,_/ \__,_/  /_____/ \____//_/  \__/  
                Lock your Cock\n""")


mainmenu = input("1 encryption\n2 decryption\n0 quit\n\n")

if mainmenu == "1":
    options = input("1 encrypt with password\n2 encrypt with keyfile\n")
    if options == "1":
        encryptpass()
    if options == "2":
        encryptkey()


if mainmenu == "2":
    options = input("1 decrypt with password\n2 decryption with keyfile\n")
    if options == "1":
        decryptpass()
    if options == "2":
        decryptkey()

if mainmenu == "0":
    input("press enter to exit")
    quit()