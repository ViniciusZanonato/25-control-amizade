#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para debugar o problema do questionário NeuroLearn
Testa todo o fluxo desde o login até o acesso ao dashboard
"""

from app import app, db, Usuario, Aluno, QuestionarioNeuroLearn, PerfilAprendizagem, gerar_perfil_aprendizagem
from werkzeug.security import generate_password_hash
import json

def resetar_aluno_teste():
    """Reset do aluno de teste para recriar o problema"""
    with app.app_context():
        # Buscar ou criar usuário de teste
        usuario = Usuario.query.filter_by(email='debug@aluno.com').first()
        if usuario:
            # Deletar perfil existente
            aluno = Aluno.query.filter_by(usuario_id=usuario.id).first()
            if aluno:
                # Limpar dados relacionados
                QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno.id).delete()
                PerfilAprendizagem.query.filter_by(aluno_id=aluno.id).delete()
                
                # Resetar flags
                aluno.questionario_completo = False
                aluno.perfil_gerado = False
                db.session.commit()
                print(f"✅ Aluno resetado - ID: {aluno.id}")
                return aluno
        
        # Criar novo usuário se não existe
        usuario = Usuario(
            nome='Debug Aluno',
            email='debug@aluno.com',
            senha_hash=generate_password_hash('123456'),
            tipo='aluno'
        )
        db.session.add(usuario)
        db.session.commit()
        
        aluno = Aluno(
            usuario_id=usuario.id,
            email_escola='debug@escola.com',
            serie_ano='9º ano',
            professor_responsavel='Prof. Debug',
            idade=15
        )
        db.session.add(aluno)
        db.session.commit()
        print(f"✅ Novo aluno criado - ID: {aluno.id}")
        return aluno

def simular_questionario_completo(aluno_id):
    """Simula o preenchimento completo do questionário"""
    with app.app_context():
        aluno = Aluno.query.get(aluno_id)
        print(f"🔍 Estado inicial - Questionário: {aluno.questionario_completo}, Perfil: {aluno.perfil_gerado}")
        
        # Simular respostas variadas (não só 3)
        respostas_simuladas = {
            # Bloco 1 - Percepção Sensorial (questões 1-10)
            1: [4, 2, 3, 5, 4, 2, 3, 1, 4, 3],
            # Bloco 2 - Atenção e Foco (questões 11-20) 
            2: [3, 4, 2, 3, 2, 4, 3, 5, 2, 4],
            # Bloco 3 - Comunicação (questões 21-30)
            3: [2, 3, 4, 3, 2, 4, 3, 2, 4, 3],
            # Bloco 4 - Organização (questões 31-40)
            4: [4, 3, 4, 2, 3, 4, 5, 3, 4, 3],
            # Bloco 5 - Aprendizagem (questões 41-50)
            5: [4, 5, 2, 4, 3, 4, 3, 4, 5, 3],
            # Bloco 6 - Interação Social (questões 51-60)
            6: [3, 2, 4, 3, 2, 3, 4, 3, 2, 4],
            # Bloco 7 - Criatividade (questões 61-67)
            7: [5, 4, 5, 4, 3, 5, 4]
        }
        
        questao_id = 1
        for bloco, respostas in respostas_simuladas.items():
            for resposta_valor in respostas:
                questionario = QuestionarioNeuroLearn(
                    aluno_id=aluno_id,
                    bloco=bloco,
                    questao=questao_id,
                    resposta=resposta_valor
                )
                db.session.add(questionario)
                questao_id += 1
        
        # Marcar como completo
        aluno.questionario_completo = True
        db.session.commit()
        
        total_respostas = QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno_id).count()
        print(f"📝 Questionário simulado - {total_respostas} respostas salvas")
        
        return True

def testar_geracao_perfil(aluno_id):
    """Testa a geração do perfil"""
    with app.app_context():
        aluno = Aluno.query.get(aluno_id)
        print(f"🤖 Iniciando geração do perfil para aluno {aluno_id}")
        
        try:
            gerar_perfil_aprendizagem(aluno_id)
            
            # Recarregar do banco
            aluno = Aluno.query.get(aluno_id)
            perfil = PerfilAprendizagem.query.filter_by(aluno_id=aluno_id).first()
            
            print(f"✅ Perfil gerado com sucesso!")
            print(f"   - Questionário completo: {aluno.questionario_completo}")
            print(f"   - Perfil gerado: {aluno.perfil_gerado}")
            print(f"   - Perfil no banco: {'Sim' if perfil else 'Não'}")
            
            if perfil:
                print(f"   - Tipo de perfil: {perfil.tipo_perfil}")
                print(f"   - Data de geração: {perfil.data_geracao}")
            
            return True
        except Exception as e:
            print(f"❌ Erro ao gerar perfil: {e}")
            return False

def testar_acesso_dashboard(aluno_id):
    """Testa se o aluno consegue acessar o dashboard"""
    with app.app_context():
        aluno = Aluno.query.get(aluno_id)
        
        print(f"🏠 Testando acesso ao dashboard:")
        print(f"   - Questionário completo: {aluno.questionario_completo}")
        print(f"   - Perfil gerado: {aluno.perfil_gerado}")
        
        # Simular a lógica do dashboard_aluno
        if not aluno.questionario_completo:
            print("⚠️ PROBLEMA: Aluno seria redirecionado para questionário")
            return False
        else:
            print("✅ Aluno pode acessar o dashboard")
            return True

def main():
    """Função principal para testar todo o fluxo"""
    print("🧠 NEUROLEARN - TESTE DE DEBUG DO QUESTIONÁRIO")
    print("=" * 50)
    
    # 1. Resetar aluno de teste
    print("\n1️⃣ Resetando aluno de teste...")
    aluno = resetar_aluno_teste()
    
    # 2. Testar estado inicial
    print("\n2️⃣ Testando acesso inicial (deve redirecionar para questionário)...")
    testar_acesso_dashboard(aluno.id)
    
    # 3. Simular questionário completo
    print("\n3️⃣ Simulando preenchimento do questionário...")
    simular_questionario_completo(aluno.id)
    
    # 4. Testar geração do perfil
    print("\n4️⃣ Testando geração do perfil...")
    sucesso_perfil = testar_geracao_perfil(aluno.id)
    
    # 5. Testar acesso final ao dashboard
    print("\n5️⃣ Testando acesso final ao dashboard...")
    sucesso_dashboard = testar_acesso_dashboard(aluno.id)
    
    print("\n" + "=" * 50)
    if sucesso_perfil and sucesso_dashboard:
        print("✅ TESTE CONCLUÍDO COM SUCESSO!")
        print("   O fluxo do questionário está funcionando corretamente.")
        print(f"   Aluno de teste: debug@aluno.com (senha: 123456)")
    else:
        print("❌ PROBLEMA IDENTIFICADO!")
        print("   Verificar logs acima para detalhes do erro.")

if __name__ == '__main__':
    main()

