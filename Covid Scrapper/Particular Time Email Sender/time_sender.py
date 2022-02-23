import requests
import email, smtplib, ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup as bs

while True:
    TIME_NOW = time.strftime("%H:%M:%S")
    if TIME_NOW == "00:58:30":

     subject = "Daily Covid Data Sent By Python"
     body = "Daily Covid Data Sent By Python"
     sender_email = "jlcpcbofficial02@gmail.com"
     receiver_email = "jlcpcbofficial02@gmail.com"
     password = "181721Cloudybird815"

     url = "https://www.worldometers.info/coronavirus/"      

     response = requests.get(url)
     soup = bs(response.text,"lxml")
     anchor1= soup.find_all('div',"content-inner")
     for span in anchor1:
         span1 = span.find_all('div',"maincounter-number")
         one = span1[0]
         two = span1[1]
         three = span1[2]
         Total_Cases = one.text.strip()
         Deaths = two.text.strip()
         Recovered = three.text.strip()

     print("Total_Cases = " + str(Total_Cases))
     print("Total_Deaths = " + str(Deaths))
     print("Total_Recovered = " + str(Recovered))

     with open("covid_data.txt", "w") as file:
               file.write(f"Total_Cases = {Total_Cases}")
               file.write("\n")
               file.write(f"Total_Deaths = {Deaths}")
               file.write("\n")
               file.write(f"Total_Recovered = {Recovered}")
               file.write("\n")  

     message = MIMEMultipart()
     message["From"] = sender_email
     message["To"] = receiver_email
     message["Subject"] = subject
     message["Bcc"] = receiver_email 
     message.attach(MIMEText(body, "plain"))
     filename = "covid_data.txt"
     with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

     encoders.encode_base64(part)
     part.add_header(
         "Content-Disposition",
         f"attachment; filename= {filename}",
     )
     message.attach(part)
     text = message.as_string()
     context = ssl.create_default_context()

     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        print("Mail sent sucessfully")
