

def cadastro_posto(nome_posto,salario,combustiveis,frentistas):
    posto_dados={
        'nome':nome_posto,
        'combustiveis':combustiveis,
        'frentistas':frentistas,
        'faturamento':0,
        'bloqueado':False,
        'salario':salario
    }
    return posto_dados

def consumo(valor,combustivel,posto_dados):
    combustivel=posto_dados['combustiveis'][combustivel] #retornando todo o dicionário em combustiveis
    consumido=valor/combustivel['preco']
    combustivel['volume']-=consumido
    if combustivel['volume']<0:
        return False
    else:
        return float(f'{combustivel["volume"]:.3f}')

def bonus(frentista, posto_dados):
    if posto_dados['frentistas'][frentista]['vendas']==10:
        posto_dados['frentistas'][frentista]['vendas']=0
        posto_dados['frentistas'][frentista]['bonus']+=50

def abastecer(frentista,combustivel,valor,posto_dados):
    posto_dados['frentistas'][frentista]['vendas']+=1
    bonus(frentista,posto_dados)
    consumo = consumo(valor, combustivel,posto_dados)
    if consumo == False:
        return f'Impossível de abastecer: não há {combustivel} suficiente'
    posto_dados['combustiveis'][combustivel]['volume'] = consumo(valor, combustivel,posto_dados)
    if not posto_dados['combustiveis'][combustivel]['volume'] == False:
        posto_dados['faturamento']+=valor
    else:
        return 'Não foi possível abastecer'

