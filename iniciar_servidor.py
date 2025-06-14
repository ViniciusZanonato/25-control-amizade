#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 NeuroLearn - Sistema de Identificação de Neurodivergência
📅 Equipe: Control + Amizade - CodeRace 2025
🚀 Script de inicialização do servidor Flask
"""

import os
import sys
from datetime import datetime
from app import app, db, Usuario, Aluno, Professor

def exibir_info_acesso():
    """Exibe informações de acesso ao sistema"""
    print("\n" + "="*80)
    print("🧠 NEUROLEARN - SISTEMA DE IDENTIFICAÇÃO DE NEURODIVERGÊNCIA")
    print("👥 Equipe: Control + Amizade | 📅 CodeRace 2025")
    print("="*80)
    
    print("\n🌐 ACESSO AO SISTEMA:")
    print("🔗 URL Principal: http://127.0.0.1:5000")
    print("🔗 Página de Login: http://127.0.0.1:5000/login")
    print("🔗 Registro de Aluno: http://127.0.0.1:5000/registro")
    
    with app.app_context():
        # Contar usuários
        total_usuarios = Usuario.query.count()
        total_alunos = Aluno.query.count()
        total_professores = Professor.query.count()
        
        print(f"\n📊 ESTATÍSTICAS DO BANCO DE DADOS:")
        print(f"👥 Total de usuários: {total_usuarios}")
        print(f"👨‍🎓 Alunos registrados: {total_alunos}")
        print(f"👨‍🏫 Professores: {total_professores}")
        print(f"🕒 Status: {'✅ Banco inicializado' if total_usuarios > 0 else '⚠️ Banco vazio'}")
    
    # Verificar se existem dados de teste
    with app.app_context():
        professor_teste = Usuario.query.filter_by(email='professor@teste.com').first()
        alunos_teste = Usuario.query.filter(Usuario.email.like('aluno%@teste.com')).count()
        
        if professor_teste and alunos_teste > 0:
            print("\n🎯 DADOS DE TESTE DISPONÍVEIS:")
            print("\n👨‍🏫 PROFESSOR DE TESTE:")
            print("📧 Email: professor@teste.com")
            print("🔑 Senha: 123456")
            print("👤 Nome: Prof. Maria Silva")
            print("🎯 Funcionalidades: Dashboard, visualizar perfis, criar atividades")
            
            print("\n👥 ALUNOS DE TESTE (10 alunos com questionários respondidos):")
            
            # Buscar todos os alunos de teste
            alunos = db.session.query(Usuario, Aluno).join(Aluno).filter(
                Usuario.email.like('aluno%@teste.com')
            ).order_by(Usuario.email).all()
            
            for usuario, aluno in alunos:
                email_num = usuario.email.split('@')[0]  # aluno1, aluno2, etc.
                print(f"   {email_num}@teste.com / 123456 - {usuario.nome} ({aluno.serie_ano})")
            
            print("\n🧠 PERFIS DE APRENDIZAGEM GERADOS:")
            print("✅ Todos os alunos têm questionários completos")
            print("✅ Perfis gerados automaticamente pela IA")
            print("✅ Diferentes tipos: Criativo, Organizador, Social, etc.")
            
            print("\n💡 COMO TESTAR:")
            print("1. Login como PROFESSOR: professor@teste.com / 123456")
            print("2. Acesse 'Painel Professor' para ver todos os alunos")
            print("3. Visualize perfis detalhados de cada aluno")
            print("4. Teste filtros por tipo de perfil")
            print("5. Login como ALUNO: aluno1@teste.com / 123456 (ou qualquer outro)")
            print("6. Veja o dashboard do aluno (sem acesso ao próprio perfil completo)")
            
        else:
            print("\n⚠️ DADOS DE TESTE NÃO ENCONTRADOS:")
            print("\n🔧 Para gerar dados de teste:")
            print("   python gerar_dados_teste.py")
            
            print("\n👨‍🏫 ACESSO PROFESSOR (MANUAL):")
            print("📧 Use a página de registro para criar um professor")
            print("🎯 Tipo: Professor")
            
            print("\n👨‍🎓 REGISTRO DE ALUNOS (MANUAL):")
            print("📝 Use a página de registro para criar novos alunos")
            print("🔒 Cada aluno terá acesso apenas ao seu próprio dashboard")
            print("📋 Questionário NeuroLearn disponível após registro")
    
    print("\n🔍 FUNCIONALIDADES PRINCIPAIS PARA TESTAR:")
    print("✅ Sistema de registro e autenticação")
    print("✅ Questionário NeuroLearn (67 questões especializadas)")
    print("✅ Análise por Inteligência Artificial (Google Gemini)")
    print("✅ Geração de perfis de aprendizagem personalizados")
    print("✅ Dashboard diferenciado para professor e aluno")
    print("✅ Relatórios detalhados e filtrados")
    print("✅ Sistema de proteção de dados (LGPD)")
    
    print("\n📋 FLUXO DE TESTE RECOMENDADO:")
    print("1. 👨‍🏫 Login como professor para acessar dashboard")
    print("2. 👨‍🎓 Registrar novo aluno através da página de registro")
    print("3. 📝 Fazer login como aluno e responder questionário")
    print("4. 🤖 Aguardar análise por IA e geração do perfil")
    print("5. 👨‍🏫 Visualizar relatório completo como professor")
    print("6. 📊 Testar filtros e funcionalidades avançadas")
    
    print("\n📖 DOCUMENTAÇÃO:")
    print("📄 README.md - Documentação completa do projeto")
    print("🔧 requirements.txt - Dependências do sistema")
    print("🗃️ Banco: sistema_educacional.db (SQLite)")
    
    print("\n⚡ TECNOLOGIAS:")
    print("🐍 Python 3.6+ com Flask")
    print("🤖 Google Gemini API para análise de IA")
    print("🗄️ SQLite para armazenamento de dados")
    print("🔒 Sistema de segurança e validação integrado")
    
    print("\n🎉 DIFERENCIAL DO NEUROLEARN:")
    print("🧠 Baseado em Ontopsicologia")
    print("📊 67 questões especializadas")
    print("🎯 Detecção de TDAH, TEA, Dislexia e Superdotação")
    print("🔍 Sistema anti-fraude e detecção de inconsistências")
    print("👨‍🏫 Interface específica para educadores")
    
    print("\n" + "="*80)
    print("🚀 SERVIDOR RODANDO - Pressione Ctrl+C para parar")
    print("="*80 + "\n")

if __name__ == '__main__':
    # Verificar se o banco existe e tem dados
    with app.app_context():
        try:
            # Tentar criar as tabelas se não existirem
            db.create_all()
            total_users = Usuario.query.count()
            if total_users == 0:
                print("⚠️ ATENÇÃO: Banco de dados vazio!")
                print("💡 Execute primeiro: python init_db.py")
                print("📝 Ou use a página de registro para criar novos usuários")
                # Não encerrar, permitir que o servidor rode mesmo com banco vazio
        except Exception as e:
            print(f"❌ Erro ao acessar banco de dados: {e}")
            print("💡 Execute primeiro: python init_db.py")
            sys.exit(1)
    
    # Exibir informações de acesso
    exibir_info_acesso()
    
    # Iniciar servidor
    try:
        # Verificar se é ambiente de desenvolvimento
        debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
        app.run(debug=debug_mode, host='127.0.0.1', port=5000)
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor parado pelo usuário")
        print("✅ Obrigado por testar o NeuroLearn!")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar servidor: {e}")

