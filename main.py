from time import time
import os
import glob
import asyncio
import aiohttp


def clear_folder():
    [os.remove(f) for f in glob.glob('images/*')]


def write_image(data):
    filename = f'images/file-{int(time() * 1000)}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_content(url, session)) for _ in range(10)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    clear_folder()
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
