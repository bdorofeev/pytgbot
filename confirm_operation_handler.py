from telegram.ext import ConversationHandler
from start_handler import start

CONFIRM_OPERATION = 5

def push_img(update, context):
    user = update.message.from_user
    confirmation = update.message.text.lower()

    if confirmation == 'да':
        # Запросить фото оплаты
        update.message.reply_text("Отправьте фото оплаты")
        return CONFIRM_OPERATION

    elif confirmation == 'нет':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Операция отменена.")
        return start(update, context)


    else:
        update.message.reply_text("Неверный ответ. Пожалуйста, введите 'да' или 'нет'.")
        return CONFIRM_OPERATION

def confirm_img(update, context):
    photo = update.message.photo[-1]  # Get the last photo sent by the user
    file_id = photo.file_id
    context.user_data['img'] = file_id

    recipient_chat_id = '891715912'  # Replace with the actual chat ID of the recipient
    message = (
        f"img: {context.user_data['img']}\n"
        f"Система пополнения: {context.user_data['payment_method']}\n"
        f"Ввели номер кошелька: {context.user_data['wallet_number']}\n"
        f"Выбрали криптовалюту: {context.user_data['crypto']}\n"
        f"Сумма в выбранной криптовалюте: {context.user_data['crypto_amount']}\n\n"
        f"Сумма перевода({context.user_data['yuan_amount']}¥)\n\n"
    )
    context.bot.send_message(chat_id=recipient_chat_id, text=message)
    file_obj = context.bot.get_file(file_id)
    file_obj.download('photo.jpg')  # Save the photo locally
    with open('photo.jpg', 'rb') as f:
        context.bot.send_photo(chat_id=recipient_chat_id, photo=f)
    update.message.reply_text("Операция подтверждена!")

    return ConversationHandler.END