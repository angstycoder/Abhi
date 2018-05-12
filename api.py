import discord
from discord.ext import commands
import urllib.parse
import requests
import aiohttp
import urbandictionary as ud


class api:
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def google(self, query):
        """Search Google Maps for info on a location"""
        g_api = "http://maps.googleapis.com/maps/api/geocode/json?"
        url = g_api + urllib.parse.urlencode({'address': query})
        json_data = requests.get(url).json()
        formatted_address=json_data['results'][0]['formatted_address']
        sat1=json_data['results'][0]['geometry']['location']['lat']
        sat2 = json_data['results'][0]['geometry']['location']['lng']
        info = discord.Embed(title=query, color=0xefefef)
        info.add_field(name="\u200b", value=formatted_address, inline=False)
        info.add_field(name="\u200b", value="Lat:"+str(sat1), inline=False)
        info.add_field(name="\u200b", value="Lng:"+str(sat2), inline=False)
        await self.bot.say(embed=info)
    @commands.command()
    async def cat(self):
       """generate random cat image"""
       async with aiohttp.request('get', 'http://thecatapi.com/api/images/get?format=src') as resp:
            await self.bot.say(resp.url)

    @commands.command()
    async def dog(self):
        """generate random dog image"""
        dog_api = "https://dog.ceo/api/breeds/image/random"
        json_data = requests.get(dog_api).json()
        dogimage = json_data['message']
        await self.bot.say(dogimage)

    @commands.command()
    async def ud(self,word):
        """Get Urban Dictionary defenition [beta]"""
        defs = ud.define(word)
        for d in defs:
            await self.bot.say(d)
    @commands.command()
    async def udran(self):
        """Get a random Urban Dictionary defenition [beta]"""
        rand = ud.random()
        for d in rand:
            await self.bot.say(d)
def setup(bot):
    bot.add_cog(api(bot))
