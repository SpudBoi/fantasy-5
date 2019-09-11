#Author: Conor Muldoon

#importing necessary packages
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime

def append_data(entries, current_entry, weekday_index):
    #this list will hold our data and entry count
    data = []
    entry_count = entries
    entry_iteration = current_entry
    date_index = 2

    weekdays = ['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.']

    driver = webdriver.Chrome()
    driver.get("https://www.lotterycorner.com/ca/fantasy-5/2019")

    for i in range(entry_count):
        #add the first two columns to the row
        row = [entry_iteration, weekdays[weekday_index]]

        #extracting date
        date_xpath = "/html/body/div[3]/div/div/div/div[1]/div[3]/table/tbody/tr[" + str(date_index) + "]/td[1]"
        date = driver.find_element_by_xpath(date_xpath).text

        #splitting and extracting
        date_array = date.split(" ")
        month = date_array[0]
        year = date_array[2]

        #day number formatting
        if date_array[1][0] == "0":
            day = date_array[1][1]
        else:
             day = date_array[1][0:2]

        #adding the date data to the row
        row.append(month)
        row.append(day)
        row.append(year)

        #extracting number data and adding to the row
        for j in range(5):
            number_xpath = "/html/body/div[3]/div/div/div/div[1]/div[3]/table/tbody/tr[" + str(date_index) + "]/td[2]/ul/li[" + str((j+1)) + "]"
            number = driver.find_element_by_xpath(number_xpath).text
            row.append(int(number))

        data.append(row)

        #updating drawing number and weekday
        date_index = date_index + 1
        entry_iteration = entry_iteration - 1
        if weekday_index == 0:
            weekday_index = 6
        else:
            weekday_index = weekday_index - 1

    data = data[::-1]

    with open('C:\\Users\\ConMa\\Documents\\Projects\\fantasy-5\\fantasy5.csv', mode='a') as csv_file:

        #declaring the writer
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in data:
            writer.writerow(row)

    print("Database has been updated!")


def get_current_draw():
    #opening driver and navigating to fantasy 5 page
    driver = webdriver.Chrome()
    driver.get("https://www.calottery.com/play/draw-games/fantasy-5")

    #locating and returning the current draw number
    draw = driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div[1]/h3").text[-4:]
    driver.quit()
    return draw


#opening our database in read mode here
with open('C:\\Users\\ConMa\\Documents\\Projects\\fantasy-5\\fantasy5.csv', mode='r', encoding='UTF-8') as csv_file:

    #opening a reader
    reader = csv.reader(csv_file, delimiter=',')

    #converting the output stream into a list and finding total rows
    rows = list(reader)
    tot_rows = len(rows)

    #finding the draw number of the last entry
    last_draw_entry = rows[-2][0]

#current draw number
curr = get_current_draw()
#how many entries are required
required_entries = int(curr) - int(last_draw_entry)
#weekday index
index = datetime.datetime.today().weekday()


if required_entries > 0:
    append_data(required_entries, int(curr), index)
else:
    print("Database is up to date!")
