#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar o banco de dados com as novas funcionalidades do NeuroLearn
Equipe Control + Amizade - CodeRace 2025
"""

import sqlite3
import os
from datetime import datetime

def criar_backup():
    """Cria backup do banco atual"""
    if os.path.exists('sistema_educacional.db'):
        backup_name = f'sistema_educacional_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db'
        os.system(f'copy sistema_educacional.db {backup_name}')
        print(f"✅ Backup criado: {backup_name}")
        return True
    return False

def atualizar_banco():
    """Adiciona as novas tabelas ao banco de dados"""
    conn = sqlite3.connect('sistema_educacional.db')
    cursor = conn.cursor()
    
    try:
        print("🔄 Iniciando atualização do banco de dados...")
        
        # 1. Teste de Perfil Cognitivo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teste_perfili_cognitivo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                tipo_teste VARCHAR(50) NOT NULL,
                pontuacao INTEGER NOT NULL,
                tempo_resposta INTEGER,
                data_teste DATETIME DEFAULT CURRENT_TIMESTAMP,
                resultados_detalhados TEXT,
                FOREIGN KEY (aluno_id) REFERENCES aluno(id)
            )
        ''')
        print("✅ Tabela teste_perfili_cognitivo criada")
        
        # 2. Trilhas de Aprendizado
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trilha_aprendizado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200) NOT NULL,
                descricao TEXT,
                tipo_conteudo VARCHAR(50) NOT NULL,
                nivel_dificuldade VARCHAR(20) NOT NULL,
                area_conhecimento VARCHAR(100) NOT NULL,
                perfil_alvo VARCHAR(100),
                duracao_estimada INTEGER,
                url_conteudo VARCHAR(500),
                arquivo_conteudo VARCHAR(200),
                ativo BOOLEAN DEFAULT 1,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✅ Tabela trilha_aprendizado criada")
        
        # 3. Progresso nas Trilhas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS progresso_trilha (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                trilha_id INTEGER NOT NULL,
                progresso REAL DEFAULT 0.0,
                tempo_gasto INTEGER DEFAULT 0,
                data_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_conclusao DATETIME,
                feedback_aluno TEXT,
                dificuldade_percebida INTEGER,
                FOREIGN KEY (aluno_id) REFERENCES aluno(id),
                FOREIGN KEY (trilha_id) REFERENCES trilha_aprendizado(id)
            )
        ''')
        print("✅ Tabela progresso_trilha criada")
        
        # 4. Cronograma de Estudos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cronograma_estudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                data_inicio DATE NOT NULL,
                data_fim DATE NOT NULL,
                objetivo VARCHAR(200) NOT NULL,
                horas_por_dia REAL NOT NULL,
                dias_semana VARCHAR(20) NOT NULL,
                horario_preferido VARCHAR(20),
                tempo_pausa INTEGER DEFAULT 10,
                tempo_sessao INTEGER DEFAULT 25,
                lembretes_ativos BOOLEAN DEFAULT 1,
                ativo BOOLEAN DEFAULT 1,
                FOREIGN KEY (aluno_id) REFERENCES aluno(id)
            )
        ''')
        print("✅ Tabela cronograma_estudo criada")
        
        # 5. Sessões de Estudo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessao_estudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cronograma_id INTEGER NOT NULL,
                data_sessao DATETIME NOT NULL,
                duracao_planejada INTEGER NOT NULL,
                duracao_real INTEGER,
                realizada BOOLEAN DEFAULT 0,
                feedback TEXT,
                nivel_concentracao INTEGER,
                trilha_estudada INTEGER,
                FOREIGN KEY (cronograma_id) REFERENCES cronograma_estudo(id),
                FOREIGN KEY (trilha_estudada) REFERENCES trilha_aprendizado(id)
            )
        ''')
        print("✅ Tabela sessao_estudo criada")
        
        # 6. Biblioteca de Conteúdo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS biblioteca_conteudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(200) NOT NULL,
                descricao TEXT,
                tipo VARCHAR(50) NOT NULL,
                categoria VARCHAR(100) NOT NULL,
                nivel_ensino VARCHAR(20),
                url_conteudo VARCHAR(500),
                arquivo_conteudo VARCHAR(200),
                tem_legenda BOOLEAN DEFAULT 0,
                tem_libras BOOLEAN DEFAULT 0,
                tem_transcricao VARCHAR(500),
                duracao INTEGER,
                classificacao_etaria VARCHAR(10),
                tags VARCHAR(500),
                ativo BOOLEAN DEFAULT 1,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✅ Tabela biblioteca_conteudo criada")
        
        # 7. Monitoramento de Comportamento
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS monitoramento_comportamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                data_acao DATETIME DEFAULT CURRENT_TIMESTAMP,
                tipo_acao VARCHAR(50) NOT NULL,
                contexto VARCHAR(100),
                tempo_gasto INTEGER,
                dispositivo VARCHAR(50),
                resultado VARCHAR(20),
                detalhes TEXT,
                FOREIGN KEY (aluno_id) REFERENCES aluno(id)
            )
        ''')
        print("✅ Tabela monitoramento_comportamento criada")
        
        # 8. Configurações de Acessibilidade
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS configuracao_acessibilidade (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL UNIQUE,
                modo_escuro BOOLEAN DEFAULT 0,
                alto_contraste BOOLEAN DEFAULT 0,
                tamanho_fonte VARCHAR(20) DEFAULT 'normal',
                audio_leitura BOOLEAN DEFAULT 0,
                velocidade_audio REAL DEFAULT 1.0,
                navegacao_simplificada BOOLEAN DEFAULT 0,
                reducao_animacoes BOOLEAN DEFAULT 0,
                notificacoes_visuais BOOLEAN DEFAULT 1,
                notificacoes_sonoras BOOLEAN DEFAULT 1,
                cores_personalizadas VARCHAR(500),
                FOREIGN KEY (usuario_id) REFERENCES usuario(id)
            )
        ''')
        print("✅ Tabela configuracao_acessibilidade criada")
        
        # 9. Interações com Assistente Virtual
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interacao_assistente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                mensagem_usuario TEXT NOT NULL,
                resposta_assistente TEXT NOT NULL,
                contexto VARCHAR(100),
                satisfacao_resposta INTEGER,
                data_interacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                resolveu_duvida BOOLEAN,
                FOREIGN KEY (usuario_id) REFERENCES usuario(id)
            )
        ''')
        print("✅ Tabela interacao_assistente criada")
        
        # Inserir dados de exemplo
        inserir_dados_exemplo(cursor)
        
        conn.commit()
        print("\n🎉 Banco de dados atualizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar banco: {e}")
        conn.rollback()
    finally:
        conn.close()

def inserir_dados_exemplo(cursor):
    """Insere alguns dados de exemplo para testar as novas funcionalidades"""
    print("\n📦 Inserindo dados de exemplo...")
    
    # Trilhas de exemplo
    trilhas_exemplo = [
        ('Matemática Básica - Visual', 'Trilha de matemática com foco em elementos visuais', 'video', 'facil', 'matematica', 'Visual', 60, '', '', 1),
        ('Português - Auditivo', 'Trilha de português com áudios e podcasts', 'audio', 'medio', 'portugues', 'Auditivo', 45, '', '', 1),
        ('Ciências - Prático', 'Experimentos práticos de ciências', 'jogo', 'medio', 'ciencias', 'Sinestésico', 90, '', '', 1),
        ('Lógica e Programação', 'Introdução à programação e lógica', 'texto', 'dificil', 'tecnologia', 'Lógico', 120, '', '', 1)
    ]
    
    for trilha in trilhas_exemplo:
        cursor.execute('''
            INSERT OR IGNORE INTO trilha_aprendizado 
            (nome, descricao, tipo_conteudo, nivel_dificuldade, area_conhecimento, perfil_alvo, duracao_estimada, url_conteudo, arquivo_conteudo, ativo) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', trilha)
    
    # Conteúdo da biblioteca
    conteudos_exemplo = [
        ('Podcast de História do Brasil', 'Episódios sobre a história brasileira', 'podcast', 'historia', 'fundamental2', '', '', 1, 0, '', 30, 'livre', 'historia,brasil,educativo', 1),
        ('Vídeo: Matemática para Todos', 'Vídeo explicativo sobre matemática básica', 'video', 'matematica', 'fundamental1', '', '', 1, 1, '', 15, 'livre', 'matematica,basico,inclusivo', 1),
        ('Jogo: Palavras Cruzadas', 'Jogo educativo de português', 'jogo', 'portugues', 'fundamental2', '', '', 0, 0, '', 0, 'livre', 'portugues,jogo,palavras', 1),
        ('Vídeo: Ciências da Natureza', 'Documentário sobre meio ambiente', 'video', 'ciencias', 'medio', '', '', 1, 1, '', 45, 'livre', 'ciencias,natureza,meio-ambiente', 1)
    ]
    
    for conteudo in conteudos_exemplo:
        cursor.execute('''
            INSERT OR IGNORE INTO biblioteca_conteudo 
            (titulo, descricao, tipo, categoria, nivel_ensino, url_conteudo, arquivo_conteudo, tem_legenda, tem_libras, tem_transcricao, duracao, classificacao_etaria, tags, ativo) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', conteudo)
    
    print("✅ Dados de exemplo inseridos")

def verificar_tabelas():
    """Verifica se todas as tabelas foram criadas corretamente"""
    conn = sqlite3.connect('sistema_educacional.db')
    cursor = conn.cursor()
    
    tabelas_esperadas = [
        'teste_perfili_cognitivo',
        'trilha_aprendizado',
        'progresso_trilha',
        'cronograma_estudo',
        'sessao_estudo',
        'biblioteca_conteudo',
        'monitoramento_comportamento',
        'configuracao_acessibilidade',
        'interacao_assistente'
    ]
    
    print("\n🔍 Verificando tabelas criadas:")
    
    for tabela in tabelas_esperadas:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tabela,))
        resultado = cursor.fetchone()
        
        if resultado:
            # Contar registros
            cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
            count = cursor.fetchone()[0]
            print(f"  ✅ {tabela} - {count} registros")
        else:
            print(f"  ❌ {tabela} - NÃO ENCONTRADA")
    
    conn.close()

def main():
    print("🚀 NeuroLearn - Atualização do Banco de Dados")
    print("🏢 Equipe Control + Amizade - CodeRace 2025")
    print("="*50)
    
    # Criar backup
    if criar_backup():
        print("📁 Backup do banco atual criado com sucesso")
    
    # Atualizar banco
    atualizar_banco()
    
    # Verificar resultado
    verificar_tabelas()
    
    print("\n" + "="*50)
    print("🎯 Atualização concluída!")
    print("\n📋 Novas funcionalidades disponíveis:")
    print("   1. ✅ Teste de perfil cognitivo")
    print("   2. ✅ Trilhas personalizadas de aprendizado")
    print("   3. ✅ Cronograma de estudos adaptado")
    print("   4. ✅ Painel de progresso")
    print("   5. ✅ Assistente virtual")
    print("   6. ✅ Interface acessível")
    print("   7. ✅ Biblioteca com podcasts e vídeos")
    print("   8. ✅ Monitoramento de comportamento")
    
    print("\n🎉 Sistema NeuroLearn atualizado com sucesso!")

if __name__ == '__main__':
    main()

