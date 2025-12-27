import requests
from bs4 import BeautifulSoup
import smtplib
APP_PW = "Enter_Your_Gmail_App_password"
sender = "abc@gmail.com"
receiver = "abc@gmail.com"
web_url="https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_2?adgrpid=56395396742&dib=eyJ2IjoiMSJ9.LFVt-P4VfYSI0tw5J_cegcL5rvzFlm3epZovXWilTVtRxqaJSLL4Q6CYLC3Z4vdKgPcIl_tDAy360ItQo9385ys0dKiSzBTewB62RBDt-OfCa6vsL8-k6CBvClM0utQDjb814Uyxiscq7qJdVVUrvveRIy5dPG9xhXUbiF3LI0ak50-6rFStchlEX3ddJQ9L0OeuY-VCStDz4G5RTX2FKevXBc9as07fXEKxPsO-7ww.VuePED8HwG_tOox4ZqqTrQC1xkcfLvbXurkN89X3Eb8&dib_tag=se&ext_vrnc=hi&hvadid=398030525949&hvdev=c&hvlocphy=9148883&hvnetw=g&hvqmt=e&hvrand=14629057348184432078&hvtargid=kwd-761772532525&hydadcr=15007_1995193&keywords=amazon%2Bps5&mcid=c90f3a2955ef333e89d581a6c06d1a20&qid=1761315614&sr=8-2&th=1"
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
response = requests.get(web_url,headers=HEADERS)
website = response.text
soup = BeautifulSoup(website,"html.parser")
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_list = price_whole.split(",")
price_str=""
for amt in price_list:
    price_str+=amt
price= float(price_str)
if price<45500:
    subject = "AMAZON PRICE TRACKER"
    body = f"PS5 is less than 45k mannnn!!! Its shopping Time :)...Get one yours at {web_url} and begin your gaming future..."
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, APP_PW)
            server.sendmail(sender, receiver, message)
            print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)
else:
    print("Price isn't less than 45000")

