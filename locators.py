# Страница регистрации
REGISTER_NAME = "//label[text()='Имя']/..//input"
FIELD_EMAIL = "//label[text()='Email']/..//input"
FIELD_PASSWORD = "//label[text()='Пароль']/..//input"
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"
REGISTER_LINK = "//a[text()='Зарегистрироваться']"
INCORRECT_PASSWORD_ERROR = "//p[text()='Некорректный пароль']"
LOGIN_LINK = "//a[text()='Войти']"

# Страница входа
LOGIN_BUTTON = "//button[text()='Войти']"
FORGOT_PASSWORD_LINK = "//a[text()='Восстановить пароль']"

# Главная страница
LOGIN_BUTTON_MAIN = "//button[text()='Войти в аккаунт']"
PERSONAL_ACCOUNT_BUTTON = "//p[text()='Личный Кабинет']"
CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']"
LOGO = "//div[contains(@class,'AppHeader_header__logo')]//a"

# Вкладки
TAB_BUNS = "//span[text()='Булки']/.."
TAB_SAUCES = "//span[text()='Соусы']/.."
TAB_FILLINGS = "//span[text()='Начинки']/.."

SECTION_BUNS = "//h2[text()='Булки']"
SECTION_SAUCES = "//h2[text()='Соусы']"
SECTION_FILLINGS = "//h2[text()='Начинки']"

# Личный кабинет
LOGOUT_BUTTON = "//button[text()='Выход']"