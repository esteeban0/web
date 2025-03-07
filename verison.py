from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Función para mostrar el menú con opciones
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 Llenar Formulario", web_app={"url": "https://esteeban0.github.io/web/index.html"})],
        [InlineKeyboardButton("📋 Consultar Formularios", web_app={"url": "https://esteeban0.github.io/web/registros.html"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Seleccione una opción:", reply_markup=reply_markup)

# Configurar el bot
def main():
    app = Application.builder().token("8009681771:AAEzyHM3FtlWWLd8mdBDasmrHH0ghRQSQxY").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
