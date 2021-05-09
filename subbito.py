import stdiomask
import requests
import time
import smtplib
import platform
from datetime import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def send_email(sender, recv, passw, link):
    senderMail = sender
    recvMail = recv
    password = passw
    
    msg = "New link found: " + link

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(senderMail, password)
        server.sendmail(senderMail, recvMail, msg)
        server.close()
    except Exception as ex:
        raise ex

def subito(url, timeout, sMail, rMail, passw):
    subitoLinksFile = open("SubitoLinks.txt", "w")
    target = "<div class=\"items__item\">"
    linkList = []
    global osName

    if osName == "Windows":
        toast = ToastNotifier()

    try:

        while True:
            time.sleep(timeout)

            refLink = ""

            r = requests.get(url)
            string = r.content.decode()

            startSearchIndex = string.find(target) + 34

            while string[startSearchIndex] != "\"":
                refLink += string[startSearchIndex]
                startSearchIndex += 1

            if refLink not in linkList:
                now = datetime.utcnow()

                subitoLinksFile.write(f"[{now}] - {refLink}\n")
                subitoLinksFile.write("============================================================================================\n")

                linkList.append(refLink)

                try:
                    send_email(sender=sMail, recv=rMail, passw=passw, link=refLink) # riga 21
                    print(bcolors.OKGREEN + "[+]" + bcolors.ENDC + bcolors.BOLD + " New link found, check the proper links file. Email sent.")

                    if osName == "Windows":
                        toast.show_toast("New link", "A new link has been found", duration=3, icon_path="icon.ico")

                except:
                    print(bcolors.WARNING + "[+]" + bcolors.ENDC + bcolors.BOLD + " New link found, check the proper links file. Email cannot be sent.")
            else:
                print(bcolors.OKBLUE + "[-]" + bcolors.ENDC + bcolors.BOLD + " No new links has been found.")

    except Exception as ex:
        print(f"{ex}")
    finally:
        subitoLinksFile.close()


if __name__ == "__main__":
    osName = platform.system()

    if osName == "Windows":
        from win10toast import ToastNotifier

    # SHOWS THE OPTIONS MENU
    print()
    print()
    print(bcolors.BOLD + bcolors.WARNING + "Select which site you want to target:")
    print(bcolors.ENDC + "     [1] Subito.it")
    print()

    choose = int(input(bcolors.BOLD + bcolors.WARNING + "Insert number: " + bcolors.ENDC))
    print()

    # USER INPUTS
    url = input(bcolors.BOLD + bcolors.WARNING + "Insert target URL: " + bcolors.ENDC)
    timeout = int(input(bcolors.BOLD + bcolors.WARNING + "Insert timeout (in seconds): " + bcolors.ENDC))
    print()

    sendEmail = input(bcolors.BOLD + bcolors.WARNING + "Insert the from email: " + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.WARNING + "Insert it's password: " + bcolors.ENDC, end="")
    passw = stdiomask.getpass(prompt="", mask="*")
    recvEmail = input(bcolors.BOLD + bcolors.WARNING + "Destination email: " + bcolors.ENDC)

    # CHECK THE SELECTED SITE
    if choose == 1:
        print()
        subito(url=url, timeout=timeout, sMail=sendEmail, rMail=recvEmail, passw=passw) # riga 37