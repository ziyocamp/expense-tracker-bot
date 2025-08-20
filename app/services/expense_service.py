import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.expense import Expense, Category

from .user_service import get_user


def add_expense(db: Session, user_id: int, category: str, amount: float, note):

    try:
        category_value = Category(category)
    except ValueError:
        category_value = Category.other

    expense = Expense(user_id=user_id, category=category_value, amount=amount, note=note)
    db.add(expense)

    user = get_user(db, user_id)

    user.balance -= amount

    db.flush()


def get_today_expenses(db: Session, user_id):
    today = datetime.date.today()
    start = datetime.datetime.combine(today, datetime.time.min)  # 00:00:00
    end = datetime.datetime.combine(today, datetime.time.max)    # 23:59:59.999999

    return db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.created_at >= start,
        Expense.created_at <= end
    ).all()


def get_weekly_expenses(db: Session, user_id):
    today = datetime.date.today()
    start_week = today - datetime.timedelta(days=today.weekday())  # Dushanba
    return db.query(Expense).filter(
        Expense.user_id == user_id,
        func.date(Expense.created_at) >= start_week,
        func.date(Expense.created_at) <= today
    ).all()


def get_monthly_expenses(db: Session, user_id):
    today = datetime.date.today()
    start_month = today.replace(day=1)
    return db.query(Expense).filter(
        Expense.user_id == user_id,
        func.date(Expense.created_at) >= start_month,
        func.date(Expense.created_at) <= today
    ).all()


def get_total_expenses(db: Session, user_id):
    total = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == user_id
    ).scalar()  # sum ni oladi
    return total or 0
