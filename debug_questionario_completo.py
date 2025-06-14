import requests
import json

# Simular respostas completas do questionário
respostas = {}
for i in range(1, 68):  # 67 questões no total
    respostas[str(i)] = 3  # Resposta neutra (3) para todas as questões

# Dados para envio
data = {
    'respostas': respostas
}

# Configurar sessão com cookies de autenticação
session = requests.Session()

# Primeiro fazer login
login_data = {
    'email': 'debug@aluno.com',
    'senha': 'debug123'
}

print("Fazendo login...")
response = session.post('http://localhost:5000/login', data=login_data)
print(f"Login status: {response.status_code}")

if response.status_code == 200:
    print("Login realizado com sucesso")
    
    # Agora enviar o questionário
    print("Enviando questionário...")
    response = session.post(
        'http://localhost:5000/salvar-questionario',
        json=data,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Status da resposta: {response.status_code}")
    print(f"Conteúdo da resposta: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        if 'sucesso' in result:
            print("✅ Questionário salvo com sucesso!")
            
            # Testar redirecionamento para dashboard
            print("Testando acesso ao dashboard...")
            dashboard_response = session.get('http://localhost:5000/dashboard-aluno')
            print(f"Dashboard status: {dashboard_response.status_code}")
            
            if dashboard_response.status_code == 200:
                print("✅ Dashboard acessível!")
            else:
                print(f"❌ Erro no dashboard: {dashboard_response.status_code}")
                print(f"Conteúdo: {dashboard_response.text[:500]}...")
        else:
            print(f"❌ Erro: {result}")
    else:
        print(f"❌ Erro HTTP: {response.status_code}")
        print(f"Resposta: {response.text}")
else:
    print(f"❌ Erro no login: {response.status_code}")
    print(f"Resposta: {response.text}")

