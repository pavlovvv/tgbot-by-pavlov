import telebot
import random
from telebot import types
bot = telebot.TeleBot('1646836240:AAGaMcjRDIbvDFRHg2PnO_fodtwrWZ5r4_I')
spam = 0
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=1)
keyboard1.row('Пообщаться', 'Получить стикер', 'Спам')
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Darova', reply_markup=keyboard1)
    
@bot.message_handler(content_types=['text'])
def name(message): 
    if message.text == 'Пообщаться': #Что, если чел нажмет "Пообщаться"
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, surname); #следующий шаг – функция surname
    elif message.text == 'Получить стикер': #что, если чел нажмет "Получить стикер"
        stick = ''
        sticker = 'CAACAgIAAxkBAAEB5txgMSQDi6sef_Rx0xYbBBcdw8gCdQACZwEAAuW5CBp1mHNnndy4oB4E', 'CAACAgIAAxkBAAEB5t5gMSZUBNSfVxmgSJcjxWXq5VaQfAACaAEAAuW5CBrAXSpyVl6aXx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uJgMSZbCKcs-ywfH2fuswgw5-4BEgAC6QAD5bkIGk8D5NCmXq8dHgQ', 'CAACAgIAAxkBAAEB5uRgMSZdA1bfGXshlZu0g_vgee9QOwACNAAD5bkIGs4wPvwXvSq1HgQ', 'CAACAgIAAxkBAAEB5uZgMTnKTETTA85k6KhMF73N40fvbgACgAEAAuW5CBoh6SYYor2_7x4E', 'CAACAgIAAxkBAAEB5udgMTnLNhPU_6lUb2gXY7GrxgX3-wACYgEAAuW5CBoEx3nwxDX6VB4E', 'CAACAgIAAxkBAAEB5uhgMTnMb3jiySYwRjnVdy8O598byAACawEAAuW5CBqoTmexPn8Iah4E', 'CAACAgIAAxkBAAEB5uxgMTnTiJMvKjBJp4QEOvwVH13gHwACUwAD5bkIGhurLSuTjQ2mHgQ', 'CAACAgIAAxkBAAEB5u5gMToAAbRF6AOuNkP_13yZIBv2KH4AAucAA-W5CBpk7GFc79wnLR4E', 'CAACAgIAAxkBAAEB5vBgMTrk4i2k-dxPHLejqw25a7WMwgACcAAD5bkIGrEbj1r0nWqxHgQ', 'CAACAgIAAxkBAAEB5vJgMTr2lqUjrveyeAHBR643DHMAASYAAlwAA-W5CBqtfAz6tvD7Lh4E', 'CAACAgIAAxkBAAEB5vRgMTr_q-XT7SUK2Xp7fMKXfTi_OgACWQAD5bkIGiJdBpdaTa0rHgQ', 'CAACAgIAAxkBAAEB5vVgMTsBgw-LN-ld82TYRcLK7ycSdAACVwAD5bkIGh750Zh2UkAmHgQ', 'CAACAgIAAxkBAAEB5vhgMTsH-zGp1QABESCMCV9kE8sMgZ4AAlwBAALluQgacEbkP952TEAeBA', 'CAACAgIAAxkBAAEB5vpgMTsRKTI1XBKMEYJAuYDHwbPL2wAC3wAD5bkIGjsIjAKKeT4NHgQ', 'CAACAgIAAxkBAAEB5vtgMTsSqqNdu2R0CeTol0iIjfd1EwAC9wAD5bkIGr-Gme5_7HbuHgQ', 'CAACAgIAAxkBAAEB5v5gMTsU_LUg_vbPnaXwRikQdmPeNgAC9QAD5bkIGnMAAaVpF6muDR4E'
        a = stick + random.choice(sticker) #метод рандома
        bot.send_sticker(message.from_user.id, a) #отсылание стикеров
    elif message.text == 'Спам': #что, если чел нажмет "Спам"
        while spam==0: #бесконечный цикл
            stick = ''
            sticker = 'CAACAgIAAxkBAAEB5txgMSQDi6sef_Rx0xYbBBcdw8gCdQACZwEAAuW5CBp1mHNnndy4oB4E', 'CAACAgIAAxkBAAEB5t5gMSZUBNSfVxmgSJcjxWXq5VaQfAACaAEAAuW5CBrAXSpyVl6aXx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uJgMSZbCKcs-ywfH2fuswgw5-4BEgAC6QAD5bkIGk8D5NCmXq8dHgQ', 'CAACAgIAAxkBAAEB5uRgMSZdA1bfGXshlZu0g_vgee9QOwACNAAD5bkIGs4wPvwXvSq1HgQ', 'CAACAgIAAxkBAAEB5uZgMTnKTETTA85k6KhMF73N40fvbgACgAEAAuW5CBoh6SYYor2_7x4E', 'CAACAgIAAxkBAAEB5udgMTnLNhPU_6lUb2gXY7GrxgX3-wACYgEAAuW5CBoEx3nwxDX6VB4E', 'CAACAgIAAxkBAAEB5uhgMTnMb3jiySYwRjnVdy8O598byAACawEAAuW5CBqoTmexPn8Iah4E', 'CAACAgIAAxkBAAEB5uxgMTnTiJMvKjBJp4QEOvwVH13gHwACUwAD5bkIGhurLSuTjQ2mHgQ', 'CAACAgIAAxkBAAEB5u5gMToAAbRF6AOuNkP_13yZIBv2KH4AAucAA-W5CBpk7GFc79wnLR4E', 'CAACAgIAAxkBAAEB5vBgMTrk4i2k-dxPHLejqw25a7WMwgACcAAD5bkIGrEbj1r0nWqxHgQ', 'CAACAgIAAxkBAAEB5vJgMTr2lqUjrveyeAHBR643DHMAASYAAlwAA-W5CBqtfAz6tvD7Lh4E', 'CAACAgIAAxkBAAEB5vRgMTr_q-XT7SUK2Xp7fMKXfTi_OgACWQAD5bkIGiJdBpdaTa0rHgQ', 'CAACAgIAAxkBAAEB5vVgMTsBgw-LN-ld82TYRcLK7ycSdAACVwAD5bkIGh750Zh2UkAmHgQ', 'CAACAgIAAxkBAAEB5vhgMTsH-zGp1QABESCMCV9kE8sMgZ4AAlwBAALluQgacEbkP952TEAeBA', 'CAACAgIAAxkBAAEB5vpgMTsRKTI1XBKMEYJAuYDHwbPL2wAC3wAD5bkIGjsIjAKKeT4NHgQ', 'CAACAgIAAxkBAAEB5vtgMTsSqqNdu2R0CeTol0iIjfd1EwAC9wAD5bkIGr-Gme5_7HbuHgQ', 'CAACAgIAAxkBAAEB5v5gMTsU_LUg_vbPnaXwRikQdmPeNgAC9QAD5bkIGnMAAaVpF6muDR4E'
            a = stick + random.choice(sticker)  #метод рандома
            bot.send_sticker(message.from_user.id, a) #отсылание стикеров    
    else:
        bot.send_message(message.from_user.id, 'Напиши /start');

def surname(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?'); 
    bot.register_next_step_handler(message, age); #следующий шаг - функция age

def age(message): #получаем возраст
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, keyboard); #следующий шаг - функция keyboard
    
def keyboard(message):
    global age;
    age = message.text;
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_first = types.InlineKeyboardButton(text='Да', callback_data='item1'); #кнопка "Да"
    keyboard.add(key_first); #добавляем кнопку в клавиатуру
    key_second= types.InlineKeyboardButton(text='Нет', callback_data='item2'); #кнопка "Нет"
    keyboard.add(key_second); #добавляем кнопку в клавиатуру
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'; #выводим окончательный результат
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'item1':
            bot.send_message(call.message.chat.id, 'А кто-то сомневался?')
            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEB5wJgMWVpYvbB0tz5v9iDr5w64kZguwACAgADO2AkFKDCS3QQPmUeHgQ' ) #отсылание стикеров
        if call.data == 'item2':
            bot.send_message(call.message.chat.id, 'Не понял...')
            bot.send_message(call.message.chat.id, 'Получай11111')
            while spam==0: #бесконечный цикл
                stick = ''
                sticker = 'CAACAgIAAxkBAAEB5txgMSQDi6sef_Rx0xYbBBcdw8gCdQACZwEAAuW5CBp1mHNnndy4oB4E', 'CAACAgIAAxkBAAEB5t5gMSZUBNSfVxmgSJcjxWXq5VaQfAACaAEAAuW5CBrAXSpyVl6aXx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uBgMSZYdopEhA38WXSSR5MgJhTDygACYQEAAuW5CBo39PMaQOFrZx4E', 'CAACAgIAAxkBAAEB5uJgMSZbCKcs-ywfH2fuswgw5-4BEgAC6QAD5bkIGk8D5NCmXq8dHgQ', 'CAACAgIAAxkBAAEB5uRgMSZdA1bfGXshlZu0g_vgee9QOwACNAAD5bkIGs4wPvwXvSq1HgQ', 'CAACAgIAAxkBAAEB5uZgMTnKTETTA85k6KhMF73N40fvbgACgAEAAuW5CBoh6SYYor2_7x4E', 'CAACAgIAAxkBAAEB5udgMTnLNhPU_6lUb2gXY7GrxgX3-wACYgEAAuW5CBoEx3nwxDX6VB4E', 'CAACAgIAAxkBAAEB5uhgMTnMb3jiySYwRjnVdy8O598byAACawEAAuW5CBqoTmexPn8Iah4E', 'CAACAgIAAxkBAAEB5uxgMTnTiJMvKjBJp4QEOvwVH13gHwACUwAD5bkIGhurLSuTjQ2mHgQ', 'CAACAgIAAxkBAAEB5u5gMToAAbRF6AOuNkP_13yZIBv2KH4AAucAA-W5CBpk7GFc79wnLR4E', 'CAACAgIAAxkBAAEB5vBgMTrk4i2k-dxPHLejqw25a7WMwgACcAAD5bkIGrEbj1r0nWqxHgQ', 'CAACAgIAAxkBAAEB5vJgMTr2lqUjrveyeAHBR643DHMAASYAAlwAA-W5CBqtfAz6tvD7Lh4E', 'CAACAgIAAxkBAAEB5vRgMTr_q-XT7SUK2Xp7fMKXfTi_OgACWQAD5bkIGiJdBpdaTa0rHgQ', 'CAACAgIAAxkBAAEB5vVgMTsBgw-LN-ld82TYRcLK7ycSdAACVwAD5bkIGh750Zh2UkAmHgQ', 'CAACAgIAAxkBAAEB5vhgMTsH-zGp1QABESCMCV9kE8sMgZ4AAlwBAALluQgacEbkP952TEAeBA', 'CAACAgIAAxkBAAEB5vpgMTsRKTI1XBKMEYJAuYDHwbPL2wAC3wAD5bkIGjsIjAKKeT4NHgQ', 'CAACAgIAAxkBAAEB5vtgMTsSqqNdu2R0CeTol0iIjfd1EwAC9wAD5bkIGr-Gme5_7HbuHgQ', 'CAACAgIAAxkBAAEB5v5gMTsU_LUg_vbPnaXwRikQdmPeNgAC9QAD5bkIGnMAAaVpF6muDR4E'
                a = stick + random.choice(sticker)  #метод рандома
                bot.send_sticker(call.message.chat.id, a) #отсылание стикеров
#RUN
bot.polling(none_stop=True); 
