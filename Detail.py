# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup


def encodeValues(v):
    if v == None:
        return ""
    else:
        v = v.encode('utf_8')
        v = v.replace('\n','')
        v = v.replace('\r','')
        return v


def scraping(url, css_writer):
    print url
    f = urllib2.urlopen(url)
    html = f.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    ticket_info = soup.find("div", {"class": "module-ticket-info"})
    trs = ticket_info.find_all("tr")

    hashtable = {}
    for tr in trs:
        try:
            th = tr.find("th")
            if tr.find("td") == None:
                hashtable[th.string] = ""
            else:
                td = tr.find("td")
                if td.find("a") == None:
                    hashtable[th.string] = td.string
                else:
                    hashtable[th.string] = td.find("a").string
        except:
            pass

    aa = map(lambda v: encodeValues(v), hashtable.values())
    css_writer.writerow(aa)
