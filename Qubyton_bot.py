import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✅ QubyTON Bot aktif.\n\n"
        "QubyTON BuyBot untuk TON.\n\n"
        "Command:\n"
        "/start - cek bot\n"
        "/setup - setup token\n"
        "/stats - statistik\n"
        "/scan - scan manual"
    )
    await update.message.reply_text(text)

async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ Setup token belum aktif.\n\n"
        "Nanti command ini akan dipakai untuk memasukkan token address."
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Stats belum tersedia.")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Scan manual belum tersedia.")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN belum di-set di environment variable.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setup", setup))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("scan", scan))

    print("QubyTON Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()