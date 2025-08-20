from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from .start import start

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    start(update, context)

    return ConversationHandler.END
