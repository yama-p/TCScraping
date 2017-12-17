# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import Detail


def nextPage(soup, css_writer):
    pagination = soup.find("div", {"class": "pagination"})

    if pagination.find("li", {"class": "next"}) == None:
        return

    next_page = pagination.find("li", {"class": "next"})
    link = next_page.find("a").get("href")
    next_url = 'https:' + link
    scraping(next_url, css_writer)


def scraping(url, css_writer):
    f = urllib2.urlopen(url)
    html = f.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    unavailables = soup.find_all("li", {"class": "unavailable"})

    for unavailable in unavailables:
        try:
            watch = unavailable.find("li", {"class": "watch"})
            ticket_status= watch.find("span", {"class": "text-muted"})

            if ticket_status.string != u"取引中":
                continue

            img = unavailable.find("li", {"class": "img"})
            detail_url = img.find("a").get("href")

            Detail.scraping(detail_url, css_writer)
        except:
            pass

    nextPage(soup, css_writer)
