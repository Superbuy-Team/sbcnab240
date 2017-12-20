from sbcnab240.Processamento import load_banco, carrega_linhas


def valida_arquivo(banco):
    dados = load_banco('santander')

    for k,v in dados.items():
        print
        print k
        pos = 1
        for campo in v['campos']:
            newpos = pos + campo[2]
            print pos, newpos-1, campo[0], campo[1]
            pos = newpos


def testa_carrega():
    f = open('tests/arquivos/Dorze_Remessa.txt', 'rt')
    lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    #valida_arquivo('santander')
    linhas = testa_carrega()
    r = carrega_linhas('remessa', 'santander', linhas)
    print r
