from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google_request.scrape_google_request import ScrapeGoogle
from content_scraper.web_scrape import scrape_web_url
from RAG_analysis.rag_embedd import RAG
from groq_api.groq_request import groq_request
import time
start_time = time.time()

query1 = ScrapeGoogle()


class RequestItem(BaseModel):
    query: str

app = FastAPI()

rag1 = RAG()
rag1.initialize_db()


@app.post("/process/")
async def process_item(item: RequestItem):
    inp = item.query
    inp_list = inp.split(" ")
    inp_query = "+".join(inp_list)
    start_time = time.time()
    url_list = query1.scrape_on_query(inp_query)
    results = scrape_web_url(url_list)
    rag1.rag_embeddings(results)
    final_result = rag1.rag_search(inp)
    rag1.delete_db()
    rag1.initialize_db()
    answer = groq_request(final_result,inp)
    return {"answer":answer}


