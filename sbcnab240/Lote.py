class Lote(object):

    def __init__(self):

        self.tipo_inscricao = None
        self.numero_inscricao = None
        self.nome_beneficiario = None
        self.cod_transmissao = None
        self.mensagem_1 = None
        self.mensagem_2 = None
        self.num_remessa = None
        self.data_gravacao = None

        self.boletos = []


    def carrega_header(self, valores):

        self.tipo_inscricao = valores['tipo_inscricao']
        self.numero_inscricao = valores['numero_inscricao']
        self.nome_beneficiario = valores.get('nome_beneficiario')
        self.data_gravacao = valores['data_gravacao']
        #self.cod_transmissao = valores['cod_transmissao']


    def carrega_trailer(self, valores):
        pass


    def adiciona_boletos(self, boletos):
        self.boletos.extend(boletos)
