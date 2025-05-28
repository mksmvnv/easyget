from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.enums import MainButton


def main_menu_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text=MainButton.order)
    keyboard_builder.button(text=MainButton.calculator)
    keyboard_builder.button(text=MainButton.current_exchange_rate)
    keyboard_builder.button(text=MainButton.reviews)
    keyboard_builder.button(text=MainButton.about)
    keyboard_builder.button(text=MainButton.faq)
    keyboard_builder.button(text=MainButton.manager)
    keyboard_builder.adjust(1, 2, 2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)
