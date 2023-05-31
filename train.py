from llama_index import GPTVectorStoreIndex, Document
from bs4 import BeautifulSoup
import requests
import pyppeteer
import asyncio

async def save_vector_index():
    text = await scrape_page('https://docs.servicenow.com/bundle/tokyo-procurement-operations/page/product/supplier-management/concept/supplier-central.html')
    doc = Document(text)
    index = GPTVectorStoreIndex.from_documents([doc])
    vector = index.vector_store.get_vector(doc.id)

def beautiful_soup_response(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

async def scrape_page(url):
    browser = await pyppeteer.launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)
    text = await page.content()
    await browser.close()
    # return text
    return "I am the scraped text"

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(save_vector_index())
loop.close()