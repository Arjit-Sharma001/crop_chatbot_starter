import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from flask import Flask, request, jsonify
from chat_handler import handle_query  # Use your existing handle_query function

# Set up the logger
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your actual Telegram bot token
TELEGRAM_TOKEN = "8056284655:AAEelePCtVELVMMl85QcR7gb0rlmSkQOFOM"

# Define start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌾 Welcome to the Crop Insights Bot! Ask me anything about farming, soil, or crop yield.")

# Define message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    response = handle_query(user_query)  # Call your Flask app's query handler
    await update.message.reply_text(f"🌾 AI Insight:\n{response['reply']['text']}")

# Set up the bot with Telegram API
def run_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    run_telegram_bot()
