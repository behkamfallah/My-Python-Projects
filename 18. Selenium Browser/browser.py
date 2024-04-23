import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser:
    def __init__(self):
        self.browser = webdriver.Chrome()  # or .Firefox()

    def open_page(self, url: str):
        print(f'Opening...')
        self.browser.get(url)

    def close_browser(self):
        print('Closing')
        self.browser.close()


if __name__ == '__main__':
    browser = Browser()
    browser.open_page('https://www.varzesh3.com')
    time.sleep(2) # Wait before closing the browser then automatically closes.
