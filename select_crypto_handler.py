from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

ENTER_WALLET_NUMBER = 2

def select_crypto(update: Update, context: CallbackContext):
    selected_crypto = update.callback_query.data
    if selected_crypto == "tether":
        buttons = [
            [InlineKeyboardButton("BNB Beacon chain (BEP2)", callback_data="binancecoin")],
            [InlineKeyboardButton("BNB Smart Chain (BEP20)", callback_data="binancecoin")]
        ]
        markup = InlineKeyboardMarkup(buttons)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Выбрали криптовалюту: ' + update.callback_query.data,
            reply_markup=markup
        )
        from start_handler import SELECT_CRYPTO
        return SELECT_CRYPTO
    elif selected_crypto == "bitcoin" or selected_crypto == "ethereum":
        context.user_data['crypto'] = selected_crypto
        update.effective_message.reply_text("Введите номер кошелька:")
        return ENTER_WALLET_NUMBER
    else:
        context.user_data['crypto'] = selected_crypto
        update.effective_message.reply_text("Введите номер кошелька:")
        return ENTER_WALLET_NUMBER