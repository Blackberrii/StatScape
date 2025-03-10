import discord
from discord.ext import commands
import aiohttp
import asyncio
from dotenv import load_dotenv
import os
from aiohttp import web
from discord.ui import View, Button, button
import discord.ui

# Initialize environment and bot setup
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')
if not bot_token:
    raise ValueError("No Discord bot token provided. Set the DISCORD_BOT_TOKEN environment variable.")

# Set up bot with message content intent for command handling
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Custom emoji mappings for OSRS skills and bosses
skill_emojis = {
    "Overall": "<:overall_icon:1348081702244978750>",
    "Attack": "<:Attack_icon:1348081351978520616>",
    "Defence": "<:Defence_icon:1348081305618878577>",
    "Strength": "<:Strength_icon:1348081058243149925>",
    "Hitpoints": "<:Hitpoints_icon:1348081226321231872>",
    "Ranged": "<:Ranged_icon:1348081146738507776>",
    "Prayer": "<:Prayer_icon:1348081188866228366>",
    "Magic": "<:Magic_icon:1348081202468356157>",
    "Cooking": "<:Cooking_icon:1348081329056514090>",
    "Woodcutting": "<:Woodcutting_icon:1348080937531080744>",
    "Fletching": "<:Fletching_icon:1348081243878723696>",
    "Fishing": "<:Fishing_icon:1348081272668426340>",
    "Firemaking": "<:Firemaking_icon:1348081282973700208>",
    "Crafting": "<:Crafting_icon:1348081317144821760>",
    "Smithing": "<:Smithing_icon:1348081072608383077>",
    "Mining": "<:Mining_icon:1348081200522199167>",
    "Herblore": "<:Herblore_icon:1348081235162824744>",
    "Agility": "<:Agility_icon:1348081371217789019>",
    "Thieving": "<:Thieving_icon:1348081012164395120>",
    "Slayer": "<:Slayer_icon:1348081120947867720>",
    "Farming": "<:Farming_icon:1348081293099012136>",
    "Runecrafting": "<:Runecraft_icon:1348081134025703424>",
    "Hunter": "<:Hunter_icon:1348081217010008235>",
    "Construction": "<:Construction_icon:1348081340247052339>"
}

# Boss emojis mapping (leave unchanged)
boss_emojis = {
    "Abyssal Sire": "<:abbysire:1348091624634191942>",
    "Alchemical Hydra": "<:alchhydra:1348091680842186894>",
    "Artio": "<:artio:134809151534797343>",
    "Barrows Chests": "<:barrows:1348091362687320114>",
    "Bryophyta": "<:bryophyta:1348090986403987456>",
    "Callisto": "<:callisto:1348091564651446332>",
    "Calvar'ion": "<:calvar:1348091534079299624>",
    "Cerberus": "<:cerbe:1348091641289773066>",
    "Chambers of Xeric": "<:cox:1348091706154814144>",
    "Chambers of Xeric: Challenge Mode": "<:cox:1348091706154811414>",  # Using the same icon for hard mode
    "Chaos Elemental": "<:chaosele:1348091483764424704>",
    "Chaos Fanatic": "<:chaosfan:1348091512734351360>",
    "Commander Zilyana": "<:zily:1348091225835569313>",
    "Corporeal Beast": "<:corpbeast:1348091207267520664>",
    "Crazy Archaeologist": "<:crazyarch:1348091525430775818>",
    "Dagannoth Prime": "<:dagprime:1348091085791952949>",
    "Dagannoth Rex": "<:dagrex:1348091098186256423>",
    "Dagannoth Supreme": "<:dagsupreme:1348091108160311436>",
    "Deranged Archaeologist": "<:derangedarch:1348091057086271499>",
    "General Graardor": "<:grrar:1348091234811641876>",
    "Giant Mole": "<:giantmole:1348091045422043177>",
    "Grotesque Guardians": "<:grotesque:1348091615322963998>",
    "Hespori": "<:hespori:1348091001369264221>",
    "Kalphite Queen": "<:kalqueen:1348091077428514856>",
    "King Black Dragon": "<:kingbd:1348091068486254692>",
    "Kraken": "<:kraken:1348091632959885383>",
    "Kree'Arra": "<:kreearra:1348091217354821722>",
    "K'ril Tsutsaroth": "<:kril:1348091244856999936>",
    "Mimic": "<:mimic:1348091010777088053>",
    "Nex": "<:nex:1348091262464557178>",
    "Nightmare": "<:nightmare:1348091180750995548>",
    "Phosani's Nightmare": "<:phosanis:134809119124211974>",
    "Obor": "<:obor:1348088654735872052>",
    "Sarachnis": "<:sarachnes:1348091115802202223>",
    "Scorpia": "<:scorpia:1348091503481982987>",
    "Skotizo": "<:skotizo:1348091019777806356>",
    "Tempoross": "<:tempoross:1348091464630009918>",
    "The Gauntlet": "<:gauntlet:1348091377325576315>",
    "The Corrupted Gauntlet": "<:corruptedgaunt:1348091421252517962>",
    "Theatre of Blood": "<:tob:1348091697980117022>",
    "Theatre of Blood: Hard Mode": "<:tob:1348091697980117022>",  # Using the same icon for hard mode
    "Thermonuclear Smoke Devil": "<:thermy:1348091667902894192>",
    "Tombs of Amascut": "<:tombsofamascut:1348091689901083522>",
    "Tombs of Amascut: Expert Mode": "<:toahard:1348091742108385330>",  # Using the provided icon for hard mode
    "TzKal-Zuk": "<:inferno:1348091435697573948>",
    "TzTok-Jad": "<:fightcave:1348091388193017877>",
    "Vardorvis": "<:vard:1348091352574853171>",
    "Venenatis": "<:venenatis:1348091576177397810>",
    "Vet'ion": "<:vetion:1348091604921094195>",
    "Vorkath": "<:vorkath:1348091172047949926>",
    "Wintertodt": "<:wintertodt:1348091474323181568>",
    "Zalcano": "<:zalcano:1348091492941434941>",
    "Zulrah": "<:zulrah:1348091159494525028>"
}

# List of bosses to track
bosses = [
    "Barrows Chests", "Bryophyta", "Callisto", "Cerberus", "Chaos Elemental", "Chaos Fanatic",
    "Commander Zilyana", "Corporeal Beast", "Crazy Archaeologist", "Dagannoth Prime",
    "Dagannoth Rex", "Dagannoth Supreme", "Deranged Archaeologist", "General Graardor",
    "Giant Mole", "Grotesque Guardians", "Hespori", "Kalphite Queen", "King Black Dragon",
    "Kraken", "Kree'Arra", "K'ril Tsutsaroth", "Mimic", "Nightmare", "Obor",
    "Sarachnis", "Scorpia", "Skotizo", "Tempoross", "The Gauntlet", "The Corrupted Gauntlet",
    "Theatre of Blood", "Theatre of Blood: Hard Mode", "Thermonuclear Smoke Devil",
    "TzKal-Zuk", "TzTok-Jad", "Venenatis", "Vet'ion", "Vorkath", "Wintertodt", "Zalcano", "Zulrah"
]

async def get_osrs_data(player_name):
    """Fetches player statistics from OSRS hiscores API
    
    Args:
        player_name (str): RuneScape username to look up
        
    Returns:
        dict: Player's hiscores data if found, None if player doesn't exist
    """
    url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={player_name}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.json()

class StatsView(View):
    def __init__(self, player_name: str):
        super().__init__(timeout=180)  # 3 minute timeout
        self.player_name = player_name
        self.current_page = 0
        self.boss_chunks = []

    @button(label="Skills", style=discord.ButtonStyle.primary)
    async def skills_button(self, interaction: discord.Interaction, button: Button):
        data = await get_osrs_data(self.player_name)
        if not data:
            await interaction.response.send_message(f"Could not retrieve data for {self.player_name}.", ephemeral=True)
            return

        embed = discord.Embed(title=f"{self.player_name}'s OSRS Stats", color=discord.Color.green())
        embed.set_thumbnail(url="https://oldschool.runescape.wiki/images/Skills_icon.png?a8e9f")

        for skill_data in data['skills']:
            skill_name = skill_data['name']
            if skill_name in skill_emojis:
                emoji = skill_emojis[skill_name]
                rank = skill_data['rank']
                level = skill_data['level']
                experience = skill_data['xp']
                
                formatted_experience = f"{int(experience):,}" if isinstance(experience, (int, float)) else "N/A"
                formatted_rank = f"{int(rank):,}" if isinstance(rank, (int, float)) else "N/A"
                
                embed.add_field(
                    name=f"{emoji} {skill_name}",
                    value=f"**Level**: {level}\n**XP**: {formatted_experience}\n**Rank**: {formatted_rank}",
                    inline=True
                )

        await interaction.response.edit_message(embed=embed, view=self)

    @button(label="Boss KC", style=discord.ButtonStyle.primary)
    async def bosskc_button(self, interaction: discord.Interaction, button: Button):
        data = await get_osrs_data(self.player_name)
        if not data:
            await interaction.response.send_message(f"Could not retrieve data for {self.player_name}.", ephemeral=True)
            return

        valid_boss_data = []
        for activity in data['activities']:
            boss_name = activity['name']
            if boss_name in boss_emojis:
                valid_boss_data.append((boss_name, activity['score']))

        if not valid_boss_data:
            await interaction.response.send_message(f"No boss data found for {self.player_name}.", ephemeral=True)
            return

        self.boss_chunks = [valid_boss_data[i:i + 8] for i in range(0, len(valid_boss_data), 8)]
        embed = self.create_boss_embed()
        
        # Add navigation buttons if needed
        if len(self.boss_chunks) > 1:
            self.add_item(Button(label="Previous", custom_id="prev_page", style=discord.ButtonStyle.secondary))
            self.add_item(Button(label="Next", custom_id="next_page", style=discord.ButtonStyle.secondary))

        await interaction.response.edit_message(embed=embed, view=self)

    @button(label="Clue Scrolls", style=discord.ButtonStyle.primary)
    async def clues_button(self, interaction: discord.Interaction, button: Button):
        data = await get_osrs_data(self.player_name)
        if not data:
            await interaction.response.send_message(f"Could not retrieve data for {self.player_name}.", ephemeral=True)
            return

        embed = discord.Embed(title=f"{self.player_name}'s Clue Scroll Counts", color=discord.Color.blue())
        embed.set_thumbnail(url="https://oldschool.runescape.wiki/images/thumb/Clue_scroll.png/300px-Clue_scroll.png")

        valid_clue_data = []
        for activity in data['activities']:
            clue_name = activity['name']
            if 'clue_scrolls' in clue_name.lower():
                valid_clue_data.append((clue_name, activity['score']))

        for clue_name, count in valid_clue_data:
            embed.add_field(name=clue_name, value=f"**Count**: {count}", inline=True)

        await interaction.response.edit_message(embed=embed, view=self)

    def create_boss_embed(self):
        embed = discord.Embed(
            title=f"{self.player_name}'s Boss Kill Counts (Page {self.current_page + 1} of {len(self.boss_chunks)})",
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(url="https://oldschool.runescape.wiki/images/Slayer_icon_%28detail%29.png?a4903")

        chunk = self.boss_chunks[self.current_page]
        for boss, kc in chunk:
            embed.add_field(name=f"{boss_emojis.get(boss, '')} {boss}", value=f"**Kill Count**: {kc}", inline=True)
        
        return embed

    @button(custom_id="prev_page")
    async def prev_page(self, interaction: discord.Interaction, button: Button):
        if self.current_page > 0:
            self.current_page -= 1
            embed = self.create_boss_embed()
            await interaction.response.edit_message(embed=embed, view=self)

    @button(custom_id="next_page")
    async def next_page(self, interaction: discord.Interaction, button: Button):
        if self.current_page < len(self.boss_chunks) - 1:
            self.current_page += 1
            embed = self.create_boss_embed()
            await interaction.response.edit_message(embed=embed, view=self)

# Replace the existing command handlers with a single stats command
@bot.command(name="lookup")
async def lookup(ctx, player_name: str):
    """Shows the main menu for player statistics"""
    embed = discord.Embed(
        title=f"OSRS Stats Menu - {player_name}",
        description="Click a button below to view different statistics:",
        color=discord.Color.blue()
    )
    embed.add_field(name="Available Stats", value="• Skills\n• Boss Kill Counts\n• Clue Scrolls", inline=False)
    embed.set_thumbnail(url="https://oldschool.runescape.wiki/images/Stats_icon.png?b4e0c")
    
    view = StatsView(player_name)
    await ctx.send(embed=embed, view=view)

@lookup.error
async def lookup_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Please provide a username. Example: `!lookup zezima`")

# Cloud Run health check server
async def handle_health_check(request):
    """Health check endpoint for Cloud Run"""
    return web.Response(text="OK", status=200)

async def start_server():
    """Starts the health check server required by Cloud Run"""
    app = web.Application()
    app.router.add_get("/", handle_health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", "8080"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Health check server running on port {port}")

# Main bot startup
async def start_bot():
    """Initializes both the health check server and Discord bot"""
    await start_server()
    await bot.start(bot_token)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
