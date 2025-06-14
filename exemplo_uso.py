#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 NeuroLearn - Exemplo de Uso do Sistema
👥 Equipe: Control + Amizade - CodeRace 2025
📝 Script demonstrativo para teste do sistema
"""

import subprocess
import sys
import time

def main():
    print("🧠 NeuroLearn - Sistema de Identificação de Neurodivergência")
    print("👥 Equipe: Control + Amizade | 📅 CodeRace 2025")
    print("="*60)
    
    print("\n🚀 GUIA DE USO RÁPIDO:")
    print("\n1️⃣ Para iniciar o servidor:")
    print("   python iniciar_servidor.py")
    
    print("\n2️⃣ Para resetar o banco (manter professor):")
    print("   python init_db.py")
    
    print("\n3️⃣ URLs importantes:")
    print("   🏠 Página inicial: http://127.0.0.1:5000")
    print("   🔐 Login: http://127.0.0.1:5000/login")
    print("   📝 Registro: http://127.0.0.1:5000/registro")
    
    print("\n4️⃣ Credenciais do professor:")
    print("   📧 Email: professor@test.com")
    print("   🔑 Senha: 123456")
    
    print("\n5️⃣ Fluxo de teste recomendado:")
    print("   a) Faça login como professor")
    print("   b) Registre um novo aluno")
    print("   c) Faça login como aluno")
    print("   d) Responda o questionário NeuroLearn")
    print("   e) Veja o perfil gerado pela IA")
    print("   f) Acesse como professor para ver relatórios")
    
    print("\n✨ FUNCIONALIDADES ESPECIAIS:")
    print("   🤖 Análise por IA (Google Gemini)")
    print("   📊 67 questões especializadas")
    print("   🔍 Detecção de inconsistências")
    print("   🎯 Perfis de neurodivergência")
    print("   📋 Relatórios detalhados")
    
    print("\n" + "="*60)
    
    opcao = input("\n❓ Deseja iniciar o servidor agora? (s/N): ").lower()
    if opcao in ['s', 'sim', 'y', 'yes']:
        print("\n🚀 Iniciando servidor...")
        try:
            subprocess.run([sys.executable, "iniciar_servidor.py"])
        except KeyboardInterrupt:
            print("\n🛑 Servidor parado")
    else:
        print("\n👋 Para iniciar o servidor manualmente, execute:")
        print("   python iniciar_servidor.py")

if __name__ == '__main__':
    main()

