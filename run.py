from models.db import session
from models.db.base import SessionManager
from models.menu import UserMenu
from models.service import ShopService
from models.storage import MemoryStorage


if __name__ == "__main__":
    session.init_engine("sqlite:///db.sqlite_store")
    session.create_tables()

    # session2 = SessionManager()
    # if id(session) == id(session2):
    #     print("Singleton works")
    # else:
    #     print("There is no Singleton")

    memory_storage = MemoryStorage()

    menu = UserMenu(storage=memory_storage)
    service = ShopService(storage=memory_storage)

    menu.add_menu_category(
        name="Товары",
        callback=service.display_products,
        login_required=False,
    )
    menu.add_menu_category(
        name="Войти",
        callback=service.login,
        login_required=False,
    )
    menu.add_menu_category(
        name="Зарегистрироваться",
        callback=service.register,
        login_required=False,
    )
    menu.add_menu_category(
        name="Сменить пользователя",
        callback=service.change_user,
        login_required=True,
    )
    menu.add_menu_category(
        name="Тикет",
        callback=service.submit_ticket,
        login_required=True,
    )
    menu.add_menu_category(
        name="Купить",
        callback=service.buy_product,
        login_required=True,
    )
    menu.add_menu_category(
        name="Профиль",
        callback=service.profile,
        login_required=True,
    )
    menu.add_menu_category(
        name="Закрыть программу",
        callback=service.close_program,
        login_required=True and False,
    )

    while True:
        menu.display_categories()
        menu.handler()
        if print("Программа закрыта"):  # непонятно, как выйти в данном случае из бесконечного цикла
            break
