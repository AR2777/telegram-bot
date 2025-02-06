from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توکن ربات شما که از BotFather دریافت کرده‌اید
TOKEN = '7190757835:AAHj1CCusjfI_wntVqpdIxWNiGXcBWv2mR0'

# تابعی که به دستور /start پاسخ می‌دهد
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('سلام! من یک ربات تلگرامی هستم.')

# تابعی که به پیام‌های عادی پاسخ می‌دهد
async def echo(update: Update, context: CallbackContext) -> None:
    # هر پیامی که دریافت می‌شود، دوباره به همان پیام پاسخ داده می‌شود
    await update.message.reply_text(update.message.text)

def main():
    # ساخت اپلیکیشن جدید با توکن ربات
    application = Application.builder().token(TOKEN).build()
    
    # اضافه کردن هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))
    
    # اضافه کردن هندلر برای پیام‌های متنی
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # شروع ربات
    application.run_polling()

if __name__ == '__main__':
    main()
