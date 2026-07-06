import bcrypt

def gerar_hash(senha):
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_gerado = bcrypt.hashpw(senha_bytes, salt)
    return hash_gerado.decode("utf-8")

def verificar_senha(senha_digitada, hash_salvo):
    return bcrypt.checkpw(senha_digitada.encode("utf-8"), hash_salvo.encode("utf-8"))          

