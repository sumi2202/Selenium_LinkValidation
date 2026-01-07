import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import csv

options = Options()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = input("Enter the URL to check for broken links: ").strip()
driver.get(url)