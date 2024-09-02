from asyncio import timeout
from playwright.sync_api import expect


class CriarLotePage:
    def __init__(self, page):
        self.page = page
        self.titulo = self.page.locator("h1", has_text="Triagem/Criar lote")
    
    def criar_lote(self, paciente, laboratorio):
        self.selecionar_laboratorio(laboratorio)
        self.selecionar_requisicao_para_lote(paciente)
        self.enviar_lote()
        
    def selecionar_laboratorio(self, laboratorio):
        expect(self.titulo)
        self.page.get_by_role("button", name="Novo").click()
        self.page.locator("div:nth-child(3) > .v-field__input").click()
        self.page.get_by_text(laboratorio).click()
    
    def selecionar_requisicao_para_lote(self, paciente):
        self.page.locator("form").filter(has_text="Cód. RequisiçãoCód. Requisição").locator("svg").click()
        self.page.get_by_label("Nome do Paciente").click()
        self.page.get_by_label("Nome do Paciente").fill(paciente)
        self.page.get_by_role("button", name="Pesquisar").click()
        self.page.locator("td:nth-child(7)").first.click()
        
    def enviar_lote(self):
        if self.page.locator("div.v-card-title", has_text="Dados adicionais").is_visible():
            print("Entrou no if")
            self.page.get_by_label("", exact=True).fill("1")
            self.page.get_by_role("button", name="Ok").click()
                
        self.page.get_by_role("button", name="Criar Lote").click()
        splash_locator = self.page.locator("text=Gerando lote...")
        splash_locator.wait_for(state="hidden")
        print("Splash desapareceu, continuando o teste...")
        self.page.bring_to_front()
        expect(self.page.locator("body")).to_contain_text("Deseja criar outro lote para o laboratório ", timeout = 50000)
        self.page.get_by_role("button", name="Não").click()

