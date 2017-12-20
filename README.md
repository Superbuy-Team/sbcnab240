# sbcnab240

Biblioteca em Python 2.x para leitura de arquivos CNAB 240.

## Exemplo de uso:

```python
from sbcnab240.Processamento import carrega_linhas

f = open(arquivo_remessa, 'r')
linhas = f.readlines()
f.close()

resultado = carrega_linhas('remessa', 'santander', linhas)

if resultado and resultado.lotes:
    for l in resultado.lotes:
        for b in l.boletos:
            print b
```

## Bancos suportados

No momento, há suporte apenas para o banco Santander. Acrescentar novos bancos é simples; basta criar novos arquivos json no diretório sbcnab240/bancos/ . Pode-se usar o arquivo do banco Santander como exemplo/modelo; basta manter os identificadores de campos e tudo deve funcionar corretamente.

A biblioteca é simples e atualmente focada em extrair informações chave dos arquivos de remessa/retorno para atualização de nossa base de dados, e não foi planejada para geração de arquivos ou coisa do tipo. Em teoria, é possível adaptar o código sem *muito* esforço para se prestar também a essas funções.

## Licença

Estamos liberando a biblioteca para uso e adaptação livre por outros, por isso a licença é MIT. Não hesite em enviar pull requests se quiser colaborar!

## Sobre

Essa biblioteca está sendo disponibilizada pelo [SuperBuy](https://www.superbuy.com.br/), uma plataforma web de negócios B2B que usa Python extensivamente.
