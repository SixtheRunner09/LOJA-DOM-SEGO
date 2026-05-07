from datetime import datetime

def cad_produt(estoque):
    nome = input ('digite o produto:')
    quantidade = int(input('digite a quantidade deste novo produto no estoque:'))

    estoque.append({'nome':nome,
                    'quantidade': quantidade})
    
    print(f"produto '{nome}' cadastrado com sucesso!\n")

def verif_estq(estoque):
    print('\n  VERIFICAÇÃO DO ESTOQUE')
    for produto in estoque:
        if produto ['quantidade'] == 0:
            print(f'{produto['nome']}: Fazer pedido URGENTE!')
        elif produto['quantidade']<10:
            print(f'{produto['nome']}: Estoque acabando({produto['quantidade']})')
            print()

def reg_vend(estoque,vendas):
    nome = input('digite o produto vendido:')
    valor = float(input('digite o valor do produto que foi vendido:'))

    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            if produto['quantidade']>0:
                produto ['quantidade'] -=1
                vendas.append({'produto': nome,
                               'valor': valor})
                print('Venda localizada e registrada!')
                return
            else:
                print('produto sem estoque!\n')
                return
    print('produto não econtrado!\n')

def Calc_vend(vendas):
    total = sum(v['valor'] for v in vendas)
    return total

def anls_vendas(vendas):
    if not vendas:
        return None, None
    
    Ms_caro = max(vendas, key=lambda x: x['valor'])
    Ms_barato = min(vendas, key=lambda x: x['valor'])
    return Ms_caro, Ms_barato

def relatório_final(estoque,vendas):
    print(' RELATÓRIO FINAL ')
    print('\nETOQUE DO DOM SEGO')
    for produto in estoque:
        print(f'{produto['nome']} - {produto['quantidade']} unidades')
    faturamento = Calc_vend(vendas)
    print(f'\nFaturamento total: R${faturamento:.2f}')

    acima_100 = [v for v in vendas if v['valor']>100]
    print(f'qttd de vendas acima de 100R$: {len(acima_100)}')

    Ms_caro, Ms_barato = anls_vendas(vendas)
    if Ms_caro:
        print(f'Produto mais caro vendido: {Ms_caro['produto']}(R${Ms_caro['valor']})')
        print(f'Produto mais barato vendido: {Ms_barato['produto']}(R${Ms_barato['valor']})')
    print('Data do Relatório:',datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
print('============================\n')

def Main():
    estoque = []
    vendas = []

    while True:
        print('1 - Casdastrar produto')
        print('2 - registrar venda')
        print('3 - verificar estoque')
        print('4 - relatório final')
        print('0 - Sair')

        opcao = input('\nOlá bem-vindo ao estoque do dom sego escolha uma das opções acima:')

        if opcao == '1':
            cad_produt(estoque)
        elif opcao == '2':
            reg_vend(estoque,vendas)
        elif opcao == '3':
            verif_estq(estoque)
        elif opcao == '4':
            relatório_final(estoque,vendas)
        elif opcao == '0':
            break
        else:
            print('opção não catalógada. Tente novamente\n')

Main()