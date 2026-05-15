from aiogram import F
from aiogram.types import Message, CallbackQuery

from keyboards.keyboards import delo1, delo2, delo3, start_det, start__delo2, start__delo3, confirm_delo1_option1, confirm_delo1_option2, confirm_delo1_option3, confirm_delo2_option1, confirm_delo2_option2, confirm_delo2_option3, confirm_delo3_option1, confirm_delo3_option2, confirm_delo3_option3, retry_delo1, retry_delo2, retry_delo3, finish_game, main_keyboard

def register_detective_handlers(dp):
    
    @dp.message(F.text.in_(["🧠 Детектив"]))
    async def detective(message: Message):
        
        text = (
            "Ты готов стать лучшим детективом? \n\n"
            "📋 ПРАВИЛА ИГРЫ:\n\n"
            "1️⃣ Тебя ждут 3 интересных дела, которые нужно раскрыть\n"
            "2️⃣ Для каждого дела у тебя будет 3 варианта действий\n"
            "3️⃣ Выбирай мудро! Только ОДИН вариант приведет к успеху\n"
            "4️⃣ Если ошибешься - вернешься к делу и сможешь попробовать снова\n"
            "5️⃣ Раскрой все дела успешно и получи звание лучшего детектива! 🎯\n\n"
            "🎯 КАК ИГРАТЬ:\n\n"
            "▫️ Нажимай на кнопки с вариантами ответов\n"
            "▫️ Внимательно читай текст дела и подсказки\n"
            "▫️ Если неудачно - нажми Вернуться и выбери другой вариант\n"
            "▫️ Если успешно - переходишь к следующему делу\n"
            "▫️ В конце игры увидишь статистику твоих раскрытых дел\n\n"
            "📊 ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:\n\n"
            "После третьего дела ты получишь:\n\n"
            "✓ Финальное сообщение о твоих успехах\n"
            "✓ Количество попыток, которое потребовалось\n"
            "✓ Список раскрытых дел\n\n"
            "Все готово? Тогда начнём первое дело! 🕵️"
        )
        await message.answer(text, reply_markup=start_det)
    
    @dp.callback_query(F.data == "start_delo1")
    async def start_delo1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🕵️‍♂️ **ДЕЛО №1. ТЕНЕВОЙ ЛОББИСТ**\n\n"
            "*Женева, зал заседаний Рамочной конвенции ООН об изменении климата (UNFCCC). За закрытыми дверями обсуждается проект резолюции о поэтапном отказе от субсидий на ископаемое топливо.*\n\n"
            "Разведка ООН перехватила странный документ. В нём говорится, что одна из делегаций тайно лоббирует сохранение миллиардных субсидий для нефтяной отрасли. При этом публично эта же страна голосует за «зелёный переход» и подписала Парижское соглашение.\n\n"
            "В отчёте упоминаются три подозреваемые страны. Все они крупные экспортёры нефти. У каждой — своя легенда.\n\n"
            "**Твоя задача** — определить, кто именно стоит за лоббированием. Выбери подозреваемого, чтобы узнать подробности:"
        )
        await callback.message.answer(text, reply_markup=delo1)

    @dp.callback_query(F.data == "delo1_option1")
    async def delo1_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🇷🇺 **Россия**\n\n"
            "Делегация РФ публично поддерживает «углеродную нейтральность к 2060», но внутри кулуаров настаивает на сохранении субсидий для «северных территорий». Документы, найденные разведкой, действительно упоминали российских чиновников. Но они говорили о субсидиях для газовых проектов в Арктике — это отдельная тема, не связанная с нефтяным лобби в ООН.\n\n"
        )
        await callback.message.answer(text, reply_markup=confirm_delo1_option1)

    @dp.callback_query(F.data == "delo1_option2")
    async def delo1_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🇸🇦 **Саудовская Аравия**\n\n"
            "Королевство официально объявило о «Саудовской зелёной инициативе», но именно его представитель на прошлой неделе встречался с лоббистами Exxon. Дальнейший анализ перехваченных писем подтверждает: именно делегация Саудовской Аравии координировала действия нефтяных лоббистов.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo1_option2)

    @dp.callback_query(F.data == "delo1_option3")
    async def delo1_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🇺🇸 **США**\n\n"
            "Делегация США при новом президенте активно финансирует возобновляемую энергетику, однако сенаторы от Техаса не раз блокировали антисубсидийные поправки. США действительно блокировали несколько законопроектов внутри страны. Но в стенах ООН их делегация выступает за прозрачность субсидий.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo1_option3)

    @dp.callback_query(F.data == "choose_delo1_option1")
    async def choose_delo1_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "Россия не является главным лоббистом в этом деле. Арктические газовые проекты — отдельная история. Настоящий заказчик остался в тени.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo1)

    @dp.callback_query(F.data == "choose_delo1_option2")
    async def choose_delo1_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "✅ **ДЕЛО РАСКРЫТО!**\n\n"
            "Ты оказался прав. Именно Саудовская Аравия стояла за лоббированием нефтяных субсидий. Королевство тратит миллиарды на поддержку нефтяной отрасли, публично притворяясь «зелёным» лидером.\n\n"
            "📌 *Источник: Отчёт UNEP «Fossil Fuel Subsidies in Saudi Arabia» (2023), IPCC AR6*\n\n"
            "**Ты получаешь допуск ко второму делу!**"
        )
        await callback.message.answer(text, reply_markup=start__delo2)

    @dp.callback_query(F.data == "choose_delo1_option3")
    async def choose_delo1_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "США не имеют отношения к этому делу. Внутренние политические игры Техаса — не то же самое, что международное лобби в ООН.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo1)

    @dp.callback_query(F.data == "start_delo2")
    async def start_delo2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🕵️‍♂️ **ДЕЛО №2. ЧЁРНЫЙ ПРИЛИВ**\n\n"
            "*Порт-Харкорт, дельта реки Нигер, Нигерия. Местные жители больше не могут пить воду из колодцев — она пахнет нефтью. Рыба исчезла. Дети болеют.*\n\n"
            "Спутники ООН зафиксировали масштабное загрязнение почвы и воды. Следы ведут к одному из нефтяных месторождений, но компания отрицает свою вину. Расследование ЮНЕП длилось несколько лет.\n\n"
            "В распоряжении детективной группы оказались три версии.\n\n"
            "**Твоя задача** — выяснить, какая из них соответствует реальным фактам, установленным ООН. Выбери подозреваемого:"
        )
        await callback.message.answer(text, reply_markup=delo2)

    @dp.callback_query(F.data == "delo2_option1")
    async def delo2_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🛢️ **Royal Dutch Shell**\n\n"
            "Транснациональная корпорация, которая десятилетиями добывает нефть в дельте Нигера. Местные активисты не раз обвиняли Shell в утечках из старых трубопроводов. Компания заявляет, что загрязнение — дело рук местных воров, сливающих нефть незаконно.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo2_option1)

    @dp.callback_query(F.data == "delo2_option2")
    async def delo2_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🏛️ **Правительство Нигерии**\n\n"
            "Национальная нефтяная корпорация NNPC получает миллиарды долларов, но почти не вкладывается в ремонт инфраструктуры. Коррупция и отсутствие контроля могли привести к тому, что старые трубы ржавеют десятилетиями.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo2_option2)

    @dp.callback_query(F.data == "delo2_option3")
    async def delo2_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "👥 **Местные боевики**\n\n"
            "В дельте Нигера действуют вооружённые группировки, которые требуют справедливого распределения нефтяных доходов. Они регулярно перекрывают трубопроводы, поджигают вышки и сливают нефть в реки как акт саботажа.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo2_option3)

    @dp.callback_query(F.data == "choose_delo2_option1")
    async def choose_delo2_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "✅ **ДЕЛО РАСКРЫТО!**\n\n"
            "Ты оказался прав. Расследование ЮНЕП подтвердило: компания Shell десятилетиями игнорировала коррозию трубопроводов в дельте Нигера. В 2021 году Shell согласилась выплатить жителям Огонланда €15 млн компенсации. Но реки остались чёрными. Экосистема будет восстанавливаться ещё 30 лет.\n\n"
            "📌 *Источник: Отчёт ЮНЕП «Environmental Assessment of Ogoniland» (2011), решение суда 2021 года*\n\n"
            "**Ты получаешь допуск к третьему, последнему делу!**"
        )
        await callback.message.answer(text, reply_markup=start__delo3)

    @dp.callback_query(F.data == "choose_delo2_option2")
    async def choose_delo2_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "Правительство Нигерии — не главный виновник. Оно коррумпировано, но основная ответственность лежит на Shell, которая управляла трубопроводами.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo2)

    @dp.callback_query(F.data == "choose_delo2_option3")
    async def choose_delo2_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "Боевики — это следствие проблемы, а не её причина. Основной источник загрязнения — старые трубы Shell, которые не ремонтировались.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo2)

    @dp.callback_query(F.data == "start_delo3")
    async def start_delo3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🕵️‍♂️ **ДЕЛО №3. ИСЧЕЗАЮЩИЙ ЛЕС**\n\n"
            "*Остров Калимантан, Индонезия. Ещё 30 лет назад здесь были джунгли — дом для орангутанов, дымчатых леопардов и тысяч видов растений. Сегодня — ровные ряды масличных пальм до горизонта.*\n\n"
            "Каждые 25 секунд в Индонезии исчезает лес размером с футбольное поле. Вырубка под плантации пальмового масла уничтожила уже более 10 млн гектаров. Торфяные болота осушены и горят, выбрасывая в атмосферу гигатонны углерода.\n\n"
            "ООН бьёт тревогу. Но кто настоящий заказчик этого преступления? Детективная группа получила три версии.\n\n"
            "**Твоя задача** — найти виновного. Выбери вариант:"
        )
        await callback.message.answer(text, reply_markup=delo3)

    @dp.callback_query(F.data == "delo3_option1")
    async def delo3_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🌴 **Местные фермеры**\n\n"
            "Миллионы индонезийских крестьян выжигают леса, чтобы посадить пальмы на своих участках. Они не думают об экологии — им нужно прокормить семьи. Это они поджигают торфяники в сухой сезон.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo3_option1)

    @dp.callback_query(F.data == "delo3_option2")
    async def delo3_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🏭 **Международные корпорации**\n\n"
            "Nestlé, Unilever, Procter & Gamble и другие гиганты покупают пальмовое масло тоннами. Их спрос создаёт рыночный спрос. Если бы они отказались от масла с вырубленных территорий, плантации не расширялись бы так быстро.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo3_option2)

    @dp.callback_query(F.data == "delo3_option3")
    async def delo3_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "🇮🇩 **Правительство Индонезии**\n\n"
            "Официальная Джакарта выдаёт лицензии на вырубку, продаёт концессии и получает миллиарды долларов налогов. Законы о защите лесов существуют только на бумаге, а в реальности коррупция позволяет срубить любое дерево за взятку.\n\n"

        )
        await callback.message.answer(text, reply_markup=confirm_delo3_option3)

    @dp.callback_query(F.data == "choose_delo3_option1")
    async def choose_delo3_option1(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "Фермеры — лишь мелкие игроки. 80% вырубки приходится на крупные плантации, а разрешения выдаёт правительство.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo3)

    @dp.callback_query(F.data == "choose_delo3_option2")
    async def choose_delo3_option2(callback: CallbackQuery):
        await callback.answer()
        text = (
            "❌ **НЕВЕРНО**\n\n"
            "Корпорации — соучастники, но главный преступник — правительство, которое выдаёт лицензии и закрывает глаза на незаконную вырубку.\n\n"
            "**Попробуй ещё раз!**"
        )
        await callback.message.answer(text, reply_markup=retry_delo3)

    @dp.callback_query(F.data == "choose_delo3_option3")
    async def choose_delo3_option3(callback: CallbackQuery):
        await callback.answer()
        text = (
            "✅ **ДЕЛО РАСКРЫТО!**\n\n"
            "Ты оказался прав. Именно правительство Индонезии держит в руках ключи от лесов. Коррупционные схемы позволяют чиновникам получать до $10 млрд в год от «зелёных взяток». Лесной патруль просто смотрит в другую сторону.\n\n"
            "📌 *Источник: Доклад ООН «The Palm Oil Paradox» (UNEP, 2020), Transparency International (2021)*\n\n"
            "**Ты раскрыл все три дела! Нажми «Завершить расследование», чтобы получить финальный вердикт.**"
        )
        await callback.message.answer(text, reply_markup=finish_game)

    @dp.callback_query(F.data == "finish_game")
    async def finish_game_handler(callback: CallbackQuery):
        await callback.answer()
        
        text = (
            "🕵️‍♀️ **ФИНАЛЬНЫЙ ВЕРДИКТ ООН**\n\n"
            "Три дела. Три настоящих экопреступления. Ты доказал, что климатический кризис — не случайность, а результат чьих-то решений и чьей-то жадности.\n\n"
            "📊 **Твоя статистика:**\n"
            "— Раскрыто дел: 3 из 3\n"
            "— Звание: Хранитель климата\n\n"
            "🌍 **Что дальше?**\n"
            "Ты можешь:\n\n"
            "Нажать «📊 Факты», чтобы узнать больше о климатическом кризисе\n\n"
            "Переслать этого бота другу — пусть тоже попробует раскрыть дела\n\n"
            "*Планета ждёт таких детективов, как ты.*"
        )
        
        await callback.message.answer(text, reply_markup=main_keyboard)