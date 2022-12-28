import mechanicalsoup
import re
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen


def open_site(url: str, decode: str = "utf-8"):
    html_page = urlopen(url)
    html_text = html_page.read().decode(decode)
    return html_text
