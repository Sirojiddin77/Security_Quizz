import telegram
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot tokenini o'zingizning BotFather'dan olingan token bilan almashtiring
TOKEN = '8032404481:AAEiIwEkrfTvYw5QPLL4ToQ8PFsKDFF9YCM'


# /start buyrug'i uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Tugmalar ro'yxati
    keyboard = [
        ['/start', '/help']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Xush kelibsiz xabari
    welcome_message = "Assalomu alaykum! Botimizga xush kelibsiz! 😊\n" \
                      "Quyidagi tugmalardan foydalanishingiz mumkin:"

    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup
    )


# /help buyrug'i uchun funksiya
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_message = "Bu bot quyidagi buyruqlarni qo'llab-quvvatlaydi:\n" \
                   "/start - Botni ishga tushirish\n" \
                   "/help - Yordam ma'lumotlari"

    await update.message.reply_text(help_message)


def main() -> None:
    # Application obyektini yaratamiz
    application = Application.builder().token(TOKEN).build()

    # Buyruq handlerlarini qo'shamiz
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Botni ishga tushiramiz
    print("Bot ishga tushdi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()