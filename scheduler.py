from time import sleep
from db import select_all_hubs
from main import start_parsing, parse_hub

import asyncio


while True:
    HUBS = [f'https://habr.com/ru/hubs/{hub}/articles/' for hub in select_all_hubs()]
    data = [parse_hub(hub) for hub in HUBS]
    start_parsing(data)
    asyncio.run(start_parsing(data))
    sleep(600)

