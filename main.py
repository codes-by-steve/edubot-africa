# main.py - EduBot Africa (Conflict-Fixed Version)
import os
import time
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

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

# 🚀 Main function with conflict prevention
def main():
    # Critical: Get token from environment
    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        print("❌ FATAL: TOKEN missing! Add to Railway Variables")
        return
    
    print("✅ Dependencies loaded successfully")
    print("✅ TOKEN found in environment")
    
    # ⏳ CRITICAL FIX: Add small delay to prevent race conditions
    print("⏳ Waiting 3 seconds to avoid instance conflicts...")
    time.sleep(3)
    
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
    app.run_polling(drop_pending_updates=True)  # ← CRITICAL: Prevents conflict errors

if __name__ == "__main__":
    main()
