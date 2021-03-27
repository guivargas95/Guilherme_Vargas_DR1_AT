'''Questão 3
Considere o argumento abaixo:
Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, no máximo, 30% da sua renda mensal à
moradia,20% à educação e 15% ao transporte. Esses valores não devem ser totalmente desprezados, mas não podem funcionar
como um norte para o orçamento doméstico de todas as famílias.
Fonte: BTG Pactual Digital
Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais
com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores
percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo.
Se o gasto estiver dentro do percentual recomendado, informe ainda que
Seus gastos estão dentro da margem recomendada.
Caso contrário, informe:
Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de
gastos com esse tipo de custo.'''

renda_total = float(input('Renda mensal total: R$ '))
moradia = float(input('Gastos totais com moradia: R$ '))
educacao = float(input('Gastos totais com educação: R$ '))
transporte = float(input('Gastos totais com transporte: R$ '))

def saude_financeira(rendatotal, moradia, educacao, transporte):
    resultado_moradia = float((moradia * 100) / rendatotal)
    resultado_educacao = float((educacao * 100) / rendatotal)
    resultado_transporte = float((transporte * 100) / rendatotal)
    moradia_ideal = float(rendatotal * 0.3)
    educacao_ideal = float(rendatotal * 0.2)
    transporte_ideal = float(rendatotal * 0.15)
    print('Diagnóstico: ')
    if resultado_moradia > 30:
        print(f'Seus gastos totais com moradia comprometem {resultado_moradia:.2f}% da sua renda total.'
              f'O máximo recomendado é 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia '
              f'deveria ser de R$ {moradia_ideal:.2f}')
    else:
        print(f'Seus gastos totais com moradia comprometem {resultado_moradia:.2f}% e estão, portanto, dentro dos padrões '
              f'ideais de no máximo 30%')
    if resultado_educacao > 20:
        print(f'Seus gastos totais com educação comprometem {resultado_educacao:.2f}% da sua renda total.'
              f'O máximo recomendado é 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação '
              f'deveria ser de R$ {educacao_ideal:.2f}')
    else:
        print(f'Seus gastos totais com educação comprometem {resultado_educacao:.2f}% e estão, portanto, dentro dos padrões '
              f'ideais de no máximo 20%')
    if resultado_transporte > 15:
        print(f'Seus gastos totais com transporte comprometem {resultado_transporte:.2f}% da sua renda total.'
              f'O máximo recomendado é 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte '
              f'deveria ser de R$ {transporte_ideal:.2f}')
    else:
        print(f'Seus gastos totais com transporte comprometem {resultado_transporte:.2f}% e estão, portanto, dentro dos padrões '
              f'ideais de no máximo 15%')

saude_financeira(renda_total,moradia,educacao,transporte)
