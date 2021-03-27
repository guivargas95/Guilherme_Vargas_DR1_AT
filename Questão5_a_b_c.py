''' Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB (Arquivo .csv) de um país para um determinado ano. 
O programa solicita ao usuário o nome do país e o ano desejado.
Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 
País não disponível.
ou
Ano não disponível.
a depender do tipo de dado não encontrado. 
Exemplo de saída do programa:
Informe um país: Brasil
Informe um ano entre 2013 e 2020: 2020
PIB Brasil em 2020: US$2.35 trilhões.
Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.
Exemplo de saída do programa:
EUA                  Variação de 34.13% entre 2013 e 2020.
China                Variação de 70.72% entre 2013 e 2020.
Japão                Variação de 0.2% entre 2013 e 2020.
Alemanha             Variação de 9.92% entre 2013 e 2020.
Reino Unido          Variação de 39.18% entre 2013 e 2020.
França               Variação de 7.5% entre 2013 e 2020.
Brasil               Variação de -1.67% entre 2013 e 2020.
Itália               Variação de 1.88% entre 2013 e 2020.
Índia                Variação de 94.65% entre 2013 e 2020.
Rússia               Variação de 0.48% entre 2013 e 2020.
Canadá               Variação de 11.48% entre 2013 e 2020.
Coreia do Sul        Variação de 54.62% entre 2013 e 2020.
Espanha              Variação de 6.47% entre 2013 e 2020.
México               Variação de 30.95% entre 2013 e 2020.
Indonésia            Variação de -85.76% entre 2013 e 2020.
Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
'''

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

