from playwright.sync_api import expect

class EstornarLotePage:
    def __init__(self, page):
        self.page = page
        
    def estornar_lote(self, laboratorio, usuario, is_webservice):
        self.selecionar_laboratorio(laboratorio)
        self.selecionar_lote_para_estorno(usuario) 
        self.clicar_estornar_todos(laboratorio, is_webservice)   
        
    def selecionar_laboratorio(self, laboratorio):
        expect(self.page.get_by_role("banner")).to_contain_text("Triagem/Estornar lote")
        self.page.get_by_role("button", name="Novo").click()
        self.page.locator("div:nth-child(3) > .v-field__input").click()
        self.page.get_by_text(laboratorio).click()
        
    def selecionar_lote_para_estorno(self, usuario):
        self.page.locator("form").filter(has_text="Cod. LoteCod. Lote").locator("svg").click()
        self.page.get_by_role("button", name="Adicionar filtro").click()
        self.page.get_by_text("Usuário").click()
        self.page.get_by_label("Usuário").click()
        self.page.get_by_label("Usuário").fill(usuario)
        self.page.get_by_role("button", name="Pesquisar").click()
        print(self.page.get_by_role("row").nth(1).get_by_role("cell").nth(0).inner_text())
        self.page.get_by_role("row").nth(1).get_by_role("button").click()
        

    def clicar_estornar_todos(self, laboratorio, is_webservice):
        self.page.get_by_role("button", name="Estornar todos").click()
        expect(self.page.get_by_text("O lote será excluído,")).to_be_visible()
        self.page.get_by_role("button", name="Sim").click()
        expect(self.page.get_by_text("O estorno desmarcará todos os")).to_be_visible()
        self.page.get_by_role("button", name="Sim").click()
        
        if (not is_webservice):
            expect(self.page.get_by_text("O estorno deste lote será realizado apenas no sistema")).to_be_visible()
            self.page.get_by_role("button", name="OK").click()
            
        if (laboratorio == "Alvaro Laboratorio"):
            expect(self.page.get_by_text("Etiquetas para multiguia")).to_be_visible()
            self.page.get_by_role("button", name="OK").click()
        expect(self.page.get_by_text("Lote estornado com sucesso.")).to_be_visible()

