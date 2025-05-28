from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.enums import InlineButton, CallbackInfo
from utils.callback_data import Category, City, Pagination, Link

from data.config import settings


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.sneakers,
        callback_data=Category(
            name=CallbackInfo.sneakers,
            logistics=settings.logistics.sneakers,
        ),
    )
    keyboard_builder.button(
        text=InlineButton.jackets,
        callback_data=Category(
            name=CallbackInfo.jackets,
            logistics=settings.logistics.jackets,
        ),
    )
    keyboard_builder.button(
        text=InlineButton.other_category,
        callback_data=Category(
            name=CallbackInfo.other,
            logistics=settings.logistics.other,
        ),
    )
    keyboard_builder.button(
        text=InlineButton.return_to_main_menu,
        callback_data=Pagination(page=CallbackInfo.main_menu),
    )
    keyboard_builder.adjust(1, 1, 1, 1)
    return keyboard_builder.as_markup()


def city_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.moscow,
        callback_data=City(name=CallbackInfo.moscow),
    )
    keyboard_builder.button(
        text=InlineButton.spb,
        callback_data=City(name=CallbackInfo.spb),
    )
    keyboard_builder.button(
        text=InlineButton.other_city,
        callback_data=City(name=CallbackInfo.other),
    )
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()


def show_reviews():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.show,
        url=settings.links.reviews,
        callback_data=Link(path=CallbackInfo.reviews),
    )
    keyboard_builder.button(
        text=InlineButton.return_to_main_menu,
        callback_data=Pagination(page=CallbackInfo.main_menu),
    )
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def show_faq():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.show,
        url=settings.links.home,
        callback_data=Link(path=CallbackInfo.faq),
    )
    keyboard_builder.button(
        text=InlineButton.return_to_main_menu,
        callback_data=Pagination(page=CallbackInfo.main_menu),
    )
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def cancel_order():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.cancel,
        callback_data=Pagination(page=CallbackInfo.main_menu),
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def return_to_main_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text=InlineButton.return_to_main_menu,
        callback_data=Pagination(page=CallbackInfo.main_menu),
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
