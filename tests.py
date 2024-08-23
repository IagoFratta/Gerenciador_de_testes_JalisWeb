from playwright.sync_api import sync_playwright, expect
from teste.criar_lote import CriarLotePage
from teste.criar_requisicao import RequisicaoPage
from teste.login import LoginPage
from teste.estornar_lote import EstornarLotePage
import re

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

def run_tests(data):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={ 'width': 1366, 'height': 768 })
        page = context.new_page()

        jalis_web = JalisWeb(page)
        jalis_web.login_page.login(data['url_jalisweb'], data['usuario'], data['senha'])

        if data['criar_requisicao']:
            jalis_web.navegar('Recepção', 'Requisições')
            quantidade_de_requisicoes = int(data['quantidade_de_requisicoes'])
            for _ in range(quantidade_de_requisicoes):
                jalis_web.requisicao_page.criar_requisicao(data['exame'], data['paciente'])

        if data['criar_lote']:
            jalis_web.navegar('Triagem', 'Criar lote')
            jalis_web.criar_lote_page.criar_lote(data['paciente'], data['lab'])
            page.bring_to_front()

        if data['estornar_lote']:
            jalis_web.navegar('Triagem', 'Estornar lote')
            jalis_web.estornar_lote_page.estornar_lote(data['lab'], data['usuario'], data['is_lote_webservice'])

        context.close()
        browser.close()
