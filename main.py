from telegram.ext import Updater, CommandHandler,CallbackQueryHandler, MessageHandler, Filters,ConversationHandler
from confirm_operation_handler import push_img, CONFIRM_OPERATION, confirm_img
from crypto_conversion_handler import enter_yuan_amount, PUSH_IMG
from enter_wallet_handler import enter_wallet_number, ENTER_YUAN_AMOUNT
from select_crypto_handler import ENTER_WALLET_NUMBER, select_crypto
from start_handler import start, select_payment_method, SELECT_PAYMENT_METHOD, SELECT_CRYPTO


def main():
    token = '6660279946:AAH3D_2IJk3aAlemcqi1fh6m0mq9ihJYcds'  # Replace with your Telegram bot token
    updater = Updater(token, use_context=True)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_PAYMENT_METHOD: [
                CallbackQueryHandler(select_payment_method)
            ],
            SELECT_CRYPTO: [
                CallbackQueryHandler(select_crypto)
            ],
            ENTER_WALLET_NUMBER: [
                MessageHandler(Filters.text, enter_wallet_number)
            ],
            ENTER_YUAN_AMOUNT: [
                MessageHandler(Filters.text, enter_yuan_amount)
            ],
            PUSH_IMG: [
                MessageHandler(Filters.text, push_img)
            ],
            CONFIRM_OPERATION: [
                MessageHandler(Filters.photo, confirm_img)
            ],
        },
        fallbacks=[
            CommandHandler('cancel', cancel),
            CommandHandler('reset', reset)  # Добавлен обработчик команды /reset
            ]
    )
    dp = updater.dispatcher
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

def reset(update, context):
    context.user_data.clear()
    update.message.reply_text('Состояние разговора сброшено.')
    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text('Операция отменена.')
    return ConversationHandler.END


if __name__ == '__main__':
    main()