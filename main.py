import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

HUBS = [
    "https://habr.com/ru/hubs/infosecurity/articles/",
    "https://habr.com/ru/hubs/python/articles/"
]

ARTICLES = {}


async def send_request(url) -> str:
    connector = aiohttp.TCPConnector(limit=50)
    async with aiohttp.ClientSession(trust_env=True, connector=connector) as session:
        try:
            async with session.get(url) as resp:
                return await resp.text(encoding='utf-8')
        except aiohttp.ServerDisconnectedError as err:
            print(err)
        except aiohttp.ClientConnectorError as err:
            print(err)


async def parse_hub(category_url):
    html_response = await send_request(url=category_url)
    soup = BeautifulSoup(html_response, "lxml")
    pagination_block = soup.find("div", class_="tm-pagination__pages")
    pages_count = pagination_block.find_all('a', class_='tm-pagination__page')[-1].text.strip()
    print(f"category: {category_url} | pages: {pages_count}")

    for page in range(1, int(pages_count)):
        page_response = await send_request(
            url=f"{category_url}page{page}",
        )
        try:
            page_soup = BeautifulSoup(page_response, "lxml")
        except Exception as err:
            print(err)
        articles = page_soup.find_all("article")

        for article in articles:
            info_block = article.find("a", class_="tm-title__link")
            title = info_block.find("span").text.strip()
            id = int(info_block.get("href").split("/")[-2])
            link = f"https://habr.com{info_block.get('href')}"
            try:
                author_link = 'https://habr.com' + article.find('a', class_='tm-user-info__username').get('href')
                authorName = author_link.split('/')[-2]
            except AttributeError:
                author_link = None
                authorName = None
            time = article.find('time').get('datetime')
            hub_name = category_url.split("/")[-3]

            result = {'Hub': hub_name,
                      'Title': title,
                      "Author's Name": authorName,
                      "Author's Link": author_link,
                      'Time': time,
                      'Link': link}

            if id in ARTICLES:
                continue
            else:
                ARTICLES[id] = result

    # with open("dict_articles.json", "w", encoding='utf-8') as file:
    #     json.dump(ARTICLES, file, sort_keys=False, indent=4, ensure_ascii=False)
    #
    # print(ARTICLES)


async def main():
    data = [parse_hub(hub) for hub in HUBS]
    await asyncio.gather(*data)


if __name__ == "__main__":
    asyncio.run(main())
    with open("dict_articles.json", "w", encoding='utf-8') as file:
        json.dump(ARTICLES, file, sort_keys=False, indent=4, ensure_ascii=False)
