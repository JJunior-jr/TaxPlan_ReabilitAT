from werkzeug.security import generate_password_hash, check_password_hash

def create_user(nome, senha, tipo_usuario):
    hashed_password = generate_password_hash(senha)
    # Adicionar lógica para inserir o usuário no banco de dados

def verify_user(nome, senha):


# Lógica para verificar o usuário e a senha no banco de dados