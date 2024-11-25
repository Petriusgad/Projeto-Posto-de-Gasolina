
#combustiveis={
#    'gasolina':{'preco':5.7,
#
#                'volume':500
#
#    },
#    'etanol':{
#        'preco':5.7,
#        'volume':340
#    }
#}

import pandas as pd

def ler_txt(arquivo):

    with open(arquivo,'r',encoding='utf-8') as file:
        print(file.read())

def ler_comb(arquivo):
    combustiveis={}
    dados_combustiveis=pd.read_csv(arquivo,sep=';')
    dados_combustiveis=dados_combustiveis.to_dict('records')
    for dados in dados_combustiveis:
        combustiveis[dados['nome']]={
            'preco':dados['preco'],
            'volume':dados['volume']  }
    return combustiveis

def ler_frentista(arq):
    frentistas={}
    dados_frentistas=pd.read_csv(arq, sep=';')
    dados_frentistas=dados_frentistas.to_dict('records')
    for dados in dados_frentistas:
        frentistas[dados['nome']]={
            'vendas':0,
            'bonus':0
        }
    return frentistas

def relatorio(arq, posto_dados):
    arq+='.txt'
    with open(arq,'w+',encoding='utf-8') as file:
        file.write(f'Relatório do posto{posto_dados["nome"]}')
if __name__ == '__main__':
    print(ler_frentista('frentista.csv'))
    ler_comb('comb.csv')