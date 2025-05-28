from enum import StrEnum


class MainButton(StrEnum):
    order = "⚡ Заказать"
    calculator = "🧮 Калькулятор"
    current_exchange_rate = "💰 Актуальный курс"
    reviews = "📃 Отзывы"
    about = "📌 О нас"
    faq = "🛟 FAQ"
    manager = "👨‍💼 Задать вопрос"


class InlineButton(StrEnum):
    sneakers = "👟 Кроссовки"
    jackets = "🧥 Пуховики"
    other_category = "💻 Другое"
    moscow = "🏢 Москва"
    spb = "🏛 Санкт-Петербург"
    other_city = "🏝 Другой город"
    show = "🔎 Показать"
    cancel = "🚫 Отменить заказ"
    return_to_main_menu = "↩ Назад в главное меню"


class CallbackInfo(StrEnum):
    sneakers = "Кроссовки"
    jackets = "Пуховики"
    moscow = "Москва"
    spb = "Санкт-Петербург"
    other = "Другое"
    reviews = "Отзывы"
    faq = "FAQ"
    main_menu = "Главное меню"
