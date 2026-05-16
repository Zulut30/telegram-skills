from aiogram.types import InlineKeyboardButton as B
from aiogram.types import InlineKeyboardMarkup as K


def main_menu_kb() -> K:
    return K(
        inline_keyboard=[
            [B(text="📚 Контент", callback_data="menu:content")],
            [
                B(text="💎 VIP", callback_data="menu:vip"),
                B(text="👤 Профиль", callback_data="menu:profile"),
            ],
        ]
    )


def _back_to_menu_button() -> B:
    return B(text="← Назад", callback_data="menu:main")


def back_to_menu_kb() -> K:
    return K(inline_keyboard=[[_back_to_menu_button()]])


def vip_buy_kb(stars: int) -> K:
    return K(
        inline_keyboard=[
            [B(text=f"Купить VIP за {stars} ⭐", callback_data="vip:buy")],
            [_back_to_menu_button()],
        ]
    )
