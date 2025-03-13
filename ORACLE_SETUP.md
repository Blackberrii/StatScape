# Oracle Cloud Setup Guide

1. SSH into your Oracle instance:
```bash
ssh -i ~/.ssh/ssh_key opc@<your-instance-ip>
```

2. Install git and clone your repository:
```bash
sudo dnf install -y git
git clone https://github.com/Blackberrii/StatScape/ ~/statscape
cd ~/statscape
```

3. Create your .env file:
```bash
cp .env.example .env
nano .env  # Add your Discord bot token
```

4. Make scripts executable:
```bash
chmod +x deploy.sh oracle-setup.sh
```

5. Run the setup script:
```bash
./oracle-setup.sh
```

6. Check status:
```bash
sudo systemctl status statscape
docker logs statscape-bot
```
