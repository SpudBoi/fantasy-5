#Author: Conor Muldoon

#importing necessary packages
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import date

with open('C:\\Users\\ConMa\\Documents\\Projects\\fantasy-5\\fantasy5.csv', mode='w') as csv_file:

    #setting column names
    fieldnames = ['draw', 'weekday', 'month', 'day', 'year', 'num1', 'num2', 'num3', 'num4', 'num5']

    #declaring the writer
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #column headers are written
    writer.writerow(fieldnames)
