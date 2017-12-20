TIPO_DOCUMENTO_CPF = 1
TIPO_DOCUMENTO_CNPJ = 2


class Cedente(object):

    def __init__(self):
        self.tipoDocumento = None
        self.documento = None
        self.nome = None
        self.agencia = None
        self.agenciaDigito = None
        self.conta = None
        self.contaDigito = None
        self.convenio = None
        self.convenioDigito = None

    @property
    def documentoTexto(self):
        if self.tipoDocumento == 1:
            return '%011d' % self.documento
        elif self.tipoDocumento == 2:
            return '%014d' % self.documento
        else:
            return str(self.documento)


class Sacado(object):

    def __init__(self):
        self.tipoDocumento = None
        self.documento = None
        self.nome = None
        self.logradouro = None
        self.endereco = None
        self.bairro = None
        self.cidade = None
        self.uf = None
        self.cep = None
        self.email = None
        self.informacoes = ""

    @property
    def documentoTexto(self):
        if self.tipoDocumento == 1:
            return '%011d' % self.documento
        elif self.tipoDocumento == 2:
            return '%014d' % self.documento
        else:
            return str(self.documento)


class Boleto(object):

    def __init__(self):
        self.carteira = ""
        self.nossoNumero = ""
        self.dataVencimento = None
        self.dataDocumento = None
        self.dataProcessamento = None
        self.valorBoleto = 0.0
        self.quantidadeMoeda = 1
        self.valorMoeda = ""
        self.instrucoes = []

        #self.especieCodigo = 0
        #self.especieSigla = ""

        self.especieDocumento = ""
        self.aceite = "N"
        self.numeroDocumento = ""
        self.especie = "R$"
        self.moeda = 9

        #self.usoBanco

        self.cedente = None
        self.categoria = 0

        self.agencia = None
        self.agenciaDigito = None
        self.conta = None
        self.contaDigito = None

        self.banco = 33

        self.valorDesconto = None
        self.tipoDesconto1 = None
        self.valorDesconto1 = None
        self.tipoDesconto2 = None
        self.valorDesconto2 = None
        self.sacado = None

        self.jurosMora = 0.0
        self.iof = 0.0
        self.abatimento = 0.0
        self.valorMulta = 0.0
        self.outrosAcrescimos = 0.0
        self.outrosDescontos = 0.0
        self.dataJurosMora = None
        self.dataMulta = None
        self.dataOutrosAcrescimos = None
        self.dataOutrosDescontos = None

        self.retJurosMoltaEncargos = None
        self.retValorDescontoConcedido = None
        self.retValorAbatimentoConcedido = None
        self.retValorPagoPeloSacado = None
        self.retValorLiquidoASerCreditado = None
        self.retValorOutrasDespesas = None
        self.retValorOutrosCreditos = None
        self.retDataOcorrencia = None
        self.retDataOcorrenciaS = None
        self.retDataCredito = None
        self.retCodigoOcorrenciaSacado = None
        self.retDescricaoOcorrenciaSacado = None
        self.retValorOcorrenciaSacado = None


    def carrega_segmento(self, specs, tipo, valores):
        if   tipo == "P":

            carteiras = specs['carteiras']
            tipo_cobranca = str(valores['tipo_cobranca'])

            self.carteira = carteiras.get(tipo_cobranca, "0")
            self.nossoNumero = valores['nosso_numero']
            self.dataVencimento = valores['data_vencimento']
            self.dataDocumento = valores['data_emissao']
            self.valorBoleto = valores['valor_nominal']

            cedente = self.cedente

            cedente.agencia = valores['agencia_benef']
            cedente.agenciaDigito = valores.get('agencia_benef_dig')
            cedente.conta = valores['numero_conta']
            cedente.contaDigito = valores.get('digito_conta')
            cedente.convenio = 0
            cedente.convenioDigito = -1

            self.especieDocumento = valores.get('tipo_documento') # or ""?
            self.numeroDocumento = valores['seu_numero']
            #self.moeda = valores['cod_moeda'] #TODO: checar se tem de/para
            #self.categoria = 0
            self.banco = valores['codigo_banco']

            self.agencia = valores['agencia_benef']
            self.agenciaDigito = valores.get('agencia_benef_dig')
            self.conta = valores['numero_conta']
            self.contaDigito = valores.get('digito_conta')

            self.valorDesconto = valores['desconto'] #TODO: distinguir entre percentagem e valor

            self.jurosMora = valores['valor_mora_dia'] #TODO: distinguir entre percentagem e valor
            self.iof = valores.get('valor_iof', 0)
            self.abatimento = valores['valor_abatimento']

            #self.outrosAcrescimos = 0 #? #TODO: verificar se soma outros campos ou nao
            #self.outrosDescontos = 0 #? #TODO: verificar se soma outros campos ou nao
            self.dataJurosMora = valores['data_juros']

            #self.dataOutrosDescontos = None
            #self.dataOutrosAcrescimos = None

            self.aceite = valores['aceite'] #?

        elif tipo == "Q":
            sacado = Sacado()

            sacado.nome = valores['nome']

            sacado.tipoDocumento = valores['tipo_inscricao']
            sacado.documento = valores['numero_inscricao']

            sacado.logradouro = valores['endereco']
            sacado.endereco = valores['endereco']
            sacado.bairro = valores['bairro']
            sacado.cidade = valores['cidade']
            sacado.uf = valores['uf']
            sacado.cep = ('%05d' % valores['cep']) + ('%03d' % valores['cep_sufixo'])

            self.sacado = sacado

        elif tipo == "R":
            self.valorMulta = valores['multa']
            self.dataMulta = valores['data_multa']
            pass

        elif tipo == "S":
            pass

        elif tipo == "T":
            #carteiras = specs['carteiras']
            #tipo_cobranca = str(valores['tipo_cobranca'])

            #self.carteira = carteiras.get(tipo_cobranca, "0")
            self.nossoNumero = valores['nosso_numero']
            self.dataVencimento = valores['data_vencimento']
            self.valorBoleto = valores['valor_nominal']

            cedente = self.cedente

            cedente.agencia = valores['agencia_benef']
            cedente.agenciaDigito = valores.get('agencia_benef_dig')
            cedente.conta = valores['numero_conta']
            cedente.contaDigito = valores.get('digito_conta')
            cedente.convenio = 0
            cedente.convenioDigito = -1

            self.banco = valores['codigo_banco']

            self.agencia = valores['agencia_benef']
            self.agenciaDigito = valores.get('agencia_benef_dig')
            self.conta = valores['numero_conta']
            self.contaDigito = valores.get('digito_conta')

        elif tipo == "U":
            self.retJurosMoltaEncargos = valores['valor_encargos']
            self.retValorDescontoConcedido = valores['valor_desconto']
            self.retValorAbatimentoConcedido = valores['valor_abatimento']
            self.retValorPagoPeloSacado = valores['valor_pago']
            self.retValorLiquidoASerCreditado = valores['valor_liquido']
            self.retValorOutrasDespesas = valores['valor_despesas']
            self.retValorOutrosCreditos = valores['valor_creditos']
            self.retDataOcorrencia = valores['data_ocorrencia']
            self.retDataOcorrenciaS = valores['data_ocorrencia_s']
            self.retDataCredito = valores['data_efetivacao']
            self.retCodigoOcorrenciaSacado = valores['cod_movimento']
            self.retDescricaoOcorrenciaSacado = valores['comp_ocorrencia']
            self.retValorOcorrenciaSacado = valores['valor_ocorrencia']

        elif tipo == "Y":
            pass

    @property
    def valorCobrado(self):
        return valorBoleto #TODO

    @property
    def nossoNumeroTexto(self):
        return "%013d" % self.nossoNumero
