# StatScape Discord Bot

A Discord bot for retrieving Old School RuneScape player statistics like leaderboard stats, boss killcounts and clue scrolls completed.

[Invite link:](https://discord.com/oauth2/authorize?client_id=1348056629429403668)



(if the button above does not work:)
https://discord.com/oauth2/authorize?client_id=1348056629429403668

## Setup for personal usage

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

* `!commands` - Shows this list of commands
* `!lookup <username>` - Displays a player's skill levels, experience, and ranks for all OSRS skills
* `!bosskc <username>` - Shows kill counts for all OSRS bosses the player has killed
* `!clues <username>` - Displays the number of completed clue scrolls for each difficulty

Example:
```
!lookup zezima
!bosskc woox
!clues b0aty
```

## Cloud Deployment for personal usage

To deploy on Google Cloud Run:

1. Install Google Cloud CLI
2. Login to Google Cloud:
   ```bash
   gcloud auth login
   ```
3. Set your project:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```
4. Build and deploy:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/statscape-bot
   gcloud run deploy statscape-bot \
     --image gcr.io/YOUR_PROJECT_ID/statscape-bot \
     --platform managed \
     --allow-unauthenticated \
     --set-env-vars="DISCORD_BOT_TOKEN=your_token_here"
   ```

Note: Replace YOUR_PROJECT_ID with your Google Cloud project ID

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
