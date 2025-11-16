import sqlite3

# =======================
# 1) CRIAR CONEXÃO
# =======================
def criar_conexao(nome_usuario):
    nome_limpo = nome_usuario.strip().lower().replace(" ", "_")
    nome_banco = f"{nome_limpo}_2025.db"
    print(f"[INFO] Banco criado/carregado: {nome_banco}")
    return sqlite3.connect(nome_banco)

# =======================
# 2) CRIAR TABELA
# =======================
def criar_tabela(conn):
    cursor = conn.cursor()

    comando1 = """
    CREATE TABLE IF NOT EXISTS calendario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mes INTEGER NOT NULL,
        dia TEXT NOT NULL,
        horario TEXT NOT NULL,
        evento TEXT NOT NULL
    );
    """

    cursor.execute(comando1)
    conn.commit()

# =======================
# 3) INSERIR EVENTO
# =======================
def inserir_evento(conn):
    cursor = conn.cursor()
    print("\n=== INSERIR EVENTO ===")

    # --- MÊS ---
    while True:
        mes = input("Digite o mês (1-12): ").strip()
        if mes.isdigit() and 1 <= int(mes) <= 12:
            mes = int(mes)
            break
        print("Mês inválido!")

    # --- DIA ---
    while True:
        dia = input("Digite o dia (01-31): ").strip()
        if dia.isdigit() and len(dia) == 2 and 1 <= int(dia) <= 31:
            break
        print("Dia inválido! (Use 2 dígitos)")

    # --- HORÁRIO ---
    while True:
        hora = input("Hora (00-23): ").strip()
        minuto = input("Minutos (00-59): ").strip()

        if hora.isdigit() and minuto.isdigit():
            h = int(hora)
            m = int(minuto)
            if 0 <= h <= 23 and 0 <= m <= 59:
                horario = f"{h:02d}:{m:02d}"
                break
        print("Horário inválido!")

    # --- EVENTO ---
    while True:
        evento = input("Descreva o evento: ").strip()
        if evento:
            break
        print("Evento não pode ser vazio.")

    # COMANDO 2 — INSERIR
    comando2 = """
    INSERT INTO calendario (mes, dia, horario, evento)
    VALUES (?, ?, ?, ?);
    """

    cursor.execute(comando2, (mes, dia, horario, evento))
    conn.commit()

    print("\n[OK] Evento inserido com sucesso!")

# =======================
# 4) LISTAR EVENTOS
# =======================
def listar_eventos(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT id, mes, dia, horario, evento FROM calendario ORDER BY mes, dia, horario;")
    dados = cursor.fetchall()

    if not dados:
        print("\nNenhum evento encontrado.")
        return

    print("\n=== EVENTOS ===")
    for linha in dados:
        print(f"[{linha[0]}] {linha[2]}/{linha[1]:02d} - {linha[3]} - {linha[4]}")
    print("=====================")

# =======================
# 5) ATUALIZAR EVENTO
# =======================
def atualizar_evento(conn):
    cursor = conn.cursor()
    listar_eventos(conn)

    try:
        eid = int(input("\nID do evento para atualizar: ").strip())
    except:
        print("ID inválido.")
        return

    cursor.execute("SELECT id FROM calendario WHERE id = ?;", (eid,))
    if cursor.fetchone() is None:
        print("Evento não encontrado.")
        return

    print("\nDigite os novos dados:")

    mes = int(input("Novo mês (1-12): "))
    dia = input("Novo dia (01-31): ")
    hora = input("Hora (00-23): ")
    minuto = input("Minutos (00-59): ")
    evento = input("Nova descrição: ")

    horario = f"{int(hora):02d}:{int(minuto):02d}"

    comando4 = """
    UPDATE calendario
    SET mes = ?, dia = ?, horario = ?, evento = ?
    WHERE id = ?;
    """

    cursor.execute(comando4, (mes, dia, horario, evento, eid))
    conn.commit()

    print("\n[OK] Evento atualizado.")

# =======================
# 6) REMOVER EVENTO
# =======================
def remover_evento(conn):
    cursor = conn.cursor()
    listar_eventos(conn)

    try:
        eid = int(input("\nID para excluir: ").strip())
    except:
        print("ID inválido.")
        return

    comando5 = "DELETE FROM calendario WHERE id = ?;"

    cursor.execute(comando5, (eid,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Nenhum evento removido.")
    else:
        print("[OK] Evento removido.")

# =======================
# 7) PROGRAMA PRINCIPAL
# =======================
def main():
    print("Olá! Seja bem-vindo ao seu Calendário.")
    nome = input("Qual seu nome? ")

    conn = criar_conexao(nome)
    criar_tabela(conn)

    while True:
        print("""
===== MENU =====
1) Inserir evento
2) Listar eventos
3) Atualizar evento
4) Remover evento
5) Sair
""")
        opc = input("Escolha: ").strip()

        if opc == "1":
            inserir_evento(conn)
        elif opc == "2":
            listar_eventos(conn)
        elif opc == "3":
            atualizar_evento(conn)
        elif opc == "4":
            remover_evento(conn)
        elif opc == "5":
            print("Saindo...")
            conn.close()
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
