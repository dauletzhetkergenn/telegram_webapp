from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
TOKEN = '8349763299:AAHcKzkk-v75bcbxJTLpsXC6Zrgy3gg6rPU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[InlineKeyboardButton("Открыть магазин", web_app=WebAppInfo(url="https://m280x99c-8000.euw.devtunnels.ms/"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми, чтобы открыть магазин", reply_markup=reply_markup)

    

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()