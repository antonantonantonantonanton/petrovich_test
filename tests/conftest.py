import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    #options.add_argument('--window-size=1650,900') #Можно задать определенный размер окна
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver.maximize_window()
    url = 'https://moscow.petrovich.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    #driver.delete_all_cookies()
    yield driver
    driver.quit()



