from typing import List
from newspaper import Config,Article
import newspaper

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
config = Config()

config.browser_user_agent = user_agent
config.request_timeout = 2


def scrape_web_url(url_list: List[str]):
    return_txt = ''
    tot = 0
    for url in url_list:
        print(url,end= ' ')
        try:
            if tot > 5:
                break
            page = Article(url, config=config)
            page.download()
            page.parse()
            print(url)
            tot += 1
            return_txt += page.text
        except:
            pass
    return return_txt

