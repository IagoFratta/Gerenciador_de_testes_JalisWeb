import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


class CriarLotePage:
    def __init__(self, page):
        self.page = page
    
    def criar_lote(self, paciente, laboratorio):
        self.selecionar_laboratorio(laboratorio)
        self.selecionar_requisicao_para_lote(paciente)
        self.enviar_lote()
        
    def selecionar_laboratorio(self, laboratorio):
        expect(self.page.get_by_role("banner")).to_contain_text("Triagem/Criar lote")
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
        self.page.get_by_role("button", name="Criar Lote").click()
        splash_locator = self.page.locator("text=Gerando lote...")

    # Espera o splash desaparecer (ou seja, que o splash não esteja mais visível)
        splash_locator.wait_for(state="hidden")

    # Continuar com o restante do teste
        print("Splash desapareceu, continuando o teste...")
        self.page.bring_to_front()
        expect(self.page.locator("body")).to_contain_text("Deseja criar outro lote para o laboratório ")
        self.page.get_by_role("button", name="Não").click()

