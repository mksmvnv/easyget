from aiogram.utils.keyboard import ReplyKeyboardBuilder

from core.utils.enums import Menu


def main_menu_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text=Menu.order)
    keyboard_builder.button(text=Menu.calculator)
    keyboard_builder.button(text=Menu.current_exchange_rate)
    keyboard_builder.button(text=Menu.reviews)
    keyboard_builder.button(text=Menu.about)
    keyboard_builder.button(text=Menu.faq)
    keyboard_builder.button(text=Menu.manager)
    keyboard_builder.adjust(1, 2, 2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)
