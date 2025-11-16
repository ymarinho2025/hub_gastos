# controle_gastos_v2.py
# Controle de Gastos V2 — pronto para import (função main)

import matplotlib.pyplot as plt
import sys
import time

def main():
    print("BEM VINDO AO CONTROLE DE GASTOS V2\ncoloque apenas numeros e caso coloque os centavos colocar o '.' e não a ','")

    # Entrada robusta do salário
    while True:
        try:
            salario = float(input("Qual seu salario mensal?\nR$"))
            break
        except ValueError:
            print("Valor inválido. Use apenas números (ponto para decimais).\n")

    gastos = {}
    finalizar = False  # Flag para encerrar o menu de coleta

    # Primeiro Loop
    while True:
        print("====== CONTROLE DE GASTOS V2 =======\nvamos calcular seus gastos mensais\ne te ajudar a organizar seu dinheiro!\n")
        # Segundo Loop
        while True:
            # Usar Try para o usuario não colocar pontuação errada
            try:
                # Usuario Coloca valor dos gastos
                gastos_mensais = float(input("INSIRA o VALOR dos seus GASTOS ou\n0) ir para proxima etapa\n"))
                print()
            except ValueError:
                print("coloque apenas numeros e caso coloque os centavos\ncolocar o '.' e não a ','\n")
                continue

            # 0 para pular para a proxima etapa
            if gastos_mensais == 0:
                for nome, custo in gastos.items():  # Nomear itens em gastos e printar eles
                    print(f"{nome}: {custo}")       # Após a execução do final na linha 35: ( gastos[nome_gastos_mensais] = gastos_mensais )
                break

            # Usuario Coloca nome dos gastos
            nome_gastos_mensais = input(f"Coloque o nome referente a este gasto de {gastos_mensais}:\n").strip().lower()
            print()
            # Checar se Usuario não pulou essa parte apenas
            if not nome_gastos_mensais:
                print("Nome em branco, Vamos refazer do zero!\n")
                continue
            # Checar se Usuario já colocou esse gasto ou queira atualizar valor
            elif nome_gastos_mensais in gastos:
                try:
                    confirmar = int(input(f"Esse nome já existe em gastos\n1) ATUALIZAR valor da {nome_gastos_mensais}\n2) VOLTAR\n"))
                    print()
                except ValueError:
                    print("aceitamos apenas 1 e 2 de resposta\n")
                    continue

                if confirmar == 2:
                    continue
                if confirmar != 1:
                    print("aceitamos apenas 1 e 2 de resposta\n")
                    continue

            # Adicionar itens a lista 'gastos'
            gastos[nome_gastos_mensais] = gastos_mensais

        # Terceiro Loop
        # É execultada após a linha 25: ( if gastos_mensais == 0: )
        # Ele quebra o Segundo Loop e entra no Terceiro Loop por ambos estarem na mesma linha
        while True:
            # Ele pode voltar pra adicionar, Entrar em novo menu para remover ou Continuar outra linha de raciocinio
            try:
                adicionar_gastos = int(input("\n1) ADICIONAR algum GASTO\n2) REMOVER algum GASTO\n3) CONTINUAR\n"))
                print()
            except ValueError:
                print("aceitamos apenas respostas de 1 a 3\n")
                continue

            # Quebra o codigo e volta para o Segundo Loop
            if adicionar_gastos == 1:
                break

            # Verifica se possui algum gasto
            elif adicionar_gastos == 2:
                if not gastos:
                    print("Você não adicionou gasto nenhum!")
                    continue
                # Quarto Loop
                while True:
                    remover_gastos = input("Coloque o nome do gasto que queira remover ou\n1) Ver GASTOS\n2) VOLTAR\n").strip().lower()
                    # Se 2 ele volta
                    if remover_gastos == '2':
                        break
                    # Se 1 ele verifica gastos
                    elif remover_gastos == '1':
                        print(f"Seus gastos são:\n{gastos}\n")
                        continue
                    # Verifica se gastos existem
                    elif remover_gastos not in gastos:
                        print(f"Esse gasto não existe, apenas possuimos os seguintes gastos:\n{gastos}\n")
                        continue
                    del gastos[remover_gastos]
                    print(gastos)

            # Continuar raciocinio do codigo
            elif adicionar_gastos == 3:
                if not gastos:
                    print("Você não cadastrou nenhum gasto.")
                    return  # evita encerrar toda a aplicação quando importado
                # Muda a flag e sai de todos os Loops
                finalizar = True
                break
            else:
                print("aceitamos apenas respostas de 1 a 3\n")

        # Sai do primeiro Loop tambem
        if finalizar:
            break

    # Após listar gastos e seu salario vamos ver quanto sobrou, ver no que ele é mais gasto, e criar um grafico
    print("=== MENU CONTROLE DE GASTOS ===")
    # Somar
    soma_custos = sum(gastos.values()) if gastos else 0.0
    # Subtrair
    subtrair = salario - soma_custos
    print(f"Seu salario está: {subtrair:.2f}")

    # Mensagem dependendo do valor que sobrou
    if subtrair < 0:
        print("\nComo pode ver seu salario está negativo porem isso não é culpa sua\n"
              "De acordo com dados recentes, aproximadamente 70,29 milhões\n"
              "de brasileiros adultos estavam com o “nome sujo” ou negativados em meados de 2025\n")
    elif subtrair == 0:
        print("\nComo pode ver, seu salário chegou exatamente ao fim do mês sem sobras.\n"
              "isso mostra que você está equilibrando bem seus gastos, mas é importante tentar guardar algo.\n"
              "em 2025, cerca de 70,29 milhões de brasileiros estavam negativados — planejar é essencial para não entrar nessa estatística.\n")
    elif subtrair > 0:
        print("Parabéns! Você conseguiu encerrar o mês com saldo positivo.\n"
              "manter esse controle é o primeiro passo para criar uma reserva financeira e conquistar estabilidade.\n")

    print("Vamos criar um grafico para analizar os maiores e menores gastos!")
    # Dar tempo antes de carregar o grafico
    time.sleep(2)

    # Cria o grafico e mostra ele
    if gastos:
        title = 'Controle de Gastos'
        xname = 'Gastos'
        yname = 'Valores'

        nomes = list(gastos.keys())
        custos = list(gastos.values())

        plt.figure(figsize=(8, 4.5))
        plt.bar(nomes, custos, color='yellow')
        plt.xlabel(xname)
        plt.ylabel(yname)
        plt.title(title)
        plt.xticks(rotation=0, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Sem dados de gastos para plotar o gráfico.")

    # Listagem final dos gastos
    if gastos:
        print('\n'.join([f"{nome}: R${valor:.2f}" for nome, valor in gastos.items()]))

    # Análise do maior gasto
    if gastos:
        # Pega o MAIOR valor entre todos os gastos
        maior_valor = max(gastos.values())

        # Cria uma lista com o(s) nome(s) do(s) gasto(s) que possuem esse maior valor
        maiores_itens = [nome for nome, val in gastos.items() if val == maior_valor]  # 'val' pra valor

        # Calcula o percentual que o maior gasto representa em relação ao salário
        perc_salario = (maior_valor / salario) * 100 if salario else 0  # evita ZeroDivision

        # Verifica se há apenas um gasto com o maior valor
        if len(maiores_itens) == 1:
            print(f"Seu maior gasto foi com '{maiores_itens[0]}' (R${maior_valor:.2f}, {perc_salario:.1f}% do salário).")
            print("Será que você está gastando isso certo?")
        else:
            itens = ", ".join(f"'{n}'" for n in maiores_itens)
            print(f"Seus maiores gastos foram com {itens} (R${maior_valor:.2f} cada, {perc_salario:.1f}% do salário).")
            print("Será que você está gastando isso certo?")
    else:
        print("Sem gastos cadastrados para analisar o maior gasto.")

if __name__ == "__main__":
    main()
