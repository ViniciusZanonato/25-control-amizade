
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar o fluxo web completo do questionário NeuroLearn
Simula exatamente o processo que um usuário faria no navegador
"""

import requests
import json
from app import app, db, Usuario, Aluno, QuestionarioNeuroLearn, PerfilAprendizagem
from werkzeug.security import generate_password_hash

def testar_fluxo_web_completo():
    """Testa o fluxo completo via requisições HTTP"""
    
    print("🌐 TESTE DE FLUXO WEB COMPLETO - NEUROLEARN")
    print("=" * 50)
    
    # URL base do servidor
    base_url = "http://127.0.0.1:5000"
    
    # Criar sessão para manter cookies
    session = requests.Session()
    
    try:
        # 1. Testar se servidor está rodando
        print("\n1️⃣ Verificando se servidor está ativo...")
        response = session.get(base_url)
        if response.status_code != 200:
            print(f"❌ Servidor não está acessível (Status: {response.status_code})")
            return False
        print("✅ Servidor está rodando")
        
        # 2. Fazer login com aluno de teste
        print("\n2️⃣ Fazendo login com aluno de teste...")
        login_data = {
            'email': 'debug@aluno.com',
            'senha': '123456'
        }
        
        response = session.post(f"{base_url}/login", data=login_data)
        if response.status_code not in [200, 302]:  # 302 = redirect após login
            print(f"❌ Erro no login (Status: {response.status_code})")
            return False
        print("✅ Login realizado com sucesso")
        
        # 3. Tentar acessar dashboard (deve redirecionar para questionário)
        print("\n3️⃣ Testando redirecionamento para questionário...")
        response = session.get(f"{base_url}/dashboard-aluno", allow_redirects=False)
        
        if response.status_code == 302 and '/questionario-neurolearn' in response.headers.get('Location', ''):
            print("✅ Redirecionamento para questionário funcionando")
        else:
            print(f"⚠️ Comportamento inesperado: Status {response.status_code}")
            print(f"    Location: {response.headers.get('Location', 'Não especificado')}")
        
        # 4. Acessar página do questionário
        print("\n4️⃣ Acessando página do questionário...")
        response = session.get(f"{base_url}/questionario-neurolearn")
        if response.status_code != 200:
            print(f"❌ Erro ao acessar questionário (Status: {response.status_code})")
            return False
        print("✅ Página do questionário carregada")
        
        # 5. Simular envio do questionário via AJAX
        print("\n5️⃣ Simulando envio do questionário via AJAX...")
        
        # Criar respostas variadas (como um usuário real faria)
        respostas = {}
        for i in range(1, 68):  # 67 questões
            # Simular respostas variadas para parecer mais real
            import random
            if i <= 10:  # Bloco 1 - Percepção
                respostas[str(i)] = random.choice([2, 3, 4])
            elif i <= 20:  # Bloco 2 - Atenção
                respostas[str(i)] = random.choice([3, 4, 5])
            elif i <= 30:  # Bloco 3 - Comunicação
                respostas[str(i)] = random.choice([2, 3])
            elif i <= 40:  # Bloco 4 - Organização
                respostas[str(i)] = random.choice([3, 4])
            elif i <= 50:  # Bloco 5 - Aprendizagem
                respostas[str(i)] = random.choice([4, 5])
            elif i <= 60:  # Bloco 6 - Social
                respostas[str(i)] = random.choice([2, 3, 4])
            else:  # Bloco 7 - Criatividade
                respostas[str(i)] = random.choice([4, 5])
        
        # Enviar dados como JSON (como o JavaScript faz)
        questionario_data = {'respostas': respostas}
        headers = {'Content-Type': 'application/json'}
        
        response = session.post(
            f"{base_url}/salvar-questionario",
            data=json.dumps(questionario_data),
            headers=headers
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('sucesso'):
                print("✅ Questionário salvo com sucesso")
            else:
                print(f"❌ Erro ao salvar: {result.get('erro', 'Erro desconhecido')}")
                return False
        else:
            print(f"❌ Erro HTTP ao salvar questionário (Status: {response.status_code})")
            print(f"    Resposta: {response.text[:200]}...")
            return False
        
        # 6. Aguardar um pouco (como o modal de loading faria)
        print("\n6️⃣ Aguardando processamento (simulando modal de loading)...")
        import time
        time.sleep(2)
        
        # 7. Tentar acessar dashboard novamente
        print("\n7️⃣ Testando acesso ao dashboard após questionário...")
        response = session.get(f"{base_url}/dashboard-aluno")
        
        if response.status_code == 200 and 'dashboard' in response.text.lower():
            print("✅ Acesso ao dashboard liberado com sucesso!")
            print("    Aluno agora pode ver seu dashboard principal")
            return True
        elif response.status_code == 302:
            location = response.headers.get('Location', '')
            if 'questionario' in location:
                print("❌ PROBLEMA: Ainda está sendo redirecionado para questionário")
                print(f"    Location: {location}")
                return False
            else:
                print(f"⚠️ Redirecionamento inesperado: {location}")
                return False
        else:
            print(f"❌ Erro ao acessar dashboard (Status: {response.status_code})")
            print(f"    Conteúdo: {response.text[:200]}...")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao servidor")
        print("   Certifique-se de que o servidor está rodando em http://127.0.0.1:5000")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def verificar_estado_banco():
    """Verifica o estado final no banco de dados"""
    print("\n📊 VERIFICAÇÃO DO BANCO DE DADOS:")
    print("-" * 30)
    
    with app.app_context():
        # Buscar aluno de teste
        usuario = Usuario.query.filter_by(email='debug@aluno.com').first()
        if not usuario:
            print("❌ Usuário de teste não encontrado")
            return
        
        aluno = Aluno.query.filter_by(usuario_id=usuario.id).first()
        if not aluno:
            print("❌ Aluno de teste não encontrado")
            return
        
        print(f"👤 Aluno: {aluno.usuario.nome} (ID: {aluno.id})")
        print(f"📝 Questionário completo: {aluno.questionario_completo}")
        print(f"🧠 Perfil gerado: {aluno.perfil_gerado}")
        
        # Verificar respostas
        respostas = QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno.id).count()
        print(f"📋 Total de respostas: {respostas}/67")
        
        # Verificar perfil
        perfil = PerfilAprendizagem.query.filter_by(aluno_id=aluno.id).first()
        if perfil:
            print(f"🎯 Tipo de perfil: {perfil.tipo_perfil}")
            print(f"📅 Data de geração: {perfil.data_geracao}")
        else:
            print("❌ Perfil não encontrado no banco")

if __name__ == '__main__':
    # Executar teste completo
    sucesso = testar_fluxo_web_completo()
    
    # Verificar estado do banco
    verificar_estado_banco()
    
    print("\n" + "=" * 50)
    if sucesso:
        print("🎉 TESTE COMPLETO PASSOU!")
        print("   O problema foi CORRIGIDO com sucesso.")
        print("   ✅ Questionário → ✅ Geração de Perfil → ✅ Dashboard")
    else:
        print("❌ TESTE FALHOU!")
        print("   O problema ainda persiste.")
    
    print("\n💡 Para testar manualmente:")
    print("   1. Execute: python iniciar_servidor.py")
    print("   2. Acesse: http://127.0.0.1:5000/login")
    print("   3. Faça login com: debug@aluno.com / 123456")
    print("   4. Complete o questionário")
    print("   5. Verifique se o dashboard é acessível")

