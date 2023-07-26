from telegram import Update
from telegram.ext import CallbackContext

ENTER_YUAN_AMOUNT = 3

def enter_wallet_number(update: Update, context: CallbackContext) -> int:
    wallet_number = update.message.text

    context.user_data['wallet_number'] = wallet_number
    update.message.reply_text(
        "Введите сумму в юанях:"
    )
    return ENTER_YUAN_AMOUNT
