# Sistema de Cadastro de Usuários

Sistema simples em Python + SQLite para cadastro de usuários, com:
- Hash de senha (bcrypt) para os usuários cadastrados
- Painel de admin protegido por variáveis de ambiente (.env)
- Proteção contra SQL Injection via queries parametrizadas

## Tecnologias
- Python
- SQLite
- bcrypt
- python-dotenv

## Como rodar

1. Clone o repositório
2. Instale as dependências:
   pip install -r requirements.txt
3. Copie o `.env.example` para `.env` e preencha com seu usuário/senha de admin:
   ADMIN_USER=seu_usuario
   ADMIN_SENHA=sua_senha
4. Rode o programa:
   python main.py

## Decisões de segurança

- As senhas dos usuários cadastrados nunca são salvas em texto puro — 
  são transformadas em hash com bcrypt antes de ir pro banco.
- As credenciais do admin ficam fora do código-fonte, em variáveis 
  de ambiente (.env), que nunca é enviado ao repositório (veja .gitignore).
- Todas as consultas ao banco usam parâmetros (?) em vez de concatenar 
  strings, prevenindo SQL Injection.
