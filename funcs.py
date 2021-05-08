import requests
import time
from datetime import datetime
import smtplib
from win10toast import ToastNotifier

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
        print(ex)

def subito(url, timeout, sMail, rMail, passw):
    subitoLinksFile = open("SubitoLinks.txt", "w")
    target = "<div class=\"items__item\">"
    linkList = []
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
                    print(bcolors.OKGREEN + "[+]" + bcolors.ENDC + bcolors.BOLD + " New link found, check the proper links file. Email sent.")
                    toast.show_toast("New link", "A new link has been found", duration=1, icon_path="icon.ico")
                    send_email(sender=sMail, recv=rMail, passw=passw, link=refLink)
                except:
                    print(bcolors.OKGREEN + "[+]" + bcolors.ENDC + bcolors.BOLD + " New link found, check the proper links file. Email cannot be sent.")
            else:
                print(bcolors.OKBLUE + "[-]" + bcolors.ENDC + bcolors.BOLD + " No new links has been found.")

    except Exception as ex:
        print(f"{ex}")
    finally:
        subitoLinksFile.close()
