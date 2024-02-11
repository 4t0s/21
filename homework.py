import asyncio
import aiohttp
import time
import requests

start = time.time()
if __name__ == '__main__':
    for i in range(1,101):
        url = f'https://jsonplaceholder.typicode.com/posts/{i}'
        response = requests.get(url)
        with open(f"main/s{i}.json", "w") as file:
            file.write(response.text)
end = time.time() - start
print(f"Time taken to download all 100 posts is {end} seconds.")
def get_data(url):
    return requests.get(url).text

async def get_data_async(url, session):
    async with session.get(url) as response:
        return await response.text()

async def parallel():
    async with aiohttp.ClientSession() as session:
        events = [get_data_async(f"https://jsonplaceholder.typicode.com/posts/{i}", session) for i in range(1,101)]
        result = await asyncio.gather(*events)
        for i, data in enumerate(result):
            with open(f"async/response_{i}.json", "w") as file:
                file.write(data)
if __name__ == "__main__":
    start = time.time()
    asyncio.run(parallel())
    print(time.time() - start)