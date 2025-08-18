# 📁 Telegram Bot with SQLAlchemy - Professional Project Structure

```
telegram_expense_bot/
│
├── 📁 app/                          # Main application package
│   ├── __init__.py                  # Makes it a Python package
│   ├── 📁 models/                   # Database models (SQLAlchemy ORM)
│   │   ├── __init__.py
│   │   ├── base.py                  # Base model class with common fields
│   │   ├── user.py                  # User model
│   │   └── expense.py               # Expense model
│   │
│   ├── 📁 handlers/                 # Telegram bot handlers (commands & conversations)
│   │   ├── __init__.py
│   │   ├── start.py                 # /start command handler
│   │   ├── expense.py               # Expense-related handlers
│   │   └── stats.py                 # Statistics handlers
│   │
│   ├── 📁 database/                 # Database configuration and sessions
│   │   ├── __init__.py
│   │   ├── connection.py            # Database connection setup
│   │   └── session.py               # Session management
│   │
│   ├── 📁 services/                 # Business logic layer
│   │   ├── __init__.py
│   │   ├── user_service.py          # User-related business logic
│   │   └── expense_service.py       # Expense-related business logic
│   │
│   ├── 📁 utils/                    # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── decorators.py            # Custom decorators (auth, error handling)
│   │   └── validators.py            # Input validation functions
│   │
│   └── config.py                    # Configuration settings
│
├── 📁 migrations/                   # Database migrations (Alembic)
│   └── versions/                    # Migration version files
│
├── 📁 tests/                        # Unit and integration tests
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_handlers.py
│   └── test_services.py
│
├── 📁 scripts/                      # Utility scripts
│   ├── create_tables.py             # Create database tables
│   └── seed_data.py                 # Insert sample data
│
├── bot.py                           # Main bot entry point
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables (not in git)
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore file
├── alembic.ini                      # Alembic configuration
└── README.md                        # Project documentation
```

## 📝 **File/Folder Explanations:**

### 🔹 **Core Application (`app/`)**
- **`models/`** - SQLAlchemy ORM models defining database structure
- **`handlers/`** - Telegram bot command handlers and conversation flows
- **`database/`** - Database connection, session management, and configuration
- **`services/`** - Business logic layer (separates bot logic from database operations)
- **`utils/`** - Helper functions, decorators, and validation utilities
- **`config.py`** - Centralized configuration management

### 🔹 **Database Management**
- **`migrations/`** - Alembic database migration files for version control
- **`scripts/`** - Database setup and maintenance scripts

### 🔹 **Development & Testing**
- **`tests/`** - Comprehensive test suite for models, handlers, and services
- **`bot.py`** - Main application entry point that starts the bot

### 🔹 **Configuration Files**
- **`.env`** - Environment variables (API keys, database URLs, secrets)
- **`requirements.txt`** - All Python dependencies with version pinning
- **`alembic.ini`** - Database migration configuration

## 🎯 **Why This Structure?**

✅ **Separation of Concerns** - Models, handlers, and business logic are separated
✅ **Scalable** - Easy to add new features without affecting existing code
✅ **Testable** - Each component can be tested independently
✅ **Professional** - Follows industry standards for Python web applications
✅ **Maintainable** - Clear organization makes debugging and updates easier
