import posto as pt
from dados import *

combustiveis=ler_comb('comb.csv')
frentistas=ler_frentista('frentista.csv')

print('Bem vindo ao software de gestão do seu posto')

nomePosto=input('Insira o nome do seu posto: ')
salariofixo=float(input('Insira o salário fixo de cada frentista: '))

postoDados = pt.cadastro_posto(nomePosto,salariofixo,combustiveis,frentistas)
print(postoDados)

pt.abastecer('Renan', 'gasolina', 300, postoDados)

def operacao(op,postoDados):
    if op == 1:
        coluna=pd.DataFrame(postoDados['frentistas'])
        print(list(coluna.columns))
       
        frentista = input('Insira o nome do frentista que abastecerá: ')
        combustivel = input('Digite o combustivel que será abastecido: ')
        valor = float(input('Digite o valor a ser abastecida: '))
        pt.abastecer(frentista, combustivel, valor, postoDados)
        return 'Abastecimento realizado com sucesso'
    elif op == 2:
        if postoDados['bloqueado']:
            return 'O posto já está bloqueado'
        else:
            postoDados['bloqueado']=True
            return 'O posto foi bloqueado'
    elif op == 3:
        if not postoDados['bloqueado']:
            return 'O posto já está desbloqueado'
        else:
            postoDados['bloqueado']=False
            return 'O posto foi desbloqueado'
    elif op == 4:
        relatorio(relatorio1, postoDados)
    

while True:
    ler_txt('dialogo1.txt')
    try:
        op=int(input('Digite o número da operação que deseja realizar: '))
    except:
        continue
    if op ==5:
        break
    operacao(op,postoDados)
print('o posto foi fechado')