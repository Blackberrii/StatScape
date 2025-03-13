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

# Oracle Cloud Deployment Instructions

1. Create an Oracle Cloud account and access the Always Free tier

2. Create a Compute instance:
   - Select "Create a VM instance" in the Compute section
   - Name your instance (e.g., "discord-bot")
   - Select "Image and shape"
      - Choose "Oracle Linux 8"
      - Click "Change Shape"
      - Under "Instance Type" select "Virtual Machine"
      - Under "Shape Series" select "Ampere"
      - Choose "VM.Standard.A1.Flex"
      - Configure resources:
         - Number of OCPUs: 1
         - Amount of memory: 6 GB
   - Configure networking:
      - Create a new VCN (Virtual Cloud Network) if none exists
      - Use default subnet
      - Assign a public IP
   - Add SSH keys:
      - Generate a key pair if you don't have one
      - Save the private key securely
   - Configure Advanced Options:
      - Boot Volume: Use default (50 GB)
      - Network Setup: Use default VNIC settings

3. Configure security:
   - Go to Networking > Virtual Cloud Networks > Your VCN
   - Click on your subnet's Security List
   - Add Ingress Rules:
      - Allow TCP ports 80, 443
      - Allow port 22 (SSH) from your IP only
   - Open required ports in Ubuntu firewall:
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw allow 22/tcp
   sudo ufw enable
   ```

4. Deploy the bot:
   ```bash
   # Install Docker
   sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
   sudo dnf install -y docker-ce docker-ce-cli containerd.io
   sudo systemctl start docker
   sudo systemctl enable docker

   # Clone your repository
   git clone <your-repo-url>
   cd <repo-directory>

   # Set up environment variables
   cp .env.example .env
   nano .env  # Edit with your Discord token and other configs

   # Run deployment script
   chmod +x deploy.sh
   ./deploy.sh
   ```

5. Monitor the bot:
   ```bash
   docker logs discord-bot
   ```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
