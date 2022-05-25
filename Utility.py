from Credentials import UserInfo
import smtplib
import requests
from bs4 import BeautifulSoup

class Email():
 
    def send_email(self, to, content):
        EmailAddress = UserInfo.EmailAddress
        EmailPassword = UserInfo.EmailPassword
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        print("verifying")
        server.login( EmailAddress, EmailPassword)
        server.sendmail('aryanshakya851.com', to, content)
        print("Done!")
        server.close()

class WebScraping():
    def WebScraper():
        url = input("URL Please! : ") # gets the HTML data
        r = requests.get(url)
        htmlContent = r.content

        soup = BeautifulSoup(htmlContent, 'html.parser') # parse the HTML

        
        print(f"WebScraper not avail")
