import requests
import pyshorteners
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup as bs

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "*******************"
receiver_email = "*******************"
password = ("*******************")

for i in range(1,7):
    page_number = (i)

    url = F"https://www.ndtv.com/latest/page-{page_number}"

    response = requests.get(url)
    sh = pyshorteners.Shortener()
    soup = bs(response.text,"lxml")

    header = soup.find("div",{"class":"row s-lmr mt-10"})
    for news in header:
      title_news = news.find_all("h2",{"class":"newsHdng"})
      for heading in title_news:
         with open("news.txt", "a") as file:
          tag = heading.find("a")
          Title = tag.text
          Dev = tag["href"]
          x = sh.tinyurl.short(Dev)
          file.write(f"{Title}--{x}")
          file.write("\n") 
          print(f"{Title}--{x}")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email 
message.attach(MIMEText(body, "plain"))
filename = "news.txt"
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
