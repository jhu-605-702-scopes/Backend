# SlingAcademy.com
# This example uses Python 3.11.4

# import the modules
import asyncio
import json
import aiohttp
from pprint import pprint
from datetime import datetime

create_user_url = "https://api.getscopes.app/v1/users/"
get_horoscope_url = "https://api.getscopes.app/v1/users/{}/horoscopes/{}"
headers = {'content-type': 'application/json'}
date = str(datetime.today().isoformat())
test_users_ids = []
test_users_horoscopes = [] 

number_of_requests = 1


# async function to make a single create user request
async def create_user(url, session):
    async with session.post(url, ssl=False, json=None, headers=headers) as response:
        status = response.status
        data = await response.json()
        print(data)
        test_users_ids.append(data["body"]["userId"])

# async function to create a single user's horoscope request
async def create_horoscope(url, session):
    full_url = get_horoscope_url.format(test_users_ids.pop(), date)
    async with session.post(full_url, ssl=False, json=None, headers=headers) as response:
        status = response.status
        data = await response.json()
        emojis = json.loads(data["body"])["emojis"]
        test_users_horoscopes.append(emojis)

# async function to make multiple requests
async def create_users(url):
    async with aiohttp.ClientSession() as session:
        tasks = [create_user(url, session) for i in range(number_of_requests)]
        results = await asyncio.gather(*tasks)
        return results

async def create_horoscopes(url):
    async with aiohttp.ClientSession() as session:
        tasks = [create_horoscope(url, session) for i in range(number_of_requests)]
        results = await asyncio.gather(*tasks)
        return results


# run the async functions
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
ids = asyncio.run(create_users(create_user_url))
pprint(test_users_ids)
horoscopes = asyncio.run(create_horoscopes(get_horoscope_url))
pprint(test_users_horoscopes)
# print the results

