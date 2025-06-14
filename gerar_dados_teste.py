import random
import sys
import os
from datetime import datetime, timedelta

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Usuario, Aluno, Professor, QuestionarioNeuroLearn, PerfilAprendizagem
from werkzeug.security import generate_password_hash
import json

def gerar_dados_teste():
    """Gera dados de teste: 1 professor e 10 alunos com questionários respondidos"""
    
    with app.app_context():
        print("🚀 Iniciando geração de dados de teste...")
        
        # 1. CRIAR PROFESSOR
        print("\n👨‍🏫 Criando professor...")
        
        # Verificar se já existe um professor
        professor_existente = Usuario.query.filter_by(email='professor@teste.com').first()
        if professor_existente:
            print("❌ Professor já existe! Removendo dados antigos...")
            # Remover dados relacionados
            professor_perfil = Professor.query.filter_by(usuario_id=professor_existente.id).first()
            if professor_perfil:
                db.session.delete(professor_perfil)
            db.session.delete(professor_existente)
            db.session.commit()
        
        # Criar novo professor
        usuario_professor = Usuario(
            nome='Prof. Maria Silva',
            email='professor@teste.com',
            senha_hash=generate_password_hash('123456'),
            tipo='professor'
        )
        db.session.add(usuario_professor)
        db.session.commit()
        
        professor = Professor(
            usuario_id=usuario_professor.id,
            disciplina='Múltiplas Disciplinas',
            formacao='Pedagogia com especialização em Neuroeducação'
        )
        db.session.add(professor)
        db.session.commit()
        
        print(f"✅ Professor criado: {usuario_professor.email} / senha: 123456")
        
        # 2. CRIAR 10 ALUNOS
        print("\n👥 Criando 10 alunos...")
        
        nomes_alunos = [
            'Ana Clara Santos',
            'Bruno Oliveira',
            'Carla Mendes',
            'Diego Silva',
            'Eduarda Costa',
            'Felipe Rodrigues',
            'Gabriela Lima',
            'Henrique Alves',
            'Isabella Ferreira',
            'João Pedro Martins'
        ]
        
        series = ['6º Ano', '7º Ano', '8º Ano', '9º Ano']
        idades = [11, 12, 13, 14, 15]
        
        for i, nome in enumerate(nomes_alunos, 1):
            # Limpar dados existentes se houver
            email = f'aluno{i}@teste.com'
            usuario_existente = Usuario.query.filter_by(email=email).first()
            if usuario_existente:
                aluno_perfil = Aluno.query.filter_by(usuario_id=usuario_existente.id).first()
                if aluno_perfil:
                    # Remover dados relacionados
                    QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno_perfil.id).delete()
                    PerfilAprendizagem.query.filter_by(aluno_id=aluno_perfil.id).delete()
                    db.session.delete(aluno_perfil)
                db.session.delete(usuario_existente)
                db.session.commit()
            
            # Criar usuário
            usuario_aluno = Usuario(
                nome=nome,
                email=email,
                senha_hash=generate_password_hash('123456'),
                tipo='aluno'
            )
            db.session.add(usuario_aluno)
            db.session.commit()
            
            # Criar perfil do aluno
            aluno = Aluno(
                usuario_id=usuario_aluno.id,
                email_escola=f'{nome.lower().replace(" ", ".").replace("ã", "a").replace("ç", "c")}@escola.edu.br',
                serie_ano=random.choice(series),
                professor_responsavel='Prof. Maria Silva',
                idade=random.choice(idades),
                questionario_completo=True,
                perfil_gerado=True
            )
            db.session.add(aluno)
            db.session.commit()
            
            # Gerar respostas do questionário (67 questões)
            print(f"  📝 Gerando questionário para {nome}...")
            gerar_respostas_questionario(aluno.id)
            
            # Gerar perfil de aprendizagem
            print(f"  🧠 Gerando perfil para {nome}...")
            gerar_perfil_teste(aluno.id, nome)
            
            print(f"✅ Aluno {i}: {email} / senha: 123456")
        
        print("\n🎉 Dados de teste gerados com sucesso!")
        print("\n📋 RESUMO:")
        print(f"👨‍🏫 Professor: professor@teste.com / 123456")
        print(f"👥 Alunos: aluno1@teste.com até aluno10@teste.com / 123456")
        print("\n🌐 Acesse: http://127.0.0.1:5000")

def gerar_respostas_questionario(aluno_id):
    """Gera respostas realistas para o questionário de 67 questões"""
    
    # Definir perfis base para variar as respostas
    perfis_base = [
        {'nome': 'Criativo', 'tendencias': {1: 2, 2: 3, 3: 4, 4: 2, 5: 4, 6: 3, 7: 5}},
        {'nome': 'Organizado', 'tendencias': {1: 3, 2: 4, 3: 3, 4: 5, 5: 4, 6: 3, 7: 3}},
        {'nome': 'Social', 'tendencias': {1: 3, 2: 3, 3: 4, 4: 3, 5: 3, 6: 5, 7: 4}},
        {'nome': 'Sensorial', 'tendencias': {1: 5, 2: 2, 3: 3, 4: 3, 5: 4, 6: 2, 7: 3}},
        {'nome': 'Equilibrado', 'tendencias': {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3}}
    ]
    
    perfil_escolhido = random.choice(perfis_base)
    tendencias = perfil_escolhido['tendencias']
    
    for questao_num in range(1, 68):  # 67 questões
        bloco = ((questao_num - 1) // 10) + 1
        
        # Usar tendência do bloco com variação
        tendencia_base = tendencias.get(bloco, 3)
        
        # Adicionar variação natural (-1 a +1)
        variacao = random.choice([-1, 0, 1])
        resposta = max(1, min(5, tendencia_base + variacao))
        
        # Adicionar algumas respostas mais extremas ocasionalmente
        if random.random() < 0.1:  # 10% de chance
            resposta = random.choice([1, 5])
        
        questionario = QuestionarioNeuroLearn(
            aluno_id=aluno_id,
            bloco=bloco,
            questao=questao_num,
            resposta=resposta
        )
        db.session.add(questionario)
    
    db.session.commit()

def gerar_perfil_teste(aluno_id, nome_aluno):
    """Gera um perfil de aprendizagem baseado nas respostas"""
    
    # Buscar respostas do aluno
    respostas = QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno_id).all()
    
    # Organizar por bloco
    respostas_por_bloco = {}
    for i in range(1, 8):
        respostas_por_bloco[i] = []
    
    for resposta in respostas:
        respostas_por_bloco[resposta.bloco].append(resposta.resposta)
    
    # Calcular médias
    medias = {}
    for bloco, valores in respostas_por_bloco.items():
        medias[bloco] = sum(valores) / len(valores) if valores else 3.0
    
    # Determinar características principais
    blocos_nomes = {
        1: 'Percepção Sensorial',
        2: 'Atenção e Foco',
        3: 'Comunicação',
        4: 'Organização',
        5: 'Aprendizagem',
        6: 'Interação Social',
        7: 'Criatividade'
    }
    
    pontos_fortes = [blocos_nomes[bloco] for bloco, media in medias.items() if media >= 4.0]
    desafios = [blocos_nomes[bloco] for bloco, media in medias.items() if media <= 2.0]
    
    # Definir tipo de perfil
    if medias[7] >= 4.0 and medias[5] >= 4.0:
        tipo_perfil = 'Pensador Criativo'
    elif medias[4] >= 4.0 and medias[2] >= 4.0:
        tipo_perfil = 'Organizador Metódico'
    elif medias[3] >= 4.0 and medias[6] >= 4.0:
        tipo_perfil = 'Comunicador Social'
    elif medias[1] >= 4.0:
        tipo_perfil = 'Observador Detalhista'
    else:
        tipo_perfil = 'Perfil Equilibrado'
    
    # Gerar textos baseados no perfil
    perfil_geral = f"""
    {nome_aluno} apresenta um perfil de aprendizagem {tipo_perfil.lower()}, demonstrando características únicas que favorecem seu desenvolvimento educacional. 
    Suas principais fortalezas estão nas áreas de {', '.join(pontos_fortes[:3]) if pontos_fortes else 'múltiplas competências'}, 
    indicando um potencial significativo para atividades que explorem essas habilidades.
    """.strip()
    
    potenciais_expressivos = f"""
    O aluno demonstra facilidade para se expressar através de modalidades que envolvem {', '.join(pontos_fortes[:2]) if len(pontos_fortes) >= 2 else 'diferentes formas de comunicação'}. 
    Recomenda-se oferecer oportunidades variadas de expressão, incluindo atividades práticas, criativas e colaborativas para maximizar seu potencial comunicativo.
    """.strip()
    
    potenciais_cognitivos = f"""
    As áreas de maior destaque cognitivo são {', '.join(pontos_fortes) if pontos_fortes else 'equilibradas entre diferentes domínios'}. 
    O aluno apresenta um perfil que favorece aprendizagens que integrem essas competências, beneficiando-se de abordagens pedagógicas diversificadas.
    """.strip()
    
    # Indicar características específicas baseadas nas médias
    indicios = []
    if medias[1] >= 4.5:
        indicios.append('Alta sensibilidade sensorial - requer ambiente controlado')
    if medias[2] <= 2.5:
        indicios.append('Dificuldades de atenção - pode se beneficiar de pausas frequentes')
    if medias[6] <= 2.5:
        indicios.append('Preferência por atividades individuais')
    if medias[4] >= 4.5:
        indicios.append('Excelentes habilidades organizacionais')
    
    if not indicios:
        indicios.append('Perfil neurotípico com características individuais de aprendizagem')
    
    indicios_neurodivergencias = '. '.join(indicios) + '.'
    
    recomendacoes = [
        f"Valorizar e desenvolver os pontos fortes em {', '.join(pontos_fortes[:2]) if len(pontos_fortes) >= 2 else 'áreas identificadas'}",
        "Oferecer atividades diversificadas que atendam diferentes estilos de aprendizagem",
        "Respeitar o ritmo individual e proporcionar feedback construtivo",
        "Promover autoconfiança através de desafios adequados ao nível de desenvolvimento",
        "Integrar tecnologias educacionais quando apropriado"
    ]
    
    if desafios:
        recomendacoes.append(f"Oferecer suporte adicional nas áreas de {', '.join(desafios[:2])}")
    
    recomendacoes_professores = '\n• ' + '\n• '.join(recomendacoes)
    
    reforco_motivacional = f"""
    Você tem talentos únicos e especiais, {nome_aluno}! Suas habilidades em {', '.join(pontos_fortes[:2]) if len(pontos_fortes) >= 2 else 'diferentes áreas'} 
    mostram o quanto você é capaz. Continue explorando, aprendendo e sempre acredite no seu potencial. 
    Cada conquista, por menor que seja, é um passo importante na sua jornada de aprendizagem!
    """.strip()
    
    # Salvar perfil
    perfil = PerfilAprendizagem(
        aluno_id=aluno_id,
        perfil_geral=perfil_geral,
        potenciais_expressivos=potenciais_expressivos,
        potenciais_cognitivos=potenciais_cognitivos,
        indicios_neurodivergencias=indicios_neurodivergencias,
        recomendacoes_professores=recomendacoes_professores,
        reforco_motivacional=reforco_motivacional,
        tipo_perfil=tipo_perfil
    )
    
    db.session.add(perfil)
    db.session.commit()

if __name__ == '__main__':
    try:
        gerar_dados_teste()
    except Exception as e:
        print(f"❌ Erro ao gerar dados: {e}")
        import traceback
        traceback.print_exc()

