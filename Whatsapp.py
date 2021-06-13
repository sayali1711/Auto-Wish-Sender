from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import date

today = date.today()


d1 = today.strftime("%d/%m")
#print("d1 =", d1)
def today_Birthday():
    with open('birthdays.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
                continue

            else:
                #print(row[0])
                if(d1==row[1]):
                    return(row[0]+" "+row[1])
                else:
                    line_count += 1
                    continue
    return("NA")
birthDate=today_Birthday()
list1=birthDate.split()
#print(birthDate.split())

driver=webdriver.Chrome("D:\\pycharm_programs\\pycharm projects\\venv\\ChromeDriver\\chromedriver.exe")

driver.get("https://web.whatsapp.com/")
input("Scan the QR Code and Press any Key to Continue: ")
name=str(list1[0])
sayali=driver.find_element_by_css_selector("span[title*="+ name +"]")
#+91 78754 95664
sayali.click();
text_input=driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')


if(list1[1]==d1):
  time.sleep(10)
  text_input.send_keys('Happy Birthday'+" "+list1[0])
  text_input.send_keys(Keys.RETURN)
else:
   time.sleep(10)
   text_input.send_keys('Bye')
   text_input.send_keys(Keys.RETURN)






