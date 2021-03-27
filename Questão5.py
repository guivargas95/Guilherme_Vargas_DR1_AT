def solicitar_pib(nome_pais,ano):
    import csv
    resultado = 0
    if ano <= 2012 or ano >= 2021:
        print('Ano não disponível. Informe o ano entre 2013 e 2020.\n')
    else:
        with open('PIB.csv', encoding='utf-8') as pib:
            tabela = csv.reader(pib, delimiter=',')
            for c,linha in enumerate(tabela): # Looping para verificar o índice do ano solicitado.
               if c == 0:
                   for c,valor in enumerate(linha):
                        if c > 0: # Se fizer a comparação com o índice 0 da erro. Comparação entre int e str.
                            if int(valor) == ano:
                                indice_ano = c
               if nome_pais == linha[0]:
                    resultado = list(linha)
            if resultado == 0:
                print('País não disponível\n')
            else:
                print(f'PIB {resultado[0]} em {ano}: US${resultado[indice_ano]} trilhões\n')

def variacao_pib():
    import csv
    with open('PIB.csv', encoding='utf-8') as pib:
        tabela = csv.reader(pib, delimiter=',')
        for c,linha in enumerate(tabela):
                if c > 0:
                    resultado = linha
                    variacao = (float(resultado[8]) / float(resultado[1]) - 1) * 100
                    print(f'{linha[0]:<30}',end=' ')
                    print(f'Variação de {variacao:.2f}%')
        print('\n')

def grafico_pib(pais):
    import matplotlib.pyplot as plt
    import csv
    with open('PIB.csv', encoding='utf-8') as pib:
        tabela = csv.reader(pib, delimiter=',')
        for c,linha in enumerate(tabela):
            if c == 0:
                ano = list(linha)
            if pais == linha[0]:
                resultado = list(linha)
        nome_pais = str(resultado[0])
        ano.pop(0)
        resultado.pop(0)
    plt.plot(ano, resultado, 'r--', label='Curva 1')
    plt.xlabel('Ano')
    plt.ylabel('Valor do PIB')
    plt.title(f'PIB de {nome_pais}')
    plt.show()

print('Olá, seja muito bem vindo a questão 5 do AT.')
while True:
    print('Informe a função que deseja verificar:\n\n1- Solicitar PIB de um país em um determinado ano'
          '\n2- Lista da variação de PIB\n3- Gráfico da evolução do PIB\n4- Sair')
    op = input('\nSua opção: ')
    if op in '1':
        pais = input('Informe o nome do país: ').strip()
        ano = int(input('Informe o ano entre 2013 e 2020: '))
        solicitar_pib(pais,ano)
    elif op in '2':
        variacao_pib()
    elif op in '3':
        pais = input('Informe o nome do país: ').strip()
        grafico_pib(pais)
    elif op in '4':
        print('Obrigado por utilizar o programa.')
        break
    else:
        print('Função inválida.\n')

