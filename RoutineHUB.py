import sys
import HUB_Login          # módulo de login (precisa retornar True no sucesso)
import controle_gastos    # seu módulo com def main()

def main():
    # 1) Faz login primeiro
    ok = HUB_Login.main()
    if not ok:
        print("Login não concluído.")
        return

    # 2) Menu simples pós-login
    while True:
        try:
            op = int(input("======== ROUTINE HUB ========\n1) Gestor de gastos\n0) Sair\nEscolha: "))
            print()
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 1:
            # chama a função principal do módulo de gastos
            controle_gastos.main()
        elif op == 0:
            print("Saindo do Routine HUB...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)
    finally:
        # garante que o HUB_Login feche a conexão SQLite
        try:
            HUB_Login.shutdown()
        except Exception:
            pass
