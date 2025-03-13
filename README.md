# StatScape Discord Bot

A Discord bot for retrieving Old School RuneScape player statistics with an interactive menu system.

## Quick Links
- [Invite Bot to Server](https://discord.com/oauth2/authorize?client_id=1348056629429403668)
- [Source Code](https://github.com/Blackberrii/StatScape)

## Features
- Interactive menu system
- Real-time OSRS stats lookup
- Boss kill counts with pagination
- Clue scroll completions
- Minigame scores
- OSRS emojis

## Commands
The bot uses a simple command system:
- `!lookup <username>` - Opens an interactive menu showing:
  - Skills (levels, XP, and ranks)
  - Boss KC (paginated kill counts)
  - Clue Scrolls (all difficulty tiers)
  - Minigame Scores

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/blackberrii/StatScape.git
cd StatScape
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment:
```bash
cp .env.example .env
# Edit .env and add your Discord bot token
```

4. Run the bot:
```bash
python bot.py
```

## Deployment Options

### Docker (Recommended)
```bash
# Build image
docker build -t statscape-bot .

# Run container
docker run -d \
  --name statscape-bot \
  --restart always \
  --env-file .env \
  statscape-bot
```

### Oracle Cloud (Free Tier)
1. Set up an Oracle Cloud instance using the provided setup script:
```bash
chmod +x oracle-setup.sh
./oracle-setup.sh
```

2. Monitor the deployment:
```bash
sudo systemctl status statscape
docker logs statscape-bot
```

For detailed Oracle Cloud setup instructions, see [ORACLE_SETUP.md](ORACLE_SETUP.md)

## Development

### Requirements
- Python 3.8+
- Discord.py 2.0+
- aiohttp 3.8.0+
- python-dotenv

### Environment Variables
- `DISCORD_BOT_TOKEN` - Your Discord bot token (required)

### Docker Commands
```bash
# Rebuild container
./deploy.sh

# View logs
docker logs statscape-bot

# Restart bot
docker restart statscape-bot
```

## Support
- Found a bug? [Open an issue](https://github.com/Blackberrii/StatScape/issues)

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Credits
- All OSRS-related assets and data belong to [Jagex Ltd](https://www.jagex.com/)
- Custom emoji assets from [OSRS Wiki](https://oldschool.runescape.wiki/)
