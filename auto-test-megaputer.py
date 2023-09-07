
from selenium import webdriver
import unittest
import csv

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link ="https://www.megaputer.ru/produkti/sertifikat/"
browser = webdriver.Edge()
browser.get(link)

srch_string = browser.find_element(By.ID, "certificates-text")
name_info1 = "Иванова Алена"
srch_string.send_keys(name_info1)
button_find = browser.find_element(By.ID, "certificates-button").click()
try:
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "text1")))
finally:
    try:
        srch_info_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[1]').text
        srch_info2_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[2]').text
        srch_info3_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[3]').text
        try:
            srch_info4_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[1]').text
            srch_info5_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[2]').text
            try:
                srch_info6_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[1]').text
                srch_info7_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[2]').text
                print(name_info1, srch_info2_string, srch_info3_string, sep=', ')
                print(name_info1, srch_info4_string, srch_info5_string, sep=', ')
                print(name_info1, srch_info6_string, srch_info7_string, sep=', ')
            except NoSuchElementException:
                print(name_info1, srch_info4_string, srch_info5_string, sep=', ')
        except NoSuchElementException:
            print(name_info1, srch_info2_string, srch_info3_string, sep=', ')
    except NoSuchElementException:
        print(name_info1, ',', ',', sep='')

srch_string = browser.find_element(By.ID, "certificates-text").clear()

srch_string2 = browser.find_element(By.ID, "certificates-text")
name_info2 = "Петров Михаил"
srch_string2.send_keys(name_info2)
button_find2 = browser.find_element(By.ID, "certificates-button").click()
try:
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "text1")))
finally:
    try:
        srch_info1_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[1]').text
        srch_info12_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[2]').text
        srch_info13_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[3]').text
        try:
            srch_info14_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[1]').text
            srch_info15_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[2]').text
            try:
                srch_info16_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[1]').text
                srch_info17_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[2]').text
                print(name_info2, srch_info12_string, srch_info13_string, sep=', ')
                print(name_info2, srch_info14_string, srch_info15_string, sep=', ')
                print(name_info2, srch_info16_string, srch_info17_string, sep=', ')
            except NoSuchElementException:
                print(name_info2, srch_info12_string, srch_info13_string, sep=', ')
                print(name_info2, srch_info14_string, srch_info15_string, sep=', ')
        except NoSuchElementException:
            print(name_info2, srch_info12_string, srch_info13_string, sep=', ')
    except NoSuchElementException:
        print(name_info2, ',', ',', sep='')

srch_string = browser.find_element(By.ID, "certificates-text").clear()

srch_string3 = browser.find_element(By.ID, "certificates-text")
name_info3 = "Сидоров Петр"
srch_string3.send_keys(name_info3)
button_find3 = browser.find_element(By.ID, "certificates-button").click()
try:
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "text1")))
finally:
    try:
        srch_info2_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[1]').text
        srch_info22_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[2]').text
        srch_info23_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[1]/td[3]').text
        try:
            srch_info24_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[1]').text
            srch_info25_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[2]/td[2]').text
            try:
                srch_info26_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[1]').text
                srch_info27_string = browser.find_element(By.XPATH, '//*[@id="text1"]/table/tbody/tr[3]/td[2]').text
                print(name_info3, srch_info22_string, srch_info23_string, sep=', ')
                print(name_info3, srch_info24_string, srch_info25_string, sep=', ')
                print(name_info3, srch_info26_string, srch_info27_string, sep=', ')
            except NoSuchElementException:
                print(name_info3, srch_info22_string, srch_info23_string, sep=', ')
                print(name_info3, srch_info24_string, srch_info25_string, sep=', ')
        except NoSuchElementException:
            print(name_info3, srch_info22_string, srch_info23_string, sep=', ')
    except NoSuchElementException:
        print(name_info3, ',', ',', sep='')


class Test(unittest.TestCase):

    def test_write_csv_file(self):
        mData = [[name_info1, srch_info2_string, srch_info3_string], [name_info2, srch_info12_string, srch_info13_string], [name_info2, srch_info14_string, srch_info15_string], [name_info2, srch_info16_string, srch_info17_string], [name_info3, ',']]
        mFile = open('csv-sert-sotrudniki.csv', 'w')
        with mFile:
           writer = csv.writer(mFile)
           writer.writerows(mData)
