import re
from playwright.sync_api import expect

class RequisicaoPage:
    def __init__(self, page):
        self.page = page

    def selecionar_exame(self, exame):
            self.page.get_by_label("Exame", exact=True).fill(exame)
            self.page.get_by_text(exame, exact=True).click()
            self.page.get_by_role("button", name="OK").click()
            expect(self.page.get_by_role("listbox").get_by_text("1", exact=True)).to_be_visible()

    def pesquisar_paciente(self, paciente):
        self.page.get_by_label("Nome").click()
        self.page.get_by_label("Nome").fill(paciente)
        self.page.get_by_role("button", name="Pesquisar").click()


    def _handle_dialogs(self):
        expect(self.page.locator("body")).to_contain_text("Deseja adicionar uma nova requisição para o paciente?")
        if self.page.locator("text=Deseja adicionar uma nova requisição para o paciente?").is_visible():
            self.page.get_by_role("button", name="Não").click()

        expect(self.page.locator("body")).to_contain_text("Requisição gravada com o código")     
        if self.page.locator("body", has_text="Requisição gravada com o código").is_visible():
            v_card_text_div = self.page.locator("div.v-card-text:has-text('Requisição gravada com o código')")
            dialog_text = v_card_text_div.inner_text()
            print(dialog_text)
            self.page.get_by_role("button", name="OK").nth(1).click()
    
    def criar_requisicao(self, exame, paciente):
        expect(self.page.get_by_role("banner")).to_contain_text("Recepção/Requisições")
        expect(self.page.get_by_role("button", name="1")).to_be_visible()
        self.page.get_by_role("button", name="Novo").click()
        self.pesquisar_paciente(paciente)
        self.page.get_by_role("row").nth(1).get_by_role("button").click()
        self.page.wait_for_timeout(1000)
        expect(self.page.get_by_text("O paciente está cadastrado com o convênio")).to_be_visible()
        self.page.get_by_role("button", name="Sim").click()
        self.page.wait_for_timeout(1000)
        expect(self.page.get_by_text("O paciente está cadastrado com o médico")).to_be_visible()
        self.page.get_by_role("button", name="Sim").click()
        self.page.get_by_role("button", name="Próximo").click()
        expect(self.page.get_by_label("Matrícula")).to_be_visible()
        self.page.get_by_role("button", name="Próximo").click()
        self.selecionar_exame(exame)
        self.page.get_by_role("button", name="Salvar").click()
        self._handle_dialogs()
            