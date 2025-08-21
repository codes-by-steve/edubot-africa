# main.py - EduBot Africa (Minimal Working Version)
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🌍 African context examples (customize for your region)
CURRENCY_EXAMPLES = {
    "GHS": "Ghana Cedis (Ghana)",
    "NGN": "Naira (Nigeria)",
    "KES": "Kenya Shillings (Kenya)",
    "ZAR": "Rand (South Africa)"
}

# 📚 Subject handlers
async def math_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle math problems with African context"""
    user_query = " ".join(context.args)
    
    if not user_query:
        await update.message.reply_text(
            "🔢 *Math Help*\n\n"
            "Send: `/math If 3 fufu balls cost 15 GHS, how much for 7?`\n\n"
            "I'll solve with African examples!",
            parse_mode='Markdown'
        )
        return
    
    # Simple response generator (customize later)
    currency = "GHS"  # Default - detect from query in advanced version
    example = (
        f"✅ *Math Solution* (Using {CURRENCY_EXAMPLES[currency].split(' (')[0]} context):\n\n"
        f"If 3 items = 15 {currency}\n"
        f"Then 1 item = 15 ÷ 3 = 5 {currency}\n"
        f"So 7 items = 7 × 5 = 35 {currency}\n\n"
        f"💡 *Real-life tip:* This is how market women calculate prices!\n\n"
        f"📚 *Concept:* Unit pricing - used daily across Africa."
    )
    
    await update.message.reply_text(example, parse_mode='Markdown')

async def science_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle science questions with local relevance"""
    await update.message.reply_text(
        "🔬 *Science Help*\n\n"
        "Send: `/science Why does yam rot faster in humid weather?`\n\n"
        "I'll explain with African farming examples!",
        parse_mode='Markdown'
    )

async def coding_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle basic coding questions"""
    await update.message.reply_text(
        "💻 *Coding Help*\n\n"
        "Send: `/code How to make a calculator in Python?`\n\n"
        "I'll give simple examples for beginners!",
        parse_mode='Markdown'
    )

# 🌍 Start command (bot intro)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = (
        "🌍 *Welcome to EduBot Africa!* 🌍\n\n"
        "I'm your *AI Homework Helper* built *by Africans for African students*.\n\n"
        "📚 *How to use me:*\n"
        "• `/math` Solve math problems\n"
        "• `/science` Get science help\n"
        "• `/code` Learn basic coding\n\n"
        "💡 *Special feature:*\n"
        "All examples use *African context* (crops, currency, markets)\n\n"
        "📱 *Works on any phone* - no app needed!\n\n"
        "👉 Try: `/math If 5 coconuts cost 20 GHS...`"
    )
    await update.message.reply_text(welcome, parse_mode='Markdown')

# 🚀 Main function
def main():
    TOKEN = os.getenv("TOKEN")
    
    if not TOKEN:
        print("❌ FATAL: TOKEN missing! Add to Railway Variables")
        return
    
    print("✅ EduBot Africa is LIVE!")
    app = Application.builder().token(TOKEN).build()
    
    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("math", math_handler))
    app.add_handler(CommandHandler("science", science_handler))
    app.add_handler(CommandHandler("code", coding_handler))
    
    print("🤖 Waiting for student questions...")
    app.run_polling()

if __name__ == "__main__":
    main()
