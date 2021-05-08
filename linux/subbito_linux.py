from funcs_linux import *
import stdiomask

print()
print()
print(bcolors.BOLD + bcolors.WARNING + "Select which site you want to target:")
print(bcolors.ENDC + "     [1] Subito.it")
print()

choose = int(input(bcolors.BOLD + bcolors.WARNING + "Insert number: " + bcolors.ENDC))
print()

url = input(bcolors.BOLD + bcolors.WARNING + "Insert target URL: " + bcolors.ENDC)
timeout = int(input(bcolors.BOLD + bcolors.WARNING + "Insert timeout (in seconds): " + bcolors.ENDC))
print()
sendEmail = input(bcolors.BOLD + bcolors.WARNING + "Insert the from email: " + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + "Insert it's password: " + bcolors.ENDC, end="")
passw = stdiomask.getpass(prompt="", mask="*")
recvEmail = input(bcolors.BOLD + bcolors.WARNING + "Destination email: " + bcolors.ENDC)


if choose == 1:
    print()
    subito(url=url, timeout=timeout, sMail=sendEmail, rMail=recvEmail, passw=passw)