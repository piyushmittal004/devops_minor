from selenium import webdriver
import time
import os

driver = webdriver.Chrome(executable_path="functional_tests/chromedriver")

driver.get('http://127.0.0.1:8000/')

assert (print(driver.title), 'Object Detection | Images')
assert (print(driver.current_url), 'http://127.0.0.1:8000/')

execution_path = os.getcwd()

driver.find_element_by_id('file_upload').send_keys(os.path.join(execution_path, "functional_tests/Image1.jpeg"))
time.sleep(5)

driver.find_element_by_id('clear').click()
time.sleep(5)

driver.find_element_by_id('file_upload').send_keys(os.path.join(execution_path, "functional_tests/Image1.jpeg"))
time.sleep(5)

driver.find_element_by_id('file_upload').send_keys(os.path.join(execution_path, "functional_tests/Image2.jpeg"))
time.sleep(5)

driver.find_element_by_id('run').click()
assert (driver.current_url, 'http://127.0.0.1:8000/result')

time.sleep(70)

driver.close()
