# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:48:01 2022

@author: Gururaja Hegde V'
"""

from bs4 import BeautifulSoup
import requests

html_txt=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup= BeautifulSoup(html_txt, 'lxml')
jobs=soup.find_all('li',class_ ='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_Date = job.find('span',class_ = 'sim-posted').span.text
    if 'few' in published_Date:
        company_name=job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_ = 'srp-skills').text.replace(' ','')
        print(f'''
              Company Name: {company_name}
              Required Skills: {skills}
             ''')
    
    