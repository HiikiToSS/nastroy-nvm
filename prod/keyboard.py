from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# #main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = '/start')],
#                                      [KeyboardButton(text = '/begin')],
#                                      [KeyboardButton(text = '/stop')]],
#                            resize_keyboard=True,
#                            input_field_placeholder='Если ты ленивая жопа - жми кнопки')


#start_register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Регистрация')]],
#                                resize_keyboard = True)

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Отправить номер', request_contact=True)]],
                                 resize_keyboard = True, input_field_pleceholder = 'Можете сделать это автоматически, нажав на кнопку')
#

instart = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Начать прямо сейчас', callback_data = 'start_now')],
                                                [InlineKeyboardButton(text = 'Указать время', callback_data = 'time_edit')],
                                                [InlineKeyboardButton(text = 'Вывод статистики', callback_data = 'statistic')],
                                                [InlineKeyboardButton(text = 'Закончить наблюдения', callback_data = 'stop')]])