import re
import sqlite3

login = {} # Usuario e Senha
perfil = {} # Nome e Email por login
email_re = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

_conn = sqlite3.connect('exemplo.db')
_cur = _conn.cursor()

# 1) Criar tabelas se não existirem
_cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    username TEXT PRIMARY KEY,
    senha    TEXT NOT NULL
);
""")
_cur.execute("""
CREATE TABLE IF NOT EXISTS perfis (
    username TEXT PRIMARY KEY,
    nome     TEXT NOT NULL,
    email    TEXT NOT NULL,
    FOREIGN KEY (username) REFERENCES usuarios(username) ON DELETE CASCADE
);
""")
_conn.commit()

# 2) Carregar dicionários login/perfil a partir do banco
for u, s in _cur.execute("SELECT username, senha FROM usuarios;").fetchall():
    login[u] = s
for u, n, e in _cur.execute("SELECT username, nome, email FROM perfis;").fetchall():
    perfil[u] = {"nome": n, "email": e}
    
def criar_conta():
    while True:
        print("CRIAÇÃO DE CONTA - Hub de Gastos - YMarinhoTech")
        user = input("Crie um nome de usuario:\nsem ultrapassar 20 caracteres\n").strip().lower()
        print()
        if not user:
            print("Usuario está em branco!\n")
            continue
        elif len(user) > 20:
            print("Você não pode ultrapassar 20 caracteres\n")
            continue
        while True:
            password = input("Crie sua senha\ncom 8 a 20 caracteres\n").strip()
            print()
            if len(password) < 8 or len(password) >= 20:
                print("senha tem que ser de 8 a 20 caracteres\n")
                continue
            login[user] = password

            _cur.execute(
                "INSERT OR REPLACE INTO usuarios (username, senha) VALUES (?, ?);",
                (user, password)
            )
            _conn.commit()

            print(f"Conta '{user}' salva no banco com sucesso!\n")
            break
        break

def login_conta():
    if not login:
        print("Não existem logins cadastrados no momento\n")
    else:
        while True:
            print("LOGIN - Hub de Gastos - YMarinhoTech")
            login_user = input("Coloque nome de usuario:\n").strip().lower()
            print()
            if not login_user:
                print("Nome está em branco!\n")
                continue
            login_password = input("Coloque sua senha:\n").strip()
            print()
            if login_user in login:
                if login[login_user] == login_password:
                    print("Login bem-sucedido! Bem-vindo(a) ao Instagram 2025.\n")
                    info_login(login_user)
                    return True

                else:
                    print("Senha incorreta. Tente novamente.\n")
                    break
            else:
                print("Usuário não encontrado. Tente novamente.\n")
                break
        
def info_login(login_user): 
    # só pergunta nome/email se faltar no perfil
    user_perfil = perfil.get(login_user, {"nome": None, "email": None})
    
    if not user_perfil.get("nome") or not user_perfil.get("email"):
        while True:
            nome = input(f"Olá {login_user}, qual seu nome verdadeiro?\n").strip()
            print()
            if not nome:
                print("Nome está em branco!\n")
                continue
            try:
                confirm_nome = int(input(f"Seu nome é {nome}, Correto?\n1) Sim\n2) Não\n"))
                print()
            except ValueError:
                print("Aceitamos apenas os números 1 e 2 como resposta!")
                continue
            if confirm_nome == 1:
                break
            elif confirm_nome == 2:
                continue
            else:
                print("Aceitamos apenas os números 1 e 2 como resposta!")
                continue
        while True:
            email = input(f"Certo {nome}, Agora precisamos apenas de seu email:\n").strip().lower()
            print()
            if email_re.fullmatch(email):
                try:
                    confirm_email = int(input(f"Seu email é {email}, Correto?\n1) Sim\n2) Não\n"))
                    print()
                except ValueError:
                    print("Aceitamos apenas os números 1 e 2 como resposta!")
                    continue
                if confirm_email == 1:
                    perfil[login_user] = {"nome": nome, "email": email}
                    print(f"\nDados atualizados com sucesso:")
                    print(f"Usuário: {login_user}\nEmail: {email}\nNome: {nome}\n")
                    
                    _cur.execute("""
                        INSERT INTO perfis (username, nome, email)
                        VALUES (?, ?, ?)
                        ON CONFLICT(username) DO UPDATE SET
                            nome = excluded.nome,
                            email = excluded.email;
                    """, (login_user, nome, email))
                    _conn.commit()

                    print("Perfil salvo no banco!\n")
                    break
                elif confirm_email == 2:
                    continue
            else:
                print(f"seu email tem que ser algo como: {nome.lower()}012@email.com\n")
                continue

def esqueceu_senha():
    if not login:
        print("Não existem logins cadastrados no momento\n")
    else:
        while True:
            email = input("Insira o email vinculado a conta:\n")
            print()
            if email_re.fullmatch(email):
                print(f"Enviamos um email para: {email} com as informações referentes a recuperação de sua conta!\ncaso esse email não esteja vinculado no sistema, ele não será enviado.\n")
                break
            else:
                print(f"E-mail inválido, coloque algo como  exemplo2025@gmail.com\n")
                break

def main():
    while True:
        print("======== PAGINA DE LOGIN ========\n")
        try:
            escolha = int(input("1) Cadastrar conta\n2) Fazer login\n3) Esqueci a senha\n"))
            print()
        except ValueError:
            print("Aceitamos apenas os números 1 a 3 como resposta!")
            continue
        if escolha == 1:
            criar_conta()
        elif escolha == 2:
            ok = login_conta()
            if ok:
                return True
        elif escolha == 3:
            esqueceu_senha()
        else:
            print("Aceitamos apenas os números 1 a 3 como resposta!\n")

def shutdown():
    try:
        _conn.close()
    except Exception:
        pass

if __name__ == "__main__":
    try:
        main()
    finally:
        shutdown()