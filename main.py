import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher.filters import Text

from handlers import *

API_TOKEN = '1703747406:AAEgIhCXYSFBaBRAOyMZ4oXoo7Tm03c25eg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def any_msg(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Местные и дополнительные виды")
    button2 = types.KeyboardButton("Понятие о разрезе")
    button3 = types.KeyboardButton("Соединение на чертеже,части вида и части разреза")
    button4 = types.KeyboardButton("Понятие о сечении")
    button5 = types.KeyboardButton("Изображение и обозначение резьбы")
    button6 = types.KeyboardButton("Соединение деталей")
    button7 = types.KeyboardButton("Выполнение эскиза детали")
    button8 = types.KeyboardButton("Назначение и особенности чертежей общего вида и сборочного чертежа изделия")
    button9 = types.KeyboardButton("Чтение чертежей,деталей,на основе анализа формы и их пространственного расположения")
    button10 = types.KeyboardButton("Строительные чертежи. Последовательность чтения строительных чертежей")
    keyboard.add(button1, button2, button3, button4, button5,
                 button6, button7, button8, button9, button10, )
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)

    @dp.message_handler(Text(equals="Местные и дополнительные виды"))
    async def with_puree(message: types.Message):
        await paragraph_1(message)

    # if message.text.lower() == 'местные и дополнительные виды':
    #     await paragraph_1(message)

    @dp.message_handler(Text(equals="Понятие о разрезе"))
    async def with_puree(message: types.Message):
        await paragraph_2(message)

    # if message.text.lower() == 'Понятие о разрезе':
    #     paragraph_2(message)

    @dp.message_handler(Text(equals="Соединение на чертеже,части вида и части разреза"))
    async def with_puree(message: types.Message):
        await paragraph_3(message)

    # if message.text.lower() == 'Соединение на чертеже,части вида и части разреза':
    #     paragraph_3(message)

    @dp.message_handler(Text(equals="Понятие о сечении"))
    async def with_puree(message: types.Message):
        await paragraph_4(message)

    # if message.text.lower() == 'Понятие о сечении':
    #     paragraph_4(message)

    @dp.message_handler(Text(equals="Изображение и обозначение резьбы"))
    async def with_puree(message: types.Message):
        await paragraph_5(message)

    # if message.text.lower() == 'Изображение и обозначение резьбы':
    #     paragraph_5(message)

    @dp.message_handler(Text(equals="Соединение деталей"))
    async def with_puree(message: types.Message):
        await paragraph_6(message)

    # if message.text.lower() == 'Соединение деталей':
    #     paragraph_6(message)

    @dp.message_handler(Text(equals="Выполнение эскиза детали"))
    async def with_puree(message: types.Message):
        await paragraph_7(message)

    # if message.text.lower() == 'Выполнение эскиза детали':
    #     paragraph_7(message)

    @dp.message_handler(Text(equals="Назначение и особенности чертежей общего вида и сборочного чертежа изделия"))
    async def with_puree(message: types.Message):
        await paragraph_8(message)

    # if message.text.lower() == 'Назначение и особенности чертежей общего вида и сборочного чертежа изделия':
    #     paragraph_8(message)

    @dp.message_handler(Text(equals="Чтение чертежей,деталей,на основе анализа формы и их пространственного расположения"))
    async def with_puree(message: types.Message):
        await paragraph_9(message)

    # if message.text.lower() == 'Чтение чертежей,деталей,на основе анализа формы и их пространственного расположения':
    #     paragraph_9(message)

    @dp.message_handler(Text(equals="Строительные чертежи. Последовательность чтения строительных чертежей"))
    async def with_puree(message: types.Message):
        await paragraph_10(message)

    # if message.text == 'Строительные чертежи. Последовательность чтения строительных чертежей':
    #     paragraph_10(message)

    @dp.message_handler(Text(equals="Теория видов"))
    async def with_puree(message: types.Message):
        await p12(message)

    # if message.text == 'Теория видов':
    #     p12(message)

    @dp.message_handler(Text(equals="Дополнительные виды"))
    async def with_puree(message: types.Message):
        await p1(message)

    # if message.text == 'Дополнительные виды':
    #     p1(message)

    @dp.message_handler(Text(equals="Обозначение видов"))
    async def with_puree(message: types.Message):
        await p2(message)

    # if message.text == 'Обозначение видов':
    #     p2(message)

    @dp.message_handler(Text(equals="Классификация разрезов"))
    async def with_puree(message: types.Message):
        await p3(message)

    # if message.text == 'Классификация разрезов':
    #     p3(message)

    @dp.message_handler(Text(equals="Вертикальный разрез"))
    async def with_puree(message: types.Message):
        await p4(message)

    # if message.text == 'Вертикальный разрез':
    #     p4(message)

    @dp.message_handler(Text(equals="Горизонтальный разрез"))
    async def with_puree(message: types.Message):
        await p5(message)

    # if message.text == 'Горизонтальный разрез':
    #     p5(message)

    @dp.message_handler(Text(equals="Наклонный разрез"))
    async def with_puree(message: types.Message):
        await p6(message)

    # if message.text == 'Наклонный разрез':
    #     p6(message)

    @dp.message_handler(Text(equals="Обозначение разрезов"))
    async def with_puree(message: types.Message):
        await p7(message)

    # if message.text == 'Обозначение разрезов':
    #     p7(message)

    @dp.message_handler(Text(equals="Правила обозначения разрезов"))
    async def with_puree(message: types.Message):
        await p71(message)

    # if message.text == 'Правила обозначения разрезов':
    #     p71(message)

    @dp.message_handler(Text(equals="Графическое обозначение материалов"))
    async def with_puree(message: types.Message):
        await p8(message)

    # if message.text == 'Графическое обозначение материалов':
    #     p8(message)

    @dp.message_handler(Text(equals="Местный разрез"))
    async def with_puree(message: types.Message):
        await p9(message)

    # if message.text == 'Местный разрез':
    #     p9(message)

    @dp.message_handler(Text(equals="Разрезы в аксонометрических проекциях"))
    async def with_puree(message: types.Message):
        await p10(message)

    # if message.text == 'Разрезы в аксонометрических проекциях':
    #     p10(message)

    @dp.message_handler(Text(equals="Правила соединения половины вида и половины разреза"))
    async def with_puree(message: types.Message):
        await p13(message)

    # if message.text == 'Правила соединения половины вида и половины разреза':
    #     p13(message)

    @dp.message_handler(Text(equals="Условности и упрощения"))
    async def with_puree(message: types.Message):
        await p14(message)

    # if message.text == 'Условности и упрощения':
    #     p14(message)

    @dp.message_handler(Text(equals="Классификация сечений"))
    async def with_puree(message: types.Message):
        await p15(message)

    # if message.text == 'Классификация сечений':
    #     p15(message)

    @dp.message_handler(Text(equals="Вынесенные сечения"))
    async def with_puree(message: types.Message):
        await p16(message)

    # if message.text == 'Вынесенные сечения':
    #     p16(message)

    @dp.message_handler(Text(equals="Наложенные сечения"))
    async def with_puree(message: types.Message):
        await p17(message)

    # if message.text == 'Наложенные сечения':
    #     p17(message)

    @dp.message_handler(Text(equals="Обозначение сечений"))
    async def with_puree(message: types.Message):
        await p18(message)

    # if message.text == 'Обозначение сечений':
    #     p18(message)

    @dp.message_handler(Text(equals="Графические обозначения материалов в сечениях"))
    async def with_puree(message: types.Message):
        await p19(message)

    # if message.text == 'Графические обозначения материалов в сечениях':
    #     p19(message)

    @dp.message_handler(Text(equals="Классификация резьбы, её основные элементы и параметры"))
    async def with_puree(message: types.Message):
        await p20(message)

    # if message.text == 'Классификация резьбы, её основные элементы и параметры':
    #     p20(message)

    @dp.message_handler(Text(equals="Обозначение резьбы на черчеже"))
    async def with_puree(message: types.Message):
        await p21(message)

    # if message.text == 'Обозначение резьбы на черчеже':
    #     p21(message)

    @dp.message_handler(Text(equals="Метрическая резьба и её обозначение"))
    async def with_puree(message: types.Message):
        await p22(message)

    # if message.text == 'Метрическая резьба и её обозначение':
    #     p22(message)

    @dp.message_handler(Text(equals="Болт"))
    async def with_puree(message: types.Message):
        await p23(message)

    # if message.text == 'Болт':
    #     p23(message)

    @dp.message_handler(Text(equals="Винт"))
    async def with_puree(message: types.Message):
        await p24(message)

    # if message.text == 'Винт':
    #     p24(message)

    @dp.message_handler(Text(equals="Шпилька"))
    async def with_puree(message: types.Message):
        await p25(message)

    # if message.text == 'Шпилька':
    #     p25(message)

    @dp.message_handler(Text(equals="Гайка"))
    async def with_puree(message: types.Message):
        await p26(message)

    # if message.text == 'Гайка':
    #     p26(message)

    @dp.message_handler(Text(equals="Разъёмные резьбовые соединения"))
    async def with_puree(message: types.Message):
        await p27(message)

    # if message.text == 'Разъёмные резьбовые соединения':
    #     p27(message)

    @dp.message_handler(Text(equals="Болтовое соединение"))
    async def with_puree(message: types.Message):
        await p28(message)

    # if message.text == 'Болтовое соединение':
    #     p28(message)

    @dp.message_handler(Text(equals="Виртовое соединение"))
    async def with_puree(message: types.Message):
        await p29(message)

    # if message.text == 'Виртовое соединение':
    #     p29(message)

    @dp.message_handler(Text(equals="Шпилечное соединение"))
    async def with_puree(message: types.Message):
        await p30(message)

    # if message.text == ' Шпилечное соединение':
    #     p30(message)

    @dp.message_handler(Text(equals="Условности"))
    async def with_puree(message: types.Message):
        await p31(message)

    # if message.text == 'Условности':
    #     p31(message)

    @dp.message_handler(Text(equals="Правила выполнения эскизов"))
    async def with_puree(message: types.Message):
        await p32(message)

    # if message.text == 'Правила выполнения эскизов':
    #     p32(message)

    @dp.message_handler(Text(equals="Последовательность выполнения эскиза"))
    async def with_puree(message: types.Message):
        await p33(message)

    # if message.text == 'Последовательность выполнения эскиза':
    #     p33(message)

    @dp.message_handler(Text(equals="Чертеж общего вида"))
    async def with_puree(message: types.Message):
        await p34(message)

    # if message.text == 'Чертеж общего вида':
    #     p34(message)

    @dp.message_handler(Text(equals="Сборочный чертеж"))
    async def with_puree(message: types.Message):
        await p35(message)

    # if message.text == 'Сборочный чертеж':
    #     p35(message)

    @dp.message_handler(Text(equals="Спецификация и номера позиций"))
    async def with_puree(message: types.Message):
        await p36(message)

    # if message.text == 'Спецификация и номера позиций':
    #     p36(message)

    @dp.message_handler(Text(equals="Упрощения"))
    async def with_puree(message: types.Message):
        await p37(message)

    # if message.text == 'Упрощения':
    #     p37(message)

    @dp.message_handler(Text(equals="Чтение чертежей"))
    async def with_puree(message: types.Message):
        await p38(message)

    # if message.text == 'Чтение чертежей':
    #     p38(message)

    @dp.message_handler(Text(equals="Деталирование"))
    async def with_puree(message: types.Message):
        await p39(message)

    # if message.text == 'Деталирование':
    #     p39(message)

    @dp.message_handler(Text(equals="Порядок при выполнении детализировании"))
    async def with_puree(message: types.Message):
        await p40(message)

    # if message.text == 'Порядок при выполнении детализировании':
    #     p40(message)

    @dp.message_handler(Text(equals="Строительные чертежи"))
    async def with_puree(message: types.Message):
        await p41(message)

    # if message.text == 'Строительные чертежи':
    #     p41(message)

    @dp.message_handler(Text(equals="Масштабы строительных чертежей"))
    async def with_puree(message: types.Message):
        await p42(message)

    # if message.text == 'Масштабы строительных чертежей':
    #     p42(message)

    @dp.message_handler(Text(equals="Особенности строительных чертежей"))
    async def with_puree(message: types.Message):
        await p43(message)

    # if message.text == 'Особенности строительных чертежей':
    #     p43(message)

    @dp.message_handler(Text(equals="План первого этажа"))
    async def with_puree(message: types.Message):
        await p44(message)

    # if message.text == 'План первого этажа':
    #     p44(message)

    @dp.message_handler(Text(equals="Фасад"))
    async def with_puree(message: types.Message):
        await p45(message)

    # if message.text == 'Фасад':
    #     p45(message)

    @dp.message_handler(Text(equals="Разрез"))
    async def with_puree(message: types.Message):
        await p46(message)

    # if message.text == 'Разрез':
    #     p46(message)

    @dp.message_handler(Text(equals="На главную"))
    async def with_puree(message: types.Message):
        await any_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    