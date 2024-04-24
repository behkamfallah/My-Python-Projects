import re
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--disable-gpu')

        self.browser = webdriver.Chrome(options=self.chrome_options)

    def scrape_emails(self, url: str) -> set:
        print('Scraping Emails...')
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_of_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails

    def close_browser(self):
        print('Closing')
        self.browser.close()


def main():
    print('Welcome to email scraper!')
    print('---------------------------')
    browser = Browser()
    user_input = input('Please input the website: ')
    print('---------------------------')
    emails = browser.scrape_emails(user_input)

    if len(emails) == 0:
        print('No email found.')
    else:
        for i, email in enumerate(emails, start=1):
            print(i, email, sep=': ')

    browser.close_browser()

if __name__ == '__main__':
    main()
