import time
import string
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


browser = webdriver.Chrome('C:/chromedriver.exe')
browser.implicitly_wait(10)
username = ('dk.testermail.qa@gmail.com')
password = ('123123Test!')
num_of_msgs = 15
num_of_string = 10

def login():
    browser.maximize_window()
    browser.get('https://mail.google.com/')
    email_field = browser.find_element_by_id('identifierId')
    email_field.clear()
    email_field.send_keys(username)
    browser.find_element_by_id('identifierNext').click()
    password_field = browser.find_element_by_name('password')
    password_field.clear()
    password_field.send_keys(password)
    browser.find_element_by_id('passwordNext').click()


def t(chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for symbol in range(num_of_string))

def send_mail(adress, subject, text):
    browser.find_element_by_css_selector('div.T-I.T-I-KE.L3').click()
    browser.find_element_by_name('to').send_keys(adress)
    browser.find_element_by_name('subjectbox').send_keys(subject)
    message_field = browser.find_element_by_css_selector('div.Am.Al.editable.LW-avf')
    message_field.click()
    message_field.send_keys(text)
    time.sleep(3)
    browser.find_element_by_css_selector('div.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3').click()

def get_recent_messages(n):
    browser.find_element_by_css_selector('table.F.cf.zt tr').click()
    mails = collect_message()
    for i in range(n - 1):
        next_mail()
        mails.update(collect_message())
    return mails

def next_mail():
    for i in range(num_of_string):
        try:
            browser.find_element_by_css_selector('div.T-I.J-J5-Ji.adg.T-I-awG.T-I-ax7.T-I-Js-Gs.L3').click()
            break
        except StaleElementReferenceException:
            pass
    else:
        raise Exception("Can`t click next email button")

def collect_message():
    for collecting_messages in range(num_of_string):
        subject = browser.find_element_by_css_selector('h2.hP').text
        if subject:
            break
        time.sleep(0.1)
    else:
        raise Exception("Unable to extract message subject and text")
    return {subject: browser.find_element_by_css_selector('div.ii.gt').text}

def summary_message(messages):
    return "\n".join(final_message(*m) for m in messages.items())


def final_message(subject, text):
    letters = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    return "Recived mail on theme {subject} with message: {text}. " \
            "It contains {letters} letters and {digits} numbers".format(letters = letters, digits = digits, subject = subject, text = text)

def deleting():
    for delete in range(num_of_msgs):
        browser.get('https://mail.google.com/mail/u/0/#inbox')
        browser.find_element_by_css_selector('table.F.cf.zt tr').click()
        next_mail()
        time.sleep(3)
        browser.find_element_by_xpath("//div[@class='iH bzn']//div[@class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA']//div[@class='asa']").click()


login()
for sending_mails in range(num_of_msgs):
    send_mail(username, t(), t())
    time.sleep(1)
messages = get_recent_messages(num_of_msgs)
send_mail(username, "Mailbox summary", summary_message(messages))
deleting()



