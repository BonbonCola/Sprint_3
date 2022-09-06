# главная страница
account_button = "//p[contains(text(),'Личный Кабинет')]" # кнопка Личный кабинет в хэдере
entrance_to_account_button = "//button[contains(text(),'Войти в аккаунт')]" # кнопка Войти в аккаунт на главной
make_order = "//button[contains(text(),'Оформить заказ')]" # кнопка Оформить заказ на главной
constructor_link = "//p[contains(text(),'Конструктор')]" # линк на конструктор в хэдере
burger_ing_list = "//h1[contains(text(),'Соберите бургер')]" # список ингридиентов в конструкторе
logo = "//header//div[@class = 'AppHeader_header__logo__2D0X2']" # логотип
nachinki = "//span[contains(text(),'Начинки')]" # линк в раздел с Начинками
nachinki_header = "//h2[contains(text(),'Начинки')]" # заголовок раздела с Начинками
bulki = "//span[contains(text(),'Булки')]" # линк в раздел с Булками
bulki_header = "//h2[contains(text(),'Булки')]" # заголовок раздела с Булками
soys = "//span[contains(text(),'Соусы')]" #линк на раздел с Соусами
soys_header = "//h2[contains(text(),'Соусы')]" # заголовок раздела с Соусами


# страница авторизации
email_input = "//body/div[@id='root']//input[@type='text']" #поле ввода емейла
password_input = "//body/div[@id='root']//input[@type='password']" #поле ввода пароля
entrance_button = "//button[contains(text(),'Войти')]" #кнопка входа
registration_link = "//a[contains(text(),'Зарегистрироваться')]" # линк на страницу регистрации
restore_password_link = "//a[contains(text(),'Восстановить пароль')]" # линк на страницу восстановления пароля

# страница регистрации / восстановления пароля
entrance_link = "//a[contains(text(),'Войти')]" # линк на страницу входа
# поле ввода имени и емейла - одинаковые, я не нашла за что зацепиться для каждого поля отдельно не используя индексы элементов из dom((
# возможно, в продакшене можно как то договориться с фронтами, чтобы такого не было. Но здесь это проект студента Практикума на курсе «React-разработчик».
registration_name_input = "//body/div[@id='root']//input[@type='text']" # поле ввода имени
registration_email_input = "//body/div[@id='root']//input[@type='text']" # поле ввода емейла
registration_password_input = "//body/div[@id='root']//input[@type='password']" # поле ввода пароля
registration_button = "//button[contains(text(),'Зарегистрироваться')]" # кнопка Регистрации
invalid_password_error_label = "//p[contains(text(),'Некорректный пароль')]" # сообщение о некорректном пароле

# страница Личного кабинета авторизованного пользователя
profile_label = "//a[contains(text(),'Профиль')]" #надпись Профиль
history_label = "//a[contains(text(),'История заказов')]" #надпись История заказов
exit_button = "//button[contains(text(),'Выход')]" #кнопка Выход
