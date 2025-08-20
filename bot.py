from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from app.config import TOKEN
from app.config import states

from app.handlers.start import start
from app.handlers.expenses import (
    total_expenses, daily_expenses, weekly_expenses, monthly_expenses,
    send_categories, set_category, set_amount, set_desc,
)
from app.handlers.cancel import cancel

from app.database.connection import create_tables

create_tables()


def main():
    """Start the bot."""
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(MessageHandler(Filters.text("Bosh sahifa"), start))
    dispatcher.add_handler(MessageHandler(Filters.text("Xarajatlarim"), total_expenses))

    dispatcher.add_handler(MessageHandler(Filters.text("Bugungi xarajatlarim"), daily_expenses))
    dispatcher.add_handler(MessageHandler(Filters.text("Xaftalik xarajatlarim"), weekly_expenses))
    dispatcher.add_handler(MessageHandler(Filters.text("Oylik xarajatlarim"), monthly_expenses))

    add_expense_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text("Xarajat qo'shish"), send_categories)],
        states={
            states.CATEGORY: [MessageHandler(Filters.regex('^(Ovqatlanish|Transport|Ijara|Boshqa)$'), set_category)],
            states.AMOUNT: [MessageHandler(Filters.regex('^\d+(\.\d+)?$'), set_amount)],
            states.DESC: [MessageHandler(Filters.text, set_desc)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(add_expense_handler)

    # --- Start polling ---
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
