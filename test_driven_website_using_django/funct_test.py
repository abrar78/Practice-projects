from selenium import webdriver
browser=webdriver.Firefox(executable_path='/home/abrar/Desktop/Abrar/test_driven_website_using_django/geckodriver')
browser.get('http://localhost:8000')

assert browser.page_source.find('install')