import sys
import HUB_Login
import controle_gastos
import Calendario

def menu_hub():
    while True:
        print("\n=== ROUTINE HUB ===")
        print("1) Controle de Gastos")
        print("2) Calendário")
        print("0) Sair")
        try:
            op = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 0:
            print("Saindo do Routine HUB...")
            break
        elif op == 1:
            controle_gastos.main()
        elif op == 2:
            Calendario.main()   # abre o menu do calendário
        else:
            print("Opção inválida.")

def main():
    ok = HUB_Login.main()   # precisa retornar True no sucesso do login
    if ok:
        print("Login concluído. Entrando no HUB...")
        menu_hub()
    else:
        print("Login não concluído.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)
    finally:
        try:
            HUB_Login.shutdown()  # fecha a conexão SQLite do módulo de login
        except Exception:
            pass
