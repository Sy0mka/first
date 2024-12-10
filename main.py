import telebot
from extensions import APIException, Converter
from config import TOKEN, keys

# Создание объекта бота с использованием токена
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start', 'help'])
def send_start_help(message: telebot.types.Message):
    text = (
        "Чтобы получить цену валюты, отправьте сообщение в формате: \n"
        "<имя валюты> <в какую валюту перевести> <количество> \n"
        "Показать доступные валюты: /values"
    )
    bot.reply_to(message, text)

# Обработчик команды /values
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

# Основной обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        # Разбиваем сообщение на части
        values = message.text.split(' ')

        # Проверяем, что в сообщении три элемента
        if len(values) != 3:
            raise APIException('Неправильное количество параметров.')

        # Присваиваем переменные
        quote, base, amount = values

        # Вызываем собственное исключение APIException с текстом пояснения ошибки
        price = Converter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} : {price}'
        bot.send_message(message.chat.id, text)

# Запуск бота
bot.polling(none_stop=True)