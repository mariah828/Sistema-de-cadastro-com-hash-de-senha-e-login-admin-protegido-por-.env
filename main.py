import database
import getpass
import auth
import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_SENHA = os.getenv("ADMIN_SENHA")

cursor = database.conexao.cursor()
    
def procurarLogin(nome):
    nome = nome.strip().lower()

    cursor.execute(
    "SELECT nome FROM usuarios WHERE nome = ?",
        (nome,)
    )

    repeat = cursor.fetchone()
    return repeat

def cadastro(nome, senha):
    nome = nome.strip().lower()
    repeat = procurarLogin(nome)

    if repeat is None:
        senha_hash = auth.gerar_hash(senha) 

        cursor.execute(
            "INSERT INTO usuarios (nome, senha) VALUES (?,?)",
            (nome, senha_hash)
        )
        database.conexao.commit()

        cursor.execute("SELECT * FROM usuarios")

        print("Usuário cadastrado!")
        return True
    
    else:
        print("O usuário já foi cadastrado!")
        return False

def admin():
    user = input("Digite o user: ")
    key = getpass.getpass("Digite a key: ")

    if user != ADMIN_USER or key != ADMIN_SENHA:
        print("Você não tem acesso a essa informação")
    else:
        cursor.execute("SELECT * FROM usuarios")
        print(total)


while True:
    nome = input("Digite o nome do perfil: ")
    senha = getpass.getpass("Digite a senha do perfil: ")

    if cadastro(nome, senha):
        if nome == ADMIN_USER and senha == ADMIN_SENHA:
            print("Parece que você é um admin.")
            print("Para acessar a quantidade de alunos cadastrados, digite o user a key novamente!")
            total = cursor.fetchall()
            admin()
            break
        else:
            total = cursor.fetchall()
            break

database.conexao.commit()
database.conexao.close()
    



