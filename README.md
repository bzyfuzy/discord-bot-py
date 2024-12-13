# Discord Bot Project
A simple Discord bot built with Python and `discord.py`. The bot can respond to commands, like `!greet`, and is designed to be easily extended with additional features.

## Features
- Responds to the `!greet` command.
- Bot token securely loaded from environment variables.
- Easily extendable for custom commands.

## Prerequisites
- Python 3.7+ installed.
- A Discord bot token (see the [Discord Developer Portal](https://discord.com/developers/applications) for creating one).

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine:

```bash
git clone https://github.com/bzyfuzy/discord-bot-py.git
cd discord-bot-py
```

### 1. Install dependencies
You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file in the root of the project and add your Discord bot token:

1. **Copy `sample.env` to `.env`**:
   In the project directory, copy the `sample.env` file to a new file named `.env`:

   ```bash
   cp sample.env .env   # For Linux/macOS
   copy sample.env .env  # For Windows Command Prompt
   Copy-Item sample.env -Destination .env  # For Windows PowerShell
   ```

 2. Replace the bot token: Open the .env file and replace bot-token with your actual Discord bot token, like this:
  ```env
  DISCORD_TOKEN=your_actual_bot_token
  ```
  Make sure the bot token is correct and valid.

### 4. Run the bot
Once everything is set up, run the bot using:
```bash
python bot.py
```
The bot should now be running and will log into Discord using the token provided in the .env file.

### 5. Invite the bot to your Discord server
  1. Fork this repository.
  2. Create a new branch for your feature or bug fix.
  3. Submit a pull request with your changes.
 
