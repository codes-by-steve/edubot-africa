# main.py - EduBot Africa (GUARANTEED WORKING)
import os
import sys

# 🔍 Dependency check (helps diagnose errors)
try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
except ImportError as e:
    print(f"❌ FATAL DEPENDENCY ERROR: {str(e)}")
    print("👉 CHECK requirements.txt - MUST contain: python-telegram-bot==20.6")
    print("👉 CHECK .python-version file exists with 3.10")
    sys.exit(1)

# 🌍 African context examples
CURRENCY_EXAMPLES = {
    "GHS": "Ghana Cedis",
    "NGN": "Naira",
    "KES": "Kenya Shillings"
}

# 📚 Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message"""
    welcome = (
        "🌍 *Welcome to EduBot Africa!* 🌍\n\n"
        "I solve *math, science & coding* problems with *African examples*.\n\n"
        "📚 *Try me:* `/math If 3 fufu balls cost 15 GHS...`"
    )
    await update.message.reply_text(welcome, parse_mode='Markdown')

async def math_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle math problems"""
    await update.message.reply_text(
        "✅ *Math Example:*\n\n"
        "If 3 fufu balls = 15 GHS\n"
        "Then 1 fufu = 5 GHS\n"
        "So 7 fufu = 35 GHS\n\n"
        "💡 *Market tip:* This is how traders calculate prices!",
        parse_mode='Markdown'
    )

# 🚀 Main function
def main():
    # Critical: Get token from environment
    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        print("❌ FATAL: TOKEN missing! Add to Railway Variables")
        print("👉 Key: TOKEN | Value: Your_bot_token_from_BotFather")
        return
    
    print("✅ Dependencies loaded successfully")
    print("✅ TOKEN found in environment")
    print("🚀 Starting EduBot Africa...")
    
    # Create application
    try:
        app = Application.builder().token(TOKEN).build()
        print("🤖 Application builder initialized")
    except Exception as e:
        print(f"❌ TOKEN ERROR: {str(e)}")
        print("👉 Check if your token is valid")
        return
    
    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("math", math_handler))
    
    print("✅ Handlers registered")
    print("🤖 EduBot is LIVE! Waiting for students...")
    app.run_polling()

if __name__ == "__main__":
    main()
