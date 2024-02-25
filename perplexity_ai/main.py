from google_request.scrape_google_request import ScrapeGoogle
from content_scraper.web_scrape import scrape_web_url
import time
start_time = time.time()

query1 = ScrapeGoogle()
print("--- %s seconds ---" % (time.time() - start_time))
m = 1
while m == 1:
    inp = input("Enter a query : ")
    if inp == '1':
        break
    inp_list = inp.split(" ")
    inp_query = "+".join(inp_list)
    start_time = time.time()
    url_list = query1.scrape_on_query(inp_query)
    scrape_web_url(url_list)

    print("--- %s seconds ---" % (time.time() - start_time))


