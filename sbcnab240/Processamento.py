import os
import json
import datetime
import decimal

from .Remessa import Remessa
from .Retorno import Retorno
#from Cobranca import Cobranca
from .Lote import Lote
from .Boleto import Boleto


cur_dir = os.path.abspath(os.path.dirname(__file__))
bancos_dir = os.path.join(cur_dir, 'bancos')


def load_arquivo_banco(banco):
    filename = os.path.join(bancos_dir, os.path.basename(banco + '.json'))
    try:
        f = open(filename)
        data = f.read()
        f.close()
    except IOError:
        return None

    return data


map_tipo_registro = {
    0: "HeaderArquivo",
    1: "HeaderLote",
    3: "Segmento",
    5: "TrailerLote",
    9: "TrailerArquivo"
}

def load_banco(banco):
    dataraw = load_arquivo_banco(banco)
    if dataraw:
        datajs = json.loads(dataraw)
        return datajs

def converte_valor(tipo, vstr):
    if   tipo == 'A':
        return vstr.strip()

    elif tipo == 'N':
        return int(vstr)

    elif tipo == 'D':
        if vstr == '        ' or vstr == '00000000':
            return None
        else:
            dia = int(vstr[0:2])
            mes = int(vstr[2:4])
            ano = int(vstr[4:])
            dd = datetime.date(ano, mes, dia)
            return dd

    elif tipo[0] == 'F':
        precisao = int(tipo[1:])
        return decimal.Decimal(vstr) / 10**precisao

    else:
        return vstr


def carrega_linhas(tipo, banco, linhas):
    specs = load_banco(banco)

    if tipo == "remessa":
        base_t = "Remessa"
        resultado = Remessa()
    elif tipo == "retorno":
        base_t = "Retorno"
        resultado = Retorno()
    else:
        return None

    campos = []
    for linha in linhas:
        tipo = int(linha[7])
        base = map_tipo_registro[tipo]
        if tipo == 3:
            segmento = linha[13]
            base += segmento
        else:
            segmento = None
            base += base_t

        #print base #DEBUG

        spec = specs[base]
        pos = 0
        _campos = {}
        for campo in spec['campos']:
            nome = campo[0]
            tipo = campo[1]
            tamanho = campo[2]
            if nome:
                valor = linha[pos:pos+tamanho]
                #print nome, tipo, valor,
                #print converte_valor(tipo, valor)
                _campos[nome] = converte_valor(tipo, valor)
            pos += tamanho

        campos.append((base, _campos))

    #for (k,v) in campos: #DEBUG
    #    print k, v #DEBUG

    resultado.carrega_campos(specs, campos)

    return resultado
