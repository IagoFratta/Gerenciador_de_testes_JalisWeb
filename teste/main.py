import re
from playwright.sync_api import Playwright, sync_playwright, expect
from criar_lote import CriarLotePage
from criar_requisicao import RequisicaoPage
from login import LoginPage
from estornar_lote import EstornarLotePage

class JalisWeb:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.criar_lote_page = CriarLotePage(page)
        self.requisicao_page = RequisicaoPage(page)
        self.estornar_lote_page = EstornarLotePage(page)
        
    def navegar(self, menu_principal, submenu):
        self.page.locator(".app-logo").click()
        expect(self.page.locator("div").filter(has_text=re.compile(rf"^{menu_principal}$")).locator("svg").first).to_be_visible()
        self.page.locator("div").filter(has_text=re.compile(rf"^{menu_principal}$")).click()
        expect(self.page.get_by_role("link", name=submenu)).to_be_visible()
        self.page.get_by_role("link", name=submenu).click()
        
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    usuario = 'admin'
    senha = 'a'
    
    menu = ['Recepção', 'Triagem']
    submenu = ["Requisições", "Criar lote", "Estornar lote"]
    
    criar_requisicao = True
    criar_lote = True
    estornar_lote = False
    is_lote_webservice = True
    
    quantidade_de_requisicoes = 1
    paciente = 'Teste apoio'
    exame = ["DB"]
    
    laboratorios = ["Alvaro Laboratorio", "DB", "Hermes Pardini Laboratório"]
    lab = laboratorios[1]
    
    jalis_web = JalisWeb(page)
    jalis_web.login_page.login(usuario, senha)
    
    if criar_requisicao:
        jalis_web.navegar(menu[0], submenu[0])
        for i in range(quantidade_de_requisicoes):
            jalis_web.requisicao_page.criar_requisicao(exame, paciente)
    
    if criar_lote:
        jalis_web.navegar(menu[1], submenu[1])
        jalis_web.criar_lote_page.criar_lote(paciente, lab)
        page.bring_to_front()
        
    if estornar_lote:
        jalis_web.navegar(menu[1], submenu[2])
        jalis_web.estornar_lote_page.estornar_lote(lab, usuario, is_lote_webservice)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
