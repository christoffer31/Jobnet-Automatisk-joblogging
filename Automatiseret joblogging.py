#Automatiseret Automatiseret jobblog

import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriverpath = os.getcwd() + "/chromedriver.exe"
browser = webdriver.Chrome(chromedriverpath)

#username
username ='user'
#password
password ='123'

def site_login():
    browser.get('https://job.jobnet.dk/CV/frontpage')
    
    #Accepts cookie alert
    time.sleep(3) #time for the alert to appear
    browser.find_element_by_class_name('coi-banner__accept').click()
    
    #Login to Jobnet
    browser.find_element_by_id('JobnetUsername').send_keys(username)
    browser.find_element_by_id('JobnetPassword').send_keys(password)
    browser.find_element_by_id('LoginButton').click()
    
site_login()

#View Joblog ##Her kommer jeg til at sammenligne data
def joblog():
    browser.get('https://job.jobnet.dk/cv/jobseeking/joblog')  

def logjobs():
    browser.get('https://job.jobnet.dk/cv/jobseeking/joblog/detail') 
    
logjobs()


#Job specifications
Stilling = 'Scrum Master'
Virksomhedsnavn = 'Nykredit'
Nordjylland = '1'
Område = Nordjylland
today = False
date = '10-07-2020'
Autosave = False

def send_text():
    #Stilling text
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-job/jn-details-container/div/fieldset/div/div[1]/jn-form-typeahead-occupations/div/jn-typeahead-reactive-occupations/input").send_keys(Stilling)
    #Virksomhedsnavn
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-workspace/jn-details-container/div/fieldset/div[1]/div[1]/jn-form-text/div/input").send_keys(Virksomhedsnavn)
time.sleep(5)
send_text()

def set_page():
    #Hverken by eller post check
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-workspace/jn-details-container/div/fieldset/div[1]/div[4]/jn-form-checkbox/span/input").click()
    #Om jobsøgning: vælgt søgt job
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-application/jn-details-container/div/fieldset/fieldset[1]/div[1]/div[2]/jn-radio-button/span/label").click()
    #Hvordan fandt du jobbet: Opslået stilling
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-application/jn-details-container/div/fieldset/fieldset[2]/div/div[1]/jn-radio-button/span/label").click()
    #Hvordan søger du jobbet:digitalt
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-application/jn-details-container/div/fieldset/fieldset[3]/div/div[1]/jn-radio-button/span/label").click()
    #Om arbejdspladsen: vælg område
    select_område = Select(browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-workspace/jn-details-container/div/fieldset/div[2]/div/jn-form-select/div/select"))
    select_område.select_by_value(Område)
    
set_page()

#set date
def set_date():
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-application/jn-details-container/div/fieldset/fieldset[1]/div[3]/div/jn-form-datepicker/div/jn-datepicker-reactive/div/input").clear()
    browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-application/jn-details-container/div/fieldset/fieldset[1]/div[3]/div/jn-form-datepicker/div/jn-datepicker-reactive/div/input").send_keys(date)

if not today == True:
    set_date()
    
#Save log
def gemlog():
     browser.find_element_by_xpath("/html/body/div[6]/jn-root/jn-layout-main/section/main/article/jn-jobseeking-detail/jn-page/jn-form/form/jn-details-control/nav/button").click()

if Autosave == True:
    gemlog()

#kør igen

Stilling = 'Ejndoms analytikker'
Virksomhedsnavn = 'Nykredit'

def again():
    logjobs()
    time.sleep(5)
    send_text()
    set_page()
    if not today == True:
        set_date()
    if Autosave == True:
        gemlog()
        
again()
    

