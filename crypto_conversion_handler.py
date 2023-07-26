import requests

from start_handler import start

PUSH_IMG = 4
def get_crypto_rate(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&&vs_currencies=cny"
    response = requests.get(url)
    data = response.json()

    if crypto in data and 'cny' in data[crypto]:
        return float(data[crypto]['cny'])
    else:
        return None

def enter_yuan_amount(update, context):
    user = update.message.from_user
    context.user_data['yuan_amount'] = update.message.text
    if context.user_data['yuan_amount'].isdigit() == True:
        if int(context.user_data['yuan_amount']) > 99:
            selected_crypto = context.user_data['crypto']
            conversion_rate = get_crypto_rate(selected_crypto)
            print(context.user_data['yuan_amount'])
            if conversion_rate:
                yuan_amount = float(context.user_data['yuan_amount'])
                context.user_data['crypto_amount'] = yuan_amount / conversion_rate
                yuan_amount = round(int(yuan_amount) * 1.05, 2)
                update.message.reply_text(
                    f"Спасибо за использование нашего бота!\n\n"
                    f"Выбрали оплату : {context.user_data['payment_method']}\n"
                    f"Вы выбрали криптовалюту: {context.user_data['crypto']}\n"
                    f"Вы ввели номер кошелька: {context.user_data['wallet_number']}\n"
                    
                    f"Сумма в выбранной криптовалюте: {context.user_data['crypto_amount']}\n\n"
                    f"кошелёк получателя: qiwi.com/p/79001241038\n"
                    f"сумма перевода({yuan_amount}¥)\n\n"
                    f"Подтвердите операцию, введите 'да' или 'нет':"
                )
            else:
                update.message.reply_text(
                    "Не удалось получить курс выбранной криптовалюты."
                )
                return start(update, context)
            return PUSH_IMG
        else:
            update.message.reply_text(
                "Введите сумму больше 100 юаней:"
            )
            return

    else:
        update.message.reply_text(
            "Введите сумму а не слово)"
        )
        return