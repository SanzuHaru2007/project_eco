from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧠 Детектив"), KeyboardButton(text="📊 Факты")],
    ],
    resize_keyboard=True
)

random_fact_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Случайный факт", callback_data="random_fact")]
    ]
)

delo1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Россия", callback_data="delo1_option1")],
        [InlineKeyboardButton(text="🇸🇦 Саудовская Аравия", callback_data="delo1_option2")],
        [InlineKeyboardButton(text="🇺🇸 США", callback_data="delo1_option3")]
    ]
)

delo2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛢️ Royal Dutch Shell", callback_data="delo2_option1")],
        [InlineKeyboardButton(text="🏛️ Правительство Нигерии", callback_data="delo2_option2")],
        [InlineKeyboardButton(text="👥 Местные боевики", callback_data="delo2_option3")]
    ]
)

delo3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌴 Местные фермеры", callback_data="delo3_option1")],
        [InlineKeyboardButton(text="🏭 Международные корпорации", callback_data="delo3_option2")],
        [InlineKeyboardButton(text="🇮🇩 Правительство Индонезии", callback_data="delo3_option3")]
    ]
)

start_det = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать первое дело", callback_data="start_delo1")]
    ]
)

start__delo2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать второе дело", callback_data="start__delo2")]
    ]
)

start__delo3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать третье дело", callback_data="start__delo3")]
    ]
)

confirm_delo1_option1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Россию", callback_data="choose_delo1_option1")]
    ]
)

confirm_delo1_option2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Саудовскую Аравию", callback_data="choose_delo1_option2")]
    ]
)

confirm_delo1_option3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать США", callback_data="choose_delo1_option3")]
    ]
)

confirm_delo2_option1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Royal Dutch Shell", callback_data="choose_delo2_option1")]
    ]
)

confirm_delo2_option2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Правительство Нигерии", callback_data="choose_delo2_option2")]
    ]
)

confirm_delo2_option3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Местные боевики", callback_data="choose_delo2_option3")]
    ]
)

confirm_delo3_option1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Местные фермеры", callback_data="choose_delo3_option1")]
    ]
)

confirm_delo3_option2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Международные корпорации", callback_data="choose_delo3_option2")]
    ]
)

confirm_delo3_option3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать Правительство Индонезии", callback_data="choose_delo3_option3")]
    ]
)

retry_delo1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться", callback_data="start_delo1")]
    ]
)

retry_delo2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться", callback_data="start_delo2")]
    ]
)

retry_delo3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться", callback_data="start_delo3")]
    ]
)

finish_game = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Завершить расследование", callback_data="finish_game")]
    ]
)