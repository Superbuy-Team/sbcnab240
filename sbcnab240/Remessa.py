from Lote import Lote
from Boleto import Boleto, Cedente

class Remessa(object):

    def __init__(self):
        self.codigo_banco = None
        self.lote_servico = None
        self.tipo_inscricao = None
        self.numero_inscricao = None
        self.nome_empresa = None
        self.nome_banco = None
        self.cod_remessa = None
        self.data_geracao = None
        self.num_sequencial = None

        self.lotes = []


    def carrega_campos(self, specs, campos):

        lotes = []
        lote_atual = None
        boletos = []
        boleto_atual = None

        for secao, valores in campos:
            if   secao == "HeaderArquivoRemessa":
                self.codigo_banco = valores['codigo_banco']
                self.lote_servico = valores['lote_servico']
                self.tipo_inscricao = valores['tipo_inscricao']
                self.numero_inscricao = valores['numero_inscricao']
                self.nome_empresa = valores['nome_empresa']
                self.nome_banco = valores['nome_banco']
                self.cod_remessa = valores['cod_remessa']
                self.data_geracao = valores['data_geracao']
                self.num_sequencial = valores['num_sequencial']

            elif secao == "HeaderLoteRemessa":
                if not lote_atual:
                    lote_atual = Lote()
                    lote_atual.carrega_header(valores)
                    lotes.append(lote_atual)

            elif secao[:8] == "Segmento":
                if secao == "SegmentoP":
                    boleto_atual = Boleto()
                    boleto_atual.dataProcessamento = self.data_geracao

                    cedente = Cedente()

                    cedente.tipoDocumento = lote_atual.tipo_inscricao
                    cedente.documento = lote_atual.numero_inscricao
                    cedente.nome = lote_atual.nome_beneficiario

                    boleto_atual.cedente = cedente

                    boletos.append(boleto_atual)

                if boleto_atual:
                    boleto_atual.carrega_segmento(specs, secao[8:], valores)

            elif secao == "TrailerLoteRemessa":
                # adiciona boletos atuais ao lote
                lote_atual.adiciona_boletos(boletos)

                # reseta lista de boletos
                boletos = []
                boleto_atual = None

                # checa lote
                # TODO

                # adiciona lote a remessa
                self.lotes.append(lote_atual)

                # reseta lote
                lote_atual = None

            elif secao == "TrailerArquivoRemessa":
                # reseta lotes
                lotes = []
