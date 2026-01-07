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
if not url.startswith("http"):
    url = "https://" + url
driver.get(url)

links = driver.find_elements(By.TAG_NAME, "a")
results = []

for link in links:
    href = link.get_attribute("href")

    if href is None or href.startswith("javascript"):
        continue

    try:
        response = requests.get(href, timeout=5)
        status = response.status_code
    except requests.exceptions.RequestException:
        status = "ERROR"

    results.append([href, status])
    