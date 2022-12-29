from core import *
from time import sleep

base_url = 'https://www.python.org/downloads/'


def main():
    browser = mechanicalsoup.Browser()
    page = browser.get(base_url)
    print(page.soup.select('div.download-unknown p a')[0].text)


if __name__ == '__main__':
    main()
