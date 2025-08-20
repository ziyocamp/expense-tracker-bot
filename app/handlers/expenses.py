from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from app.config import states

from app.database.session import get_session

from app.services.expense_service import add_expense, get_total_expenses, get_today_expenses, get_weekly_expenses, get_monthly_expenses


def format_expenses(expenses):
    if not expenses:
        return ""

    total_amount = sum(exp.amount for exp in expenses)
    lines = []
    
    for exp in expenses:
        date_str = exp.created_at.strftime("%H:%M")
        note = f" - {exp.note}" if exp.note else ""
        lines.append(f"{date_str} | {exp.category.value}: {exp.amount} so'm{note}")

    lines.append(f"\n💰 Jami: {total_amount} so'm")
    return "\n".join(lines)


def total_expenses(update: Update, context: CallbackContext) -> None:
    user_id = context.user_data['user_id']

    with get_session() as db:
        total = get_total_expenses(db, user_id)

    update.message.reply_text(f"Jami xarajatlaringiz: {total:,.2f} so'm")

    update.message.reply_text(
        "Xarajatlarni ko'rish uchun menu tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Bugungi xarajatlarim")],
                [KeyboardButton("Xaftalik xarajatlarim")],
                [KeyboardButton("Oylik xarajatlarim")],
                [KeyboardButton("Bosh sahifa")],
            ]
        )
    )

def daily_expenses(update: Update, context: CallbackContext) -> None:
    user_id = context.user_data['user_id']

    with get_session() as db:
        expenses = get_today_expenses(db, user_id)

        text = format_expenses(expenses)
    
    if text == "":
        text = "Bugungi xarajatingiz yo‘q 🥳"
    
    update.message.reply_text(text)


def weekly_expenses(update: Update, context: CallbackContext) -> None:
    user_id = context.user_data['user_id']

    with get_session() as db:
        expenses = get_weekly_expenses(db, user_id)
        
        text = format_expenses(expenses)
    
    if text == "":
        text = "Xaftalik xarajatingiz yo‘q 🥳"
    
    update.message.reply_text(text)


def monthly_expenses(update: Update, context: CallbackContext) -> None:
    user_id = context.user_data['user_id']

    with get_session() as db:
        expenses = get_monthly_expenses(db, user_id)
        
        text = format_expenses(expenses)
    
    if text == "":
        text = "Oylik xarajatingiz yo‘q 🥳"
    
    update.message.reply_text(text)


def send_categories(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Xarajatlarni ko'rish uchun menu tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Ovqatlanish")],
                [KeyboardButton("Transport")],
                [KeyboardButton("Ijara")],
                [KeyboardButton("Boshqa")],
            ]
        )
    )

    return states.CATEGORY


def set_category(update: Update, context: CallbackContext) -> None:

    context.user_data['category'] = update.message.text

    update.message.reply_text(
        "Xarajat miqdorini kiriting:",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return states.AMOUNT


def set_amount(update: Update, context: CallbackContext) -> None:

    context.user_data['amount'] = float(update.message.text)

    update.message.reply_text("Xarajat sababini kiriting:")
    
    return states.DESC


def set_desc(update: Update, context: CallbackContext) -> None:
    
    context.user_data['desc'] = update.message.text

    user_data = context.user_data

    with get_session() as db:
        add_expense(
            db=db,
            user_id=user_data['user_id'],
            category=user_data['category'],
            amount=user_data['amount'],
            note=user_data['desc'],
        )

    context.user_data.pop("category")
    context.user_data.pop("amount")
    context.user_data.pop("desc")

    update.message.reply_text("Xarajat qo'shildi")
    
    return ConversationHandler.END
