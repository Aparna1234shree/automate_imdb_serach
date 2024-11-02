import pytest
from selenium import webdriver
from configuration import config as path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = None
imdb_url = "https://www.imdb.com/search/name/"

@pytest.fixture(scope="class")
def chrome_driver(request):
    # Setup Chrome driver using webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(imdb_url)
    request.cls.driver = driver  # Store the driver instance, not the URL

    yield driver
    # Teardown Chrome driver
    driver.quit()
