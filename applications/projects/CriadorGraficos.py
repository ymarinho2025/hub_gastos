import matplotlib.pyplot as plt
import string


def main():
    valor_item = {}

    while True:
        print("============== CRIAR GRAFICO ==============\n")

        try:
            choices = int(input(
                "1) Adicionar dados comparativos\n"
                "2) Remover dados comparativos\n"
                "3) Comparar estatisticas\n"
                "4) Configurar Grafico e Finalizar\n"
            ))
        except ValueError:
            print("Digite um número válido!")
            continue
        print()

        if choices == 1:
            while True:
                nome_item = input(
                    "ESCREVA o NOME do ITEM comparativo ou\n"
                    "0) para voltar no menu anterior\n"
                ).strip().lower()

                if nome_item == "0":
                    break
                elif nome_item.isdigit() or all(c in string.punctuation for c in nome_item):
                    print("Nome inválido! Use apenas letras.\n")
                    continue

                if nome_item in valor_item:
                    print(f"O nome '{nome_item}' já está cadastrada com valor {valor_item[nome_item]}.")
                    atualizar = input("Deseja atualizar o valor? (s/n): ").strip().lower()
                    if atualizar != 's':
                        continue

                try:
                    nota = float(input(f"ADICIONE o VALOR de {nome_item}:\n"))
                except ValueError:
                    print("Digite um número válido!")
                    continue
                print()

                valor_item[nome_item] = nota
                print(f"Adicionado: {nome_item} -> {nota}")
                print(f"\nITEMS e VALORES:\n")
                for item, valor in valor_item.items():
                    print(f"  {item}: {valor}")
                print()

        elif choices == 2:
            while True:
                if not valor_item:
                    print("Nenhum dado cadastrado!\n")
                    break

                print("\nITEMS CADASTRADOS:")
                for item, valor in valor_item.items():
                    print(f"  {item}: {valor}")
                print()

                remover_item = input(
                    "DIGITE o NOME da pessoa para remover ou\n"
                    "0) para voltar no menu anterior\n"
                ).strip().lower()

                if remover_item == "0":
                    break
                elif remover_item in valor_item:
                    nota_removida = valor_item.pop(remover_item)
                    print(f"Removido: {remover_item} (nota: {nota_removida})\n")
                else:
                    print("ITEM não encontrada na lista!\n")

        elif choices == 3:
            if not valor_item:
                print("Informação incompleta! Nenhum dado cadastrado.\n")
            else:
                print("\n========== ESTATÍSTICAS ==========")
                print(f"Total de itens: {len(valor_item)}")

                for pessoa, nota in valor_item.items():
                    print(f"  {pessoa}: {nota}")

                notas = list(valor_item.values())
                print(f"\nMédia dos valores: {sum(notas) / len(notas):.2f}")
                print(f"Maior valor: {max(notas):.2f}")
                print(f"Menor valor: {min(notas):.2f}")
                print("==================================\n")

        elif choices == 4:
            if not valor_item:
                print("Não há dados para criar o gráfico!\n")
                continue

            title = input("Escreva o TÍTULO do GRÁFICO:\n").strip()
            yname = input("Adicione a DESCRIÇÃO dos NÚMEROS (ex: Notas):\n").strip()
            xname = input("Adicione a DESCRIÇÃO dos DADOS (ex: Pessoas):\n").strip()

            pessoas = list(valor_item.keys())
            notas = list(valor_item.values())

            plt.figure(figsize=(8, 4.5))
            plt.bar(pessoas, notas, color='green')
            plt.xlabel(xname)
            plt.ylabel(yname)
            plt.title(title)
            plt.xticks(rotation=0, ha='right')
            plt.tight_layout()
            plt.show()
            break

        else:
            print("Opção inválida! Escolha entre 1 e 4.\n")

    print("CODIGO FINALIZADO...")


if __name__ == "__main__":
    main()
