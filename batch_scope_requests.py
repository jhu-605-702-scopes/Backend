# SlingAcademy.com
# This example uses Python 3.11.4

# import the modules
import asyncio
import json
import aiohttp
from pprint import pprint
from datetime import datetime

class BatchScopeRequests: 

    def __init__(self, number_of_requests, create_user_url, create_horoscope_url) -> None:
        self.number_of_requests = number_of_requests
        self.create_user_url = create_user_url # "https://api.getscopes.app/v1/users/"
        self.create_horoscope_url = create_horoscope_url # "https://api.getscopes.app/v1/users/{}/horoscopes/{}"
        self.headers = {'content-type': 'application/json'}
        self.date = str(datetime.today().isoformat())
        self.test_users_ids = []
        self.test_users_horoscopes = [] 

    # async function to make a single create user request
    async def create_user(self, url, session):
        async with session.post(url, ssl=False, json={"username": "DeleteThisUser"}, headers=self.headers) as response:
            status = response.status
            data = await response.json()
            print(data)
            self.test_users_ids.append(data["body"]["userId"])

    # async function to create a single user's horoscope request
    async def create_horoscope(self, url, session):
        full_url = self.create_horoscope_url.format(self.test_users_ids.pop(), self.date)
        async with session.post(full_url, ssl=False, json=None, headers=self.headers) as response:
            status = response.status
            data = await response.json()
            emojis = json.loads(data["body"])["emojis"]
            self.test_users_horoscopes.append(emojis)

    # async function to make multiple requests
    async def create_users(self, url):
        async with aiohttp.ClientSession() as session:
            tasks = [self.create_user(url, session) for i in range(self.number_of_requests)]
            results = await asyncio.gather(*tasks)
            return results

    async def create_horoscopes(self, url):
        async with aiohttp.ClientSession() as session:
            tasks = [self.create_horoscope(url, session) for i in range(self.number_of_requests)]
            results = await asyncio.gather(*tasks)
            return results


    async def get_user_ids(self):
        ids = asyncio.run(self.create_users(self.create_user_url))
        pprint(self.test_users_ids)

    async def get_user_horoscopes(self):
        horoscopes = asyncio.run(self.create_horoscopes(self.create_horoscope_url))
        pprint(self.test_users_horoscopes)

