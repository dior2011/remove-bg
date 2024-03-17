from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Bizning kurslar",callback_data="courses"),
    InlineKeyboardButton(text="Bizning manzil",callback_data="location"),],

    [InlineKeyboardButton(text="Biz haqimizda",callback_data="about-us"),],

    [InlineKeyboardButton(text="Admin bilan bog'lanish",callback_data="contact-admin"),]

    ]
)

courses_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Frontend",callback_data="frontend"),
    InlineKeyboardButton(text="Backend",callback_data="backend"),],

    [InlineKeyboardButton(text="Online kurslar",url="https://www.youtube.com/watch?v=D9LwKc223t4"),],
    [InlineKeyboardButton(text="ortga",callback_data="back")]

    ]
)

ortga = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ortga",callback_data="back-courses")]
    ]
)

ortga_umumiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ortga",callback_data="back")]
    ]
)

colours_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="black",callback_data="black"),
         InlineKeyboardButton(text="blue",callback_data="blue"),
         ],
        [InlineKeyboardButton(text="green",callback_data="green"),
         InlineKeyboardButton(text="red",callback_data="red"),
         ],
        [InlineKeyboardButton(text="brown", callback_data="brown"),
         InlineKeyboardButton(text="yellow", callback_data="yellow"),
         ],
        [InlineKeyboardButton(text="pink", callback_data="pink"),
         InlineKeyboardButton(text="purple", callback_data="purple"),
        ],
        [InlineKeyboardButton(text="Ortga", callback_data="back")]
    ]
)
#ikkinchi usul
# numbers = InlineKeyboardBuilder()

# for number in range(1,16):
#     numbers.add(InlineKeyboardButton(text=f"{number}",callback_data=f"{number}"))

# numbers.adjust(2)

# num_inline_menu = numbers.as_markup()