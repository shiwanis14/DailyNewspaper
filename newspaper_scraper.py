import requests
import bs4
import datetime
import smtplib

result = requests.get('https://www.careerswave.in/the-economic-times-epaper-pdf/') #this is the site I scrape from
soup = bs4.BeautifulSoup(result.text, 'lxml')
date = soup.select('div')[20].select('table')[1].select('td')[0].getText()
link = soup.select('div footable_parent_35645')

today = datetime.date.today()
today = today.strftime("%d-%m-%Y")
if date==today: #if paper has been uploaded
	email_link = soup.select('div')[20].select('table')[1].select('td')[1].getText() #scrape the link
   
	smtp_object = smtplib.SMTP('smtp.gmail.com',587)
	smtp_object.ehlo()
	smtp_object.starttls()

	from_address = '' #update these two lines
	to_address = ''

	smtp_object.login(from_address, '') #update your API key (in GMAIL)

	msg = """\
	Subject: Economic times news digest

	Here is your news for - """+ date + '\t' + email_link

	smtp_object.sendmail(from_address,to_address,msg)
	smtp_object.quit()
