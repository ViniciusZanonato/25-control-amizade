from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

# Configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema_educacional.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def migrar_banco():
    """Migra o banco de dados adicionando a coluna idade se ela não existir"""
    db_path = 'sistema_educacional.db'
    
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Verificar se a coluna idade existe
        cursor.execute("PRAGMA table_info(aluno)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'idade' not in columns:
            print("Adicionando coluna 'idade' à tabela aluno...")
            cursor.execute("ALTER TABLE aluno ADD COLUMN idade INTEGER DEFAULT 16")
            conn.commit()
            print("Coluna 'idade' adicionada com sucesso!")
        else:
            print("Coluna 'idade' já existe na tabela aluno.")
        
        # Atualizar idades para alunos existentes (se houver)
        cursor.execute("UPDATE aluno SET idade = 16 WHERE idade IS NULL OR idade = 0")
        conn.commit()
        print("Idades padrão definidas para alunos existentes.")
        
    except Exception as e:
        print(f"Erro durante a migração: {e}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == '__main__':
    with app.app_context():
        print("Iniciando migração do banco de dados...")
        migrar_banco()
        print("Migração concluída!")

