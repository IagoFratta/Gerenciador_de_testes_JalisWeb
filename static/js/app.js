new Vue({
    el: '#app',
    data: {
        form: {
            url_jalisweb: '',
            usuario: '',
            senha: '',
            quantidade_de_requisicoes: Number,
            paciente: '',
            exame: '',
            lab: '',
            criar_requisicao: false,
            criar_lote: false,
            estornar_lote: false,
            is_lote_webservice: false
        }
    },
    created() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            axios.get('/get-data')
                .then(response => {
                    if (Object.keys(response.data).length > 0) {
                        this.form = response.data;
                    }
                })
                .catch(error => {
                    console.error('Erro ao buscar os dados:', error);
                });
        },
        submitForm() {
            axios.post('/run-tests', this.form)
                .then(response => {
                    alert('Testes executados com sucesso!');
                })
                .catch(error => {
                    console.error('Erro ao executar os testes:', error);
                });
        }
    }
});
