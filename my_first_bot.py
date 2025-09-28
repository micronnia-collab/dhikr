import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Paste Your Bot Token Here
TOKEN = "8258809727:AAGstG9FKIWQ9g5UEmTAAOeWUVK6CIl3NBQ" 

# Set up logging so you can see when the bot starts
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Define the Handler Functions ---

# This function runs when the user sends the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a greeting message when the command /start is issued."""
    user_name = update.effective_user.first_name
    await update.message.reply_text(f'Hello, {user_name}! Send me any message, and I will echo it back to you.')

# This function runs when the user sends ANY text message
async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echoes the user message."""
    # update.message.text contains the text the user sent
    user_text = update.message.text
    await update.message.reply_text(f"You said: {user_text}")

# --- Main Logic to Run the Bot ---
def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Register the handlers (Tell the bot what to do with incoming messages)
    
    # 1. CommandHandler: Listen for a specific command like /start
    application.add_handler(CommandHandler("start", start_command))

    # 2. MessageHandler: Listen for a type of message (filters.TEXT)
    # The ~filters.COMMAND prevents it from echoing /start as a message
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo_message))

    # Run the bot until the user presses Ctrl-C
    print("Bot is running... Press Ctrl-C to stop.")
    application.run_polling(poll_interval=3)

if __name__ == '__main__':
    # Make sure you replace the placeholder token before running!
    if TOKEN == "YOUR_HTTP_API_TOKEN_HERE":
        print("ERROR: Please replace 'YOUR_HTTP_API_TOKEN_HERE' with your actual bot token from @BotFather.")
    else:
        main()
