from funcs import *

print()
print()
print(f"Select which site you want to target:")
print(f"     [1] Subito.it")
print()

choose = int(input(f"Insert number: "))
print()

url = input(f"Insert target URL: ")
timeout = int(input(f"Insert timeout (in seconds): "))
print()
sendEmail = input(f"Insert the from email: ")
passw = input(f"Insert it's password: ")
recvEmail = input(f"Destination email: ")


if choose == 1:
    print()
    subito(url=url, timeout=timeout, sMail=sendEmail, rMail=recvEmail, passw=passw)
