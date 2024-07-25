class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, user='admin', passwd='a'):
        self.page.goto("http://localhost:5173/jalisweb/login")
        self.page.get_by_label("Usuário").click()
        self.page.get_by_label("Usuário").fill(user)
        self.page.get_by_label("Senha").click()
        self.page.get_by_label("Senha").fill(passwd)
        self.page.get_by_role("button", name="Entrar").click()
