# главная страница
account_button = "//p[contains(text(),'Личный Кабинет')]" # кнопка Личный кабинет в хэдере
entrance_to_account_button = "//button[contains(text(),'Войти в аккаунт')]" # кнопка Войти в аккаунт на главной
make_order = "//button[contains(text(),'Оформить заказ')]" # кнопка Оформить заказ на главной

# страница авторизации
email_input = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]" #поле ввода емейла
password_input = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]" #поле ввода пароля
entrance_button = "//button[contains(text(),'Войти')]" #кнопка входа
registration_link = "//a[contains(text(),'Зарегистрироваться')]" # линк на страницу регистрации
restore_password_link = "//a[contains(text(),'Восстановить пароль')]" # линк на страницу восстановления пароля

# страница регистрации / восстановления пароля
entrance_link = "//a[contains(text(),'Войти')]" # линк на страницу входа
registration_name_input = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]" # поле ввода имени
registration_email_input = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]" # поле ввода емейла
registration_password_input = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]" # поле ввода пароля
registration_button = "//button[contains(text(),'Зарегистрироваться')]" # кнопка Регистрации
invalid_password_error_label = "//p[contains(text(),'Некорректный пароль')]" # сообщение о некорректном пароле

# страница Личного кабинета авторизованного пользователя
profile_label = "//a[contains(text(),'Профиль')]" #надпись Профиль
history_label = "//a[contains(text(),'История заказов')]" #надпись История заказов
exit_button = "//button[contains(text(),'Выход')]" #кнопка Выход
