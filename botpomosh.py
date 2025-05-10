import random
import telebot

bot = telebot.Telebot('7857205665:AAEaoyE_qG3hNonDQVUmW76BiICHFVtai-A')

problems = ["мусор на улицах и водоемах", "выбросы промышленных предприятий", "необработанные отходы на свалках", "пластиковые отходы в океане"]

advice = {
    "мусор на улицах и водоемах": "Не выбрасывайте мусор на улице, используйте мусорные контейнеры.",
    "выбросы промышленных предприятий": "Поддерживайте строгую экологическую политику для предприятий, контролируйте выбросы в атмосферу.",
    "необработанные отходы на свалках": "Отсортируйте бытовые отходы, утилизируйте отходы правильно, создавайте перерабатываемые пункты.",
    "пластиковые отходы в океане": "Избегайте использование пластиковой посуды, поддерживайте проекты по очистке океанов от пластика."
}
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    text = (
        f'Привет, {message.from_user.first_name}! Я бот, который может помочь избавиться от загрязнения природы!\n\n'
        'Отправь команду /sovet, чтобы получить совет по избавлению от загрязнения'
    )

    bot.send_message(chat_id, text)

@bot.message_handler(commands=['sovet'])
def send_mem(message):
    random_sovet = choice(listdir('advices'))
    with open(f'advices/{random_sovet}', 'rb') as f:  
        bot.send_text(message.chat.id, f)  

bot.infinity_polling()
