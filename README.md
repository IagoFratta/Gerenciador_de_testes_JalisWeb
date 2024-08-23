# Gerenciador de Testes JalisWeb

## Descrição

O Gerenciador de Testes JalisWeb é uma aplicação para automatizar testes de uma aplicação web chamada JalisWeb. Ele utiliza a biblioteca Playwright para interagir com a interface web e executar testes automatizados. A interface do usuário é construída com Vue.js e o servidor backend é gerenciado com Flask.

bash
Copiar código

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/Gerenciador_de_testes_JalisWeb.git
   cd Gerenciador_de_testes_JalisWeb
   ```
Crie e ative um ambiente virtual:

  ```bash
  python -m venv .venv
  //No Windows, use
 .venv\Scripts\activate
  ```

2. Instale as dependências:

   ```bash
     pip install -r requirements.txt
   ```
Inicie o servidor Flask:

```bash
   flask run
```
Utilização
Interface Web
Acesse http://localhost:5000 no seu navegador para abrir a interface web. Nesta interface, você pode configurar e iniciar os testes automatizados.

API
GET /get-data: Obtém os dados de configuração atuais.
POST /run-tests: Inicia a execução dos testes com os dados fornecidos.
Configuração dos Testes
Os testes são configurados através do formulário na interface web. Preencha os campos necessários e clique no botão para executar os testes.

Campos do Formulário
client_id: ID único do cliente.
url_jalisweb: URL do JalisWeb.
usuario: Nome de usuário para login.
senha: Senha para login.
quantidade_de_requisicoes: Quantidade de requisições a serem criadas.
paciente: Nome do paciente.
exame: Tipo de exame.
lab: Laboratório.
criar_requisicao: Checkbox para criar requisição.
criar_lote: Checkbox para criar lote.
estornar_lote: Checkbox para estornar lote.
is_lote_webservice: Checkbox para indicar se é um lote webservice.
Exemplo de Uso do Formulário
html
Copiar código
<div id="app">
    <form @submit.prevent="submitForm">
        <!-- Outros campos do formulário -->
        <div class="form-group">
            <input class="checkbox" type="checkbox" v-model="form.criar_requisicao" id="criar_requisicao">
            <label for="criar_requisicao">Criar Requisição</label><br>
        </div>
        <div class="form-group">
            <input class="checkbox" type="checkbox" v-model="form.criar_lote" id="criar_lote">
            <label for="criar_lote">Criar Lote</label><br>
        </div>
        <div class="form-group">
            <input class="checkbox" type="checkbox" v-model="form.estornar_lote" id="estornar_lote">
            <label for="estornar_lote">Estornar Lote</label><br>
        </div>
        <div class="form-group">
            <input class="checkbox" type="checkbox" v-model="form.is_lote_webservice" id="is_lote_webservice">
            <label for="is_lote_webservice">É Lote Webservice</label><br>
        </div>
        <button type="submit">Executar Testes</button>
    </form>
</div>
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

css
Copiar código

Esse `README.md` cobre os principais aspectos do seu projeto, incluindo a descrição, a estrutura, a instalação, a utilização, a configuração dos testes e como contribuir. Ajuste conforme necessário para refletir com precisão os detalhes específicos do seu projeto.
Faça no formato .md
