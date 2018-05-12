import discord
from discord.ext import commands
import urllib.parse
import requests
import aiohttp



class api:
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def google(self, query):
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
       async with aiohttp.request('get', 'http://thecatapi.com/api/images/get?format=src') as resp:
            await self.bot.say(resp.url)

    @commands.command()
    async def dog(self):
        dog_api = "https://dog.ceo/api/breeds/image/random"
        json_data = requests.get(dog_api).json()
        dogimage = json_data['message']
        await self.bot.say(dogimage)
    
def setup(bot):
    bot.add_cog(api(bot))