# StatScape Discord Bot

A Discord bot for retrieving Old School RuneScape player statistics.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory
4. Add your Discord bot token to the `.env` file:
   ```properties
   DISCORD_BOT_TOKEN=your_token_here
   ```
5. Run the bot:
   ```bash
   python bot.py
   ```

## Commands

The bot responds to the following commands:

* `!lookup <username>` - Displays a player's skill levels, experience, and ranks for all OSRS skills
* `!bosskc <username>` - Shows kill counts for all OSRS bosses the player has killed
* `!clues <username>` - Displays the number of completed clue scrolls for each difficulty
* `!commands` - Shows this list of commands

Example:
```
!lookup zezima
!bosskc woox
!clues b0aty
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
