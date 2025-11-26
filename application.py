class Application:
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        open_page(page)
        log_in(page, Group("Guskov-AV", "Kotopes1"))
        open_users_deactiv(page)
        open_social(page)
        open_ind_social_lgoty(page)
        open_org(page)
        open_ref_org(page, "Тестовая компания Венделеевка")

        # ---------------------
        context.close()
        browser.close()

    def open_ref_org(page, name_org):
        #  просмотр и редактирование организации
        page.get_by_text("Тестовая организация").first.dblclick()
        page.get_by_role("button", name="Редактировать").click()
        page.get_by_role("textbox", name="Полное название").click()
        page.get_by_role("textbox", name="Полное название").fill(name_org)
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("button", name="К списку").click()

    def open_org(page):
        #  открытие раздела Организации
        page.get_by_role("link", name=" Организации").click()

    def open_ind_social_lgoty(page):
        #  просмотр льготника и льготы
        page.locator("tbody div").filter(has_text="город Брянск").nth(2).dblclick()
        page.get_by_role("cell", name=" ").locator("a").first.click()
        page.get_by_role("button", name="К списку").click()
        page.get_by_role("button", name="К поиску").click()

    def open_social(page):
        #  открытие раздела Льготники
        page.get_by_role("link", name=" Льготники").click()

    def open_users_deactiv(page):
        #  открытие раздела Пользователи и деативация записи
        page.get_by_role("link", name=" Пользователи").click()
        page.locator(
            ".el-table__row.hover-row > .el-table_1_column_1 > .cell > .bootstrap-switch > .bootstrap-switch-container > .bootstrap-switch-label").first.click()

    def log_in(page, group):
        #  авторизация
        page.get_by_role("textbox", name="Логин").fill(group.username)
        page.get_by_role("textbox", name="Пароль").click()
        page.get_by_role("textbox", name="Пароль").fill(group.password)
        page.get_by_role("button", name="Войти").click()

    def open_page(page):
        #  открытие страницы авторизации
        page.goto("https://test-tkp-sp.secgw.ru/#/login")

    with sync_playwright() as playwright:
        run(playwright)