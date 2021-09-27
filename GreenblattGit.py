
# region - IMPORTS
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import numpy as np
# endregion
# region - EXTRACTING DATA
base_url = 'https://www.sec.gov/cgi-bin/current?q1=0&q2=6&q3='
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')
sec_ticker_table = pd.read_csv('https://www.sec.gov/include/ticker.txt', delim_whitespace = True, header = None)
sec_ticker_table = pd.DataFrame(sec_ticker_table)
sec_ticker_table.columns = ['Ticker','CIK']
name_table = pd.read_csv(# insert path to cik_name file here)
name_table = pd.DataFrame(name_table)
name_table = name_table.drop(name_table.columns[0], axis = 1) 
name_table.columns = ['Name','CIK']
complete_df = pd.DataFrame(columns = ['Type','Name','CIK','Link'])

elements = soup.find_all('a')
def extraction(type_of_filing):
    master_df = pd.DataFrame(columns = ['Type','Name','CIK','Link','Spin-Off','Restructuring','Merger','Bankruptcy','Recapitalisation','Rights Offering'])
    for element in elements:
        element = str(element)
        if element[10:17] == 'Archive':
            index1 = element.index('html">')
            index2 = element.index('</a>')
            type = element[index1+6:index2]
            if type == type_of_filing:
                index5 = element.index('html')
                url = 'https://www.sec.gov' + element[9:index5+4]
                index3 = element.index('data/')
                index4 = element.index('/00')
                cik = element[index3+5:index4]
                try: 
                    ticker = sec_ticker_table.loc[sec_ticker_table['CIK'] == int(cik), 'Ticker'].iloc[0]
                except:
                    ticker = 'NO TICKER AVAILABLE'
                try:
                    name = name_table.loc[name_table['CIK'] == int(cik), 'Name'].iloc[0]
                except:
                    name = 'NO NAME AVAILABLE'
                master_append = [type,name,cik,url]
                def count_key_words(base_link):
                    http = httplib2.Http()
                    status, response = http.request(base_link)

                    links, text_links = ([] for i in range(2)) 
                    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'),features="html.parser"):
                        if link.has_attr('href'):
                            links.append((link['href']))

                    for link in links:
                        if link[-4:] == '.txt':
                            text_links.append(link)
                            if len(text_links) == 1:
                                content = text_links[0]
                            else:
                                master_append.append(np.NaN)
                                master_append.append(np.NaN)
                                return

                    url = 'https://www.sec.gov' + str(content)
                    data = urllib.request.urlopen(url).read().decode('utf-8')
                    for word in ['spin-off','restructuring','merger','bankruptcy','recapitalisation', 'rights offering']:
                            occurrences = data.count(word)
                            master_append.append(occurrences)
                count_key_words(url)
                print(master_append)
                if len(master_append) == 10:
                    master_df.loc[len(master_df)] = master_append
    
    if len(master_df) == 0:
        print('NO {} FILINGS TODAY'.format(type_of_filing))
    if len(master_df)>0:
        complete_df.append(master_df)  
        print(master_df)
        
        mail_content = """\
        <html>
            <head></head>
            <body>
            {0}
            </body>
        </html>
        """.format(master_df.to_html())
        sender_address = # insert address
        sender_pass = # insert password
        receiver_address = # insert address
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = '{}: SEC Filing'.format(type_of_filing)   
        message.attach(MIMEText(mail_content, 'html'))
        session = smtplib.SMTP('smtp.gmail.com', 587) 
        session.starttls() 
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
# endregion

filing_types = ['10-12B','10-12B/A','8-K','8-K/A','S-4','S-4/A','S-1','S-1/A','S-1MEF']
for type in filing_types:
    extraction(type)
today = datetime.datetime.today()
month = '%02d' % today.month
day = '%02d' % today.day    
complete_df.to_excel('# insert export file path with {} to make name specific'.format(today.year,month,day))
