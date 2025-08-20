from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from app.database import get_session
from app.services.user_service import get_or_create_user


def start(update: Update, context: CallbackContext) -> None:
    """
    /start command handler.
    Creates the user in DB if not exists.
    """
    tg_user = update.effective_user

    with get_session() as db:
        # get_or_create user in DB
        user = get_or_create_user(
            db=db,
            tg_id=tg_user.id,
            full_name=tg_user.full_name or ""
        )

        context.user_data['user_id'] = user.id

    update.message.reply_text(
        f"Assalomu alaykum, {tg_user.full_name}!\n",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("Balans"),
                    KeyboardButton("Xarajatlarim"),
                    KeyboardButton("Xarajat qo'shish"),
                ]
            ]
        )
    )
