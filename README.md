# StatScape Discord Bot

A Discord bot for retrieving Old School RuneScape player statistics.

[Invite the bot to your server.](https://discord.com/oauth2/authorize?client_id=1348056629429403668)




(if the button above does not work:)

https://discord.com/oauth2/authorize?client_id=1348056629429403668

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

The bot now uses an interactive menu system with a single command:

* `!lookup <username>` - Opens an interactive menu to view all OSRS statistics

Example:
```
!lookup zezima
```

Once the menu appears, you can click buttons to view:
- Skills - Displays levels, experience, and ranks for all OSRS skills
- Boss KC - Shows kill counts for all OSRS bosses (with pagination)
- Clue Scrolls - Displays completed clue scroll counts by difficulty

## Interactive Interface

The new button-based interface provides an easier way to view different statistics:
1. Type `!lookup` followed by a player name
2. Click the buttons to switch between different stat views
3. For boss kill counts, use the Previous/Next buttons to navigate through pages

## Cloud Deployment

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
