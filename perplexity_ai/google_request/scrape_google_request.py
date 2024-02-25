
from .setup_browser import Browser 
from typing import List
from bs4 import BeautifulSoup
import time


class ScrapeGoogle:
    def __init__(self):
        self.browser = Browser()
    def scrape_on_query(self,query: str) -> List[str]:
        self.browser.search_on_current_tab(query)
        page_source = self.browser.scrape_current_page()
        print("Got it")
        soup = BeautifulSoup(page_source, 'html.parser')
        elements_with_class = soup.find_all(class_="yuRUbf")
        final_links = []
        for element in elements_with_class:
            if len(final_links) > 3:
                break
            first_a_tag = element.find('a')
            link = first_a_tag['href']
            final_links.append(link)
        return final_links


    def quit_browser(self):
        self.browser.quit_browser()

