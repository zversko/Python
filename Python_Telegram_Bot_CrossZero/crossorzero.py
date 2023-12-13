import telebot
import config
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

cell = [' ' for x in range(0,9)]
xorz = 'X'
user_id = ''

def board(cell):
    """
    Отрисовка поля
    """
    xorz_board = telebot.types.InlineKeyboardMarkup()
    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='0'),
                    telebot.types.InlineKeyboardButton(f'{cell[1]}', callback_data='1'),
                    telebot.types.InlineKeyboardButton(f'{cell[2]}', callback_data='2'))

    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[3]}', callback_data='3'),
                    telebot.types.InlineKeyboardButton(f'{cell[4]}', callback_data='4'),
                    telebot.types.InlineKeyboardButton(f'{cell[5]}', callback_data='5'))

    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[6]}', callback_data='6'),
                    telebot.types.InlineKeyboardButton(f'{cell[7]}', callback_data='7'),
                    telebot.types.InlineKeyboardButton(f'{cell[8]}', callback_data='8'))

    return xorz_board

def check_winner_or_stalemate(cell):
    """
    Проверка на выигрышную позицию
    :param winner_position: Набор выигрышных позиций
    """
    winner_position = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winner_position:
        if (cell[i[0]] == cell[i[1]] == cell[i[2]] == 'X') or (cell[i[0]] == cell[i[1]] == cell[i[2]] == 'O'):
            return 1
    count = 1
    for i in cell:
        if cell[i] != ' ':
            count += 1
    return count

@bot.message_handler(commands=['start'])
def welcome(message):
    """
    Начало(Приветствие)
    """
    sti = open('picture/wellcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Крестики - нолики")
 
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu_homework(message):
    """
    Обнуляем таблицу, первый ход
    :param cell: поле
    :param xorz: текущий ход
    """
    global cell, xorz
    cell = [' ' for x in range(0,9)]

    if message.text == 'Крестики - нолики':
        bot.send_message(message.chat.id, f'Выберите клетку для установки {xorz}', reply_markup=board(cell))
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    """
    Запускаем цикл, по выбору клеток (цикл за счет редактирования одного сообщения)
    После каждого выбора клетки отправляем заполненое поле на проверку выигрышной позиции (check_winner_or_stalemate())
    :param cell: поле
    :param xorz: текущий ход
    :param user_id: ID пользователя (чтобы не смог сходить один и тот же пользователь)
    """

    global cell, xorz, user_id
    data = query.data
    data = int(data)

    if user_id == query.from_user.id:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Сейчас не Ваш ход', reply_markup=board(cell))

    elif cell[data] == ' ':
    
        user_id = query.from_user.id

        if xorz == 'X':
            xorz_cell = 'X'
            xorz = 'O'
        else:
            xorz_cell = 'O'
            xorz = 'X'

        cell[data] = xorz_cell

        if check_winner_or_stalemate(cell) == 1:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Выиграли {xorz_cell}-ки')
        elif check_winner_or_stalemate(cell) == 10:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Ничья')
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Выберите поле для установки {xorz}', reply_markup=board(cell))
    else:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Выберите другую клетку, эта клетка уже занята', reply_markup=board(cell))

bot.polling(none_stop=True)