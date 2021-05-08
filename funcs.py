import requests
import time
from datetime import datetime
import smtplib

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
                    send_email(sender=sMail, recv=rMail, passw=passw, link=refLink)
                    print(f"[+] New link found, check the proper links file. Email sent.")
                except:
                    print(f"[+] New link found, check the proper links file. Email cannot be sent.")
            else:
                print(f"[-] No new links has been found.")

    except Exception as ex:
        print(f"{ex}")
    finally:
        subitoLinksFile.close()
