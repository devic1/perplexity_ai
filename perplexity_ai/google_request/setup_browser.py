from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_page_load_timeout(3)
        self.driver.get("about:blank")

    def search_on_current_tab(self,query:str):
        try:
            self.driver.get(f"https://www.google.com/search?q={query}")
        except:
            None

    def quit_browser(self):
        self.driver.quit()

    def scrape_current_page(self) -> str:
        page_source = self.driver.page_source
        return page_source
        
