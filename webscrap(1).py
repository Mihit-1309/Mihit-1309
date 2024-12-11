from operator import index
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from user_agent import generate_user_agent 
url='https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('linux'))}
page_response = requests.get(url,timeout=5, headers=headers)
webpage = requests.get(url,headers=headers).text
# print(webpage.text)
soup = BeautifulSoup(webpage,'lxml')


# sp = soup.find_all('div',class_='companyCardWrapper__interLinkingWrapper')[0].text
# print(sp.split("| ")[2])   
company = soup.find_all('div',class_="companyCardWrapper")
# print(len(company))
name=[]
work_type=[]
total_employees=[]
reviews=[]
# location=[]
salaries=[]
rating=[]
for i in company:
   try:
      name.append(i.find('h2',class_='companyCardWrapper__companyName').text.strip())
   except:
      name.append(None)   

   try:  
      work_type.append(i.find('div',class_="companyCardWrapper__interLinkingWrapper").text.strip().split("|")[0])
   except:
      work_type.append(None)

   try:   
      total_employees.append(i.find('div',class_="companyCardWrapper__interLinkingWrapper").text.strip().split("|")[1])
   except:
      total_employees.append(None)

   try:
      reviews.append(i.find('span',class_="companyCardWrapper__ActionCount").text.strip())
   except:
      reviews.append(None)
   # try:
   #    location.append(i.find('div',class_='companyCardWrapper__interLinkingWrapper').text.strip().split("|")[4])
   # except:
   #    location.append(None)
   try:
      salaries.append(i.find_all('span',class_='companyCardWrapper__ActionCount')[1].text.strip())
   except:
      salaries.append(None)
   try:
      rating.append(i.find('span',class_='companyCardWrapper__companyRatingValue').text.strip())
   except:
      rating.append(None)

df = pd.DataFrame({
   'name':name,'work_type':work_type,
   'total_employees':total_employees,
   'reviews':reviews,
   # 'location':location,
   'salaries':salaries,
   'rating':rating
})

print(df)
