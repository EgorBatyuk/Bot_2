import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher.filters import Text

API_TOKEN = '1703747406:AAEgIhCXYSFBaBRAOyMZ4oXoo7Tm03c25eg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text', 'photo'])
async def paragraph_1(message):
    file = open('изобр_дет_и_м_виды.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Местный вид — изображение отдельного ограниченного места поверхности предмета.')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Теория видов")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_2(message):
    file = open('hfphtp.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Разрез — это изображение предмета, мысленно рассеченного одной или несколькими '
                                      'секущими плоскостями.\n\n'
                                      'На разрезе показывают то, что находится в секущей '
                                      'плоскости и что расположено за ней.')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Классификация разрезов")
    button2 = types.KeyboardButton("Обозначение разрезов")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_3(message):
    file = open('соед.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Правила соединения половины вида и половины разреза")
    button2 = types.KeyboardButton("Условности и упрощения")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_4(message):
    file = open('hfphtp.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Сечение — изображение фигуры, получающейся при мысленном рассечении предмета секущей плоскостью.\n '
      'На сечении показывают только ту фигуру, которая получается в секущей плоскости.')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Классификация сечений")
    button2 = types.KeyboardButton("Обозначение сечений")
    button3 = types.KeyboardButton("Графические обозначения материалов в сечениях")
    button4 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_5(message):
    file = open('обр_резб.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Резьба — совокупность винтовых выступов и впадин, нанесенных '
                                      'по винтовой линии на внутреннюю и внешнюю боковую поверхность некоторых тел вращения')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Классификация резьбы, её основные элементы и параметры")
    button2 = types.KeyboardButton("Обозначение резьбы на черчеже")
    button2 = types.KeyboardButton("Метрическая резьба и её обозначение")
    keyboard.add(button1, button2)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_6(message):
    file = open('виды_соед.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Разъёмные резьбовые соединения")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_7(message):
    file = open('гр_дет.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Изделие — это предмет или набор предметов производства, подлежащих изготовлению'
                                      ' в организации (на предприятии) по конструкторской документации')

    await bot.send_message(message.chat.id, 'Деталь — это изделие, изготовленное из однородного по наименованию и марке '
                                      'материала без применения сборочных операций, например болт, гайка, вал, литой '
                                      'корпус, рельс, уголок, швеллер и др')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Правила выполнения эскизов")
    button2 = types.KeyboardButton("Последовательность выполнения эскиза")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_8(message):
    file = open('сбор_ед_и_дет.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Сборочная единица — изделие, составные части которого подлежат соединению между '
                                      'собой на предприятии-изготовителе сборочными операциями (свинчивание, сварка, '
                                      'пайка, склеивание, клепка и т. д.)')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Чертеж общего вида")
    button2 = types.KeyboardButton("Сборочный чертеж")
    button3 = types.KeyboardButton("Спецификация и номера позиций")
    button4 = types.KeyboardButton("Упрощения")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_9(message):
    file = open('изд_руч.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('чер_общ_вида_руч.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Чтение чертежей")
    button2 = types.KeyboardButton("Деталирование")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def paragraph_10(message):
    file = open('изобр_библ.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Строительный чертеж — чертеж, на котором изображают строительные объекты: '
                                      'здания, мосты, эстакады, тоннели, дороги, гидротехнические сооружения и т. д., '
                                      'а также отдельные элементы указанных объектов')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Строительные чертежи")
    button2 = types.KeyboardButton("Масштабы строительных чертежей")
    button3 = types.KeyboardButton("Особенности строительных чертежей")
    button4 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p12(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Дополнительные виды")
    button2 = types.KeyboardButton("Обозначение видов")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p1(message):
    file = open('проец_пред_с_искаж.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Чтобы  избежать искажения формы и размеров при  проецирования предметов на '
                                      'основные плоскости проекции, применяют дополнительную плоскость проекций, '
                                      'не параллельную основным. Ее располагают параллельно той части'
                                      ' предмета, которая на основных плоскостях изображается с искажением')

    file = open('проец_пред_с_искаж.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p2(message):
    file = open('напрв_проец.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Местные и дополнительные виды наиболее часто располагают в проекционной связи'
                                      ' с другими изображениями на чертеже. В этом случае виды не обозначаются. \n\n'
                                      'В других случаях направление проецирования, по которому получают местный и '
                                      'дополнительный виды, указывается стрелкой возле соответствующего изображения')

    file = open('обознач_видов_р.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Над стрелкой и над полученным изображением (видом) наносят одну и ту же' 
                                    'прописную букву русского алфавита. Буква всегда должна быть вертикальной. '
                                      'При обозначении буква назначается в '
                                      'алфавитном порядке по возрастанию (А, Б, В, Г и т. д.)')


async def p3(message):
    file = open('класс_разрез.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Простой разрез — разрез, полученный при мысленном рассечении предмета одной'
                                      ' секущей плоскостью.')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Вертикальный разрез")
    button2 = types.KeyboardButton("Горизонтальный разрез")
    button3 = types.KeyboardButton("Наклонный разрез")
    button4 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p4(message):
    file = open('обр_фронт_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('обр_проф_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p5(message):
    file = open('обр_гор_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p6(message):
    file = open('обр_накл_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p7(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Правила обозначения разрезов")
    button2 = types.KeyboardButton("Графическое обозначение материалов")
    button3 = types.KeyboardButton("Местный разрез")
    button4 = types.KeyboardButton("Разрезы в аксонометрических проекциях")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p71(message):
    file = open('обознач_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Правивала  обозначение разрезов:\n\n'
                                      '1. Положение секущей плоскости указывают на чертеже линией сечения.\n\n'
                                        '2. Если секущая плоскость совпадает с плоскостью симметрии предмета,'
                                      ' разрез располагается на месте одного из видов (а). При этом'
                                        'положение секущей плоскости на чертеже не указывают и сам разрез не'
                                        'обозначают.\n\n'
                                        '3. Если секущая плоскость не совпадает с плоскостью симметрии детали (б),'
                                      ' то линию сечения изображают разомкнутой линией со'
                                        'стрелками, которые указывают направление взгляда. Толщина разомкнутых линий '
                                      'в 1,5 раза больше сплошной толстой основной линии.')


async def p8(message):
    file = open('граф_обознач_мат_в_раз.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p9(message):
    await bot.send_message(message.chat.id, 'Чтобы показать на чертежах внутреннее строение предметов в отдельных '
                                      'ограниченных местах, применяют разрезы, которые называют местными.')

    file = open('мест_раз1.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Помните!\n\n'
                                      'Волнистая линия, ограничивающая местный разрез, не должна совпадать с '
                                      'какими-либо другими линиями на виде или быть их продолжением.')

    file = open('', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p10(message):
    file = open('раз_в_акс.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p13(message):
    await bot.send_message(message.chat.id, 'Правила соединения половины вида и половины разреза:\n\n'
                                      '1. Граница между видом и разрезом — ось симметрии(см. рис.)\n\n'
                                      '2. Разрез на чертеже всегда располагают справа от оси симметрии (если ось '
                                      'симметрии вертикальная), а вид — слева. При совмещении по горизонтальной оси '
                                      'симметрии — вид располагается сверху, а разрез снизу\n\n'
                                      '3. На половине вида штриховые линии, изображающие контур внутренних очертаний, '
                                      'не проводят\n\n'
                                      '4. Размерные линии, относящиеся к элементу детали, вычерченному только до оси '
                                      'симметрии (например, отверстия), ограничивают с одной стороны стрелкой, разрывая'
                                      ' размеренную линию за осью симметрии на расстоянии 2—5 мм. Размер указывают полный\n\n'
                                      '5. Размеры внутренних элементов детали предпочтительно наносить со стороны '
                                      'разреза, внешних — со стороны вида')

    file = open('раз_в_акс.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p14(message):
    await bot.send_message(message.chat.id, 'Условности и упрощения\n\n'
                                      '1. тонкие стенки и ребра жесткости при выполнении разрезов вдоль показываются '
                                      'не рассеченными\n\n'
                                      '2. при соединении половины вида и половины разреза, если с осевой линией '
                                      'совпадают ребра предмета, то часть вида и часть разреза разделяют сплошной '
                                      'волнистой линией. Эта линия должна быть расположена так, чтобы ребро было '
                                      'показано на изображении. Если оно расположено на внутренней поверхности, то дают'
                                      ' больше половины разреза (а), если наружной — больше половины вида (б)')

    file = open('услов_и_упр.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p15(message):
    file = open('сечения.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Вынесенные сечения")
    button2 = types.KeyboardButton("Наложенные сечения")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p16(message):
    await bot.send_message(message.chat.id, 'Вынесенные сечения:\n\n'
                                      '1. непосредственно в проекционной связи (а)'
                                      '2. на продолжении линии сечения (если предмет симметричен). При этом линию '
                                      'сечения показывают штрихпунктирной линией (б)'
                                      'в разрыве между частями вида; при этом условный разрез на виде ограничивают '
                                      'тонкой волнистой линией (в)')

    file = open('вынес-сеч.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p17(message):
    await bot.send_message(message.chat.id, 'Наложенные сечения — сечения, расположенные непосредственно на видах чертежа '
                                      'и именно там, где проходит секущая плоскость')

    file = open('налож_сеч.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p18(message):
    file = open('обознач_сеч.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Если секущая плоскость проходит через ось поверхности вращения, ограничивающей '
                                      'отверстие или углубление, то на фигуре сечения контур отверстия или углубления '
                                      'в сечении показывают полностью ')

    file = open('обознач_несем_сеч.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Для несимметричных сечений, расположенных в разрыве вида (а) или наложенных '
                                      '(б), линию сечения указывают с помощью разомкнутой прямой со стрелками, '
                                      'но без буквенных ее обозначений')


async def p19(message):
    file = open('граф.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('направ_лин.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Графическое обозначение материалов в сечениях выполняют тонкими параллельными '
                                      'линиями, которые проводят под углом 45° к линии контура изображения или его оси')


async def p20(message):
    file = open('виды_резб_проф.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('основ_эл_рез.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'элементы и параметры резьбы:\n\n'
                                      '1. Наружный (внешний, номинальный) диаметр резьбы D — диаметр, описанный около '
                                      'резьбовой поверхности, условно характеризующий размеры резьбы и используемый'
                                      ' при ее обозначении\n\n'
                                      '2. Внутренний диаметр резьбы d — диаметр воображаемого прямого кругового '
                                      'цилиндра, вписанного в резьбовую поверхность\n\n'
                                      '3. Шаг резьбы P — расстояние между параллельными сторонами или вершинами двух '
                                      'рядом лежащих витков, измеренное вдоль оси резьбы\n\n'
                                      '4. Угол профиля β — угол между смежными боковыми сторонами профиля')


async def p21(message):
    file = open('изобр_рез_вв.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Изображение резьбы:\n\n'
                                      'На внешней поверхности (настержне) по наружному диаметру резьбу изображают '
                                      'сплошными толстыми основными линиями, по внутреннему диаметру — сплошными '
                                      'тонкими линиями (рис. 88). На виде слева резьбу показывают сплошной тонкой '
                                      'линией в виде дуги, примерно равной 3/4 окружности\n\n'
                                      
                                      'На внутренней поверхности (в отверстии) резьбу показывают сплошными толстыми '
                                      'основными линиями по внутреннему диаметру и сплошными тонкими — по наружному')


async def p22(message):
    file = open('изобр_метр_рез.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('усл_обознач_метр_рез.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Болт")
    button2 = types.KeyboardButton("Винт")
    button3 = types.KeyboardButton("Шпилька")
    button4 = types.KeyboardButton("Гайка")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p23(message):
    file = open('болт.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Болт — цилиндрический стержень с наружной резьбой на одном конце и головкой '
                                      'на другом')


async def p24(message):
    file = open('винт.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Винт — цилиндрический стержень с наружной резьбой на одном конце и '
                                      'конструктивным элементом для передачи крутящего момента на другом')


async def p25(message):
    file = open('шпилька.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Шпилька — цилиндрический стержень с резьбой на обоих концах или по всей '
                                      'длине стержня')


async def p26(message):
    file = open('гайка.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Гайка — крепежная деталь с резьбовым отверстием и конструктивным элементом для '
                                      'передачи крутящего момент')


async def p27(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Болтовое соединение")
    button2 = types.KeyboardButton("Виртовое соединение")
    button3 = types.KeyboardButton("Шпилечное соединение")
    button4 = types.KeyboardButton("Условности")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p28(message):
    file = open('болт_соед.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p29(message):
    file = open('винт_соед.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p30(message):
    file = open('шпил_соед.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p31(message):
    file = open('услов.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p32(message):
    await bot.send_message(message.chat.id, 'Правила выполнения эскизов:\n\n'
                                      '1. Эскизы должны быть выполнены в соответствии со Стандартами ЕСКД на чертежи\n\n'
                                      '2. Линии на эскизе должны быть ровными и четкими. Надписи выполняются чертежным шрифтом\n\n'
                                      '3. Выполняют эскизы обычно на бумаге в клетку. Сетка бумаги помогает быстрее '
                                      'проводить горизонтальные и вертикальные линии от руки, соблюдать проекционную '
                                      'связь между видами\n\n'
                                      '4. Окружности и их дуги следует проводить тонкими линиями циркулем с '
                                      'последующей обводкой от руки')


async def p33(message):
    file = open('эскиз.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '1. Внимательно рассмотрите деталь, проанализируйте ее форму и форму отдельных'
                                      ' ее частей. Деталь рекомендуется рассматривать как совокупность простых '
                                      'геометрических тел')
    await bot.send_message(message.chat.id, '2. Определите необходимое количество видов для полного выявления формы и'
                                      ' размеров детали')
    await bot.send_message(message.chat.id, '2. Определите необходимое количество видов для полного выявления формы и'
                                      ' размеров детали')

    file = open('э_2.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '3. Начертите рамку поля чертежа и рамку основной надписи. Определите '
                                      'компоновку и положение видов изображения')

    file = open('э_3.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '4. Выделите на листе соответствующую площадь в виде прямоугольника для каждого '
                                      'вида изображения. Проведите осевые линии')

    await bot.send_message(message.chat.id, '5. Определив на глаз соотношения размеров, нанесите на видах внешние (видимые) '
                                      'контуры детали. Нанесите невидимые части и мелкие элементы детали')

    file = open('э-4.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '6. Нанесите выносные и размерные линии. Обведите линии контура сплошной толстой '
                                      'основной линией')

    file = open('э_5.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '7. Обмерьте деталь, нанесите размерные числа')

    file = open('э_6.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, '8. Заполните основную надпись (наименование детали и материал, из '
                                      'которого она изготовлена)')


async def p34(message):
    file = open('чер_общ_вид.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p35(message):
    file = open('сборочный чертеж.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Сборочный чертеж — изображение сборочной единицы с необходимыми данными для '
                                      'ее сборки (изготовления) и указанием расположения деталей, способа их'
                                      ' соединений и др')


async def p36(message):
    await bot.send_message(message.chat.id, 'Спецификация — это текстовый документ, который определяет состав сборочной единицы')


async def p37(message):
    await bot.send_message(message.chat.id, 'Упрощения:\n\n'
                                      '1. Виды, расположенные в проекционной связи, не обозначают и не подписывают\n\n'
                                      '2. Штриховка одной детали (или одинаковых деталей) на всех ее изображениях '
                                      'выполняется с наклоном 45° в одну строну с одинаковым расстоянием между линиями. '
                                      'Штриховка сечений смежных деталей выполняется с наклоном в разные стороны или с '
                                      'разной частотой\n\n'
                                      '3. Дополнительные и местные виды обозначают стрелкой с буквой\n\n'
                                      '4. На симметричных изображениях соединяют половину вида с половиной разреза '
                                      '(или их части)\n\n'
                                      '5. На чертежах не показываются фаски, скругления, углубления, выступы и другие'
                                      ' мелкие элементы, зазоры между стержнем и отверстием\n\n')


async def p38(message):
    await bot.send_message(message.chat.id, 'Правила чтения чертежа общего виды и сборочного чертежа:\n\n'
                                      '1. Ознакомление с основной надписью\n\n'
                                      '2. Ознакомление с изображением. Устанавливают назначение и принцип работы '
                                      'изделия, его технические характеристики, требования к эксплуатации. Определяют,'
                                      ' какие на чертеже имеются виды, разрезы, сечения. Выясняют положение секущих'
                                      ' плоскостей, с помощью которых выполнены сечения и разрезы\n\n'
                                      '3. Изучение составных частей изделия. Определяют по спецификации названия '
                                      'деталей, находят их на изображении (на виде, разрезе). Сравнивая изображения '
                                      'каждой детали, определяют ее форму\n\n'
                                      '4. Изучение конструкции изделия. Выясняют, как соединены друг с другом детали, '
                                      'находят крепежные детали (для разъемных соединений)\n\n'
                                      '5. Ознакомление с другими сведениями (размерами, надписями, условными обозначениями)\n\n'
                                      '6. Установление характера взаимодействия составных частей изделия, их '
                                      'функциональные особенности и взаимодействие\n\n'
                                      '7. Изучение формы и положения конкретной детали, определение ее номера на '
                                      'чертеже и в таблице (спецификации). При этом необходимо учитывать общую '
                                      'конструкцию изделия, проекционную связь изображений, а также направление штриховки\n\n'
                                      '8. Определение процесса сборки и разборкиизделия\n\n')


async def p39(message):
    file = open('детализирование.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Деталирование — процесс выполнения по чертежу общего вида чертежей отдельных деталей')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("Порядок при выполнении детализировании")
    button2 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p40(message):
    await bot.send_message(message.chat.id, 'При выполнении деталирования рекомендуется соблюдать следующий порядок:\n\n'
                                      '1. Чтение сборочного чертежа\n\n'
                                      '2. Мысленное разделение изделия на отдельные детали, из которых оно состоит\n\n'
                                      '3. Определение деталей, чертежи которых нужно выполнить. Начинать деталирование'
                                      ' целесообразно с простых по форме деталей, так как мысленное удаление этих '
                                      'деталей облегчит определение формы более сложных\n\n\''
                                      '4. Определение необходимых изображений, которые нужны для чертежа каждой детали\n\n'
                                      'Помните! Количество изображений должно быть минимальным, но достаточным для '
                                      'полного изучения формы и размеров детали\n\n'
                                      '5. Выбор масштаба изображений. В процессе деталирования нужно ориентироваться '
                                      'на размер деталей. Небольшие детали, особенно сложной формы, изображают в '
                                      'большем масштабе\n\n'
                                      '6. Компоновка и последовательное построение изображения. На чертежах деталей '
                                      'изображают те элементы, которые на сборочном чертеже не показывают или '
                                      'показывают упрощенно\n\n'
                                      '7. Нанесение размеров. Их измеряют на изображениях сборочного чертежа с '
                                      'учетом масштаба\n\n')


async def p41(message):
    file = open('строитнльный-чер_дом.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Генеральный план строительного участка — план местности, по которому можно '
                                      'судить о размещении проектируемого здания, планировке самого участка, зеленых '
                                      'насаждения и т. д')

    await bot.send_message(message.chat.id, 'План здания — разрез здания горизонтальной плоскостью на уровне немного выше '
                                      'подоконника. Для многоэтажного здания планы выполняют для каждого этажа')

    await  bot.send_message(message.chat.id, 'Разрез — изображение здания, мысленно рассеченного вертикальной плоскостью')

    await bot.send_message(message.chat.id, 'Фасад — изображение внешней стороны здания')


async def p42(message):
    await bot.send_message(message.chat.id, 'Масштаб строительного чертежа зависит от размеров изображаемого объекта и'
                                      ' назначения чертежа')


async def p43(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton("План первого этажа")
    button2 = types.KeyboardButton("Фасад")
    button3 = types.KeyboardButton("Разрез")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p44(message):
    file = open('план_первого_этажа.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p45(message):
    file = open('числ-отмет_высот.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p46(message):
     file = open('разрез_дома.png', 'rb')
     await bot.send_photo(message.chat.id, file)

