import discord
from discord.ext import commands
from os import system
import string

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

isVulnerable = False
whitelisted = string.ascii_letters + string.digits + '.' # characters allowed in IPs or domains

# displays the help file
@bot.command()
async def helpme(ctx):
    with open('help.txt', 'r') as helpme:
        await ctx.send(helpme.read())

# switches the bot's vulnerability status
@bot.command()
async def switchvuln(ctx):
    global isVulnerable
    isVulnerable = not isVulnerable
    await ctx.send(f'Vulnerability set to {isVulnerable}.')


@bot.command()
async def ping(ctx, ip):
    # if not vulnerable, check for invalid pings
    if not isVulnerable:
        if any(c not in whitelisted for c in ip):
            await ctx.send('Invalid IP or domain name, please try again.')
            return
    
    # execute ping command, also executes injections if present
    system(f'ping {ip} > pingout.txt')
    try:
        with open('pingout.txt', 'r') as pingout:
            await ctx.send(pingout.read())
    except FileNotFoundError:
        await ctx.send('Command produced no output. Please try again')
    else:
        system(f'del pingout.txt')

# handles missing ping parameter
@ping.error
async def pingerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Parameter: IP')

# run bot
token = ''
try:
    # include your bot token in file token.txt in same directory
    with open('token.txt', 'r') as tokenfile:
        token = tokenfile.readline()
    bot.run(token)
except FileNotFoundError:
    print('Token file token.txt not found, cannot run bot.')
except:
    print("Failed to launch bot. Please check your bot token.")