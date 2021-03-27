'''Seja a seguinte citação:
Osjuros compostos são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma confiável
e sistemática acumulação de riqueza
A frase, curiosamente, é de Albert Einstein, não de algum banqueiro ou gestor de fundos de capitais.
Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês.
Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte,
R$12.113,69, e assim sucessivamente.
Ao final de 120 meses, você terá o montante final de R$187.303,05.

a. Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro
inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

b. Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o ]
número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.'''

montante_inicial = float(input('Informe o valor inicial: R$ '))
rendimento = float(input('Informe o rendimento por período (%): '))
aporte = float(input('Informe o aporte por período: R$ '))
quantidade_periodos = int(input('Informe o total de períodos: '))

def investimento(m,r,a,q):
    periodos = []
    valores = []
    r = r/100
    for c in range(1,q+1):
        m += (m*r)
        m += a
        print(f'Após {c} período(s), o montante será de R$ {m:.2f}')
        periodos.append(c)
        valores.append(m)
    return periodos,valores

def gerar_grafico(x,y):
    import matplotlib.pyplot as plt
    plt.plot(x, y, 'r--', label='Curva 1')
    plt.xlabel('Períodos')
    plt.ylabel('Valor')
    plt.title('Resultado do investimento')
    plt.show()

resultado_investimento = investimento(montante_inicial,rendimento,aporte,quantidade_periodos)
gerar_grafico(resultado_investimento[0],resultado_investimento[1])