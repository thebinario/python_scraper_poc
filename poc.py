from core import *


def init_scraper1():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    # print(html)
    title_index = html.find("<title>")

    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)


def init_scraper2():
    url = "http://olympus.realpython.org/profiles/poseidon"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    start_index = html.find("<br><br>") + len("<br><br>")
    end_index = html.find("</center>")
    title = html[start_index:end_index]
    print(title)


def re_scraper():
    string = "Everything is <replaced> if it's in <tags>."
    string = re.sub("<.*?>", "ELEPHANTS", string)
    print(string)


def re_with_scraper():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)  # Remove HTML tags

    print(title)


def exercise_scraper():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    # print(html)
    start_index = html.find("Favorite Color:") + len("Favorite Color:")
    end_index = html.find("</center>")
    title = html[start_index:end_index]
    print(title.strip())


def exercise_scraper_solution():
    url = "http://olympus.realpython.org/profiles/dionysus"
    html_page = urlopen(url)
    html_text = html_page.read().decode("utf-8")

    for string in ["Name: ", "Favorite Color:"]:
        string_start_idx = html_text.find(string)
        text_start_idx = string_start_idx + len(string)

        next_html_tag_offset = html_text[text_start_idx:].find("<")
        text_end_idx = text_start_idx + next_html_tag_offset

        raw_text = html_text[text_start_idx: text_end_idx]
        clean_text = raw_text.strip(" \r\n\t")
        print(clean_text)


def exercie_with_beautifulsoup():
    base_url = "http://olympus.realpython.org"
    html_page = urlopen(base_url + "/profiles")
    html_text = html_page.read().decode("utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    for link in soup.find_all("a"):
        link_url = base_url + link["href"]
        print(link_url)


def scraper_poc():
    url = "http://olympus.realpython.org"
    page = urlopen(url + '/profiles')
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')
    for tag_a in links:
        print("{}{}".format(url, tag_a['href']))


def create_browser():
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    page = browser.get(url)
    print(page)


def open_browser_and_login():
    # 1
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    login_page = browser.get(url)
    login_html = login_page.soup

    # 2
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    # 3
    profiles_page = browser.submit(form, login_page.url)
    print(profiles_page.url)

    links = profiles_page.soup.select("a")
    links = profiles_page.soup.select("a")

    for link in links:
        address = link["href"]
        text = link.text
        print(f"{text}: {address}")


def exercise_mechanical_soup():
    env = {'user': "zeus", "pass": "ThunderDude"}
    base_url = "http://olympus.realpython.org/login"

    # 1
    browser = mechanicalsoup.Browser()
    login_page = browser.get(base_url)
    login_html = login_page.soup

    # 2
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    # 3
    profiles_page = browser.submit(form, login_page.url)
    print(profiles_page.soup.title.text)


def example_soup_select():
    browser = mechanicalsoup.Browser()
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#time")[0]
    result = tag.text

    print(f"The result of your dice roll is: {result}")


def example_with_time():
    browser = mechanicalsoup.Browser()

    for i in range(4):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select("#result")[0]
        result = tag.text
        print(f"The result of your dice roll is: {result}")
        time.sleep(10)
