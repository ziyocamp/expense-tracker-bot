from telegram.ext import Updater, CommandHandler
from app.config import TOKEN

from app.handlers.start import start


def main():
    """Start the bot."""
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # --- Register handlers ---
    dispatcher.add_handler(CommandHandler("start", start))

    # --- Start polling ---
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
