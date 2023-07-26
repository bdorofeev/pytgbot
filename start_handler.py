from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

SELECT_PAYMENT_METHOD = 0
SELECT_CRYPTO = 1
def start(update: Update, context: CallbackContext):
    print("start")
    buttons = [
        [InlineKeyboardButton("Buff", callback_data="Buff")],
        [InlineKeyboardButton("Alipay", callback_data="Alipay")],
        [InlineKeyboardButton("OPT", callback_data="OPT")]
    ]
    markup = InlineKeyboardMarkup(buttons)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='что будем пополнять:',
        reply_markup=markup
    )
    return SELECT_PAYMENT_METHOD
def select_payment_method(update: Update, context: CallbackContext):
    context.user_data['payment_method'] = update.callback_query.data
    if context.user_data['payment_method'] == "OPT":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Вы выбрали опцию "оптовик". Перейдите на профиль: @Dorof_hanzo',
        )
    else:
        buttons = [
            [InlineKeyboardButton("bitcoin", callback_data="bitcoin")],
            [InlineKeyboardButton("tether", callback_data="tether")],
            [InlineKeyboardButton("Ethereum (ERC20)", callback_data="ethereum")],
        ]
        markup = InlineKeyboardMarkup(buttons)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Выбрали криптовалюту: ' + context.user_data['payment_method'],
            reply_markup=markup
        )

        return SELECT_CRYPTO