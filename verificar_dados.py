import sys
import os

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Usuario, Aluno, Professor, QuestionarioNeuroLearn, PerfilAprendizagem

def verificar_dados():
    """Verifica se os dados de teste foram criados corretamente"""
    
    with app.app_context():
        print("🔍 Verificando dados gerados...\n")
        
        # Verificar professor
        professor = Usuario.query.filter_by(email='professor@teste.com').first()
        if professor:
            print(f"✅ Professor encontrado: {professor.nome} ({professor.email})")
            prof_perfil = Professor.query.filter_by(usuario_id=professor.id).first()
            if prof_perfil:
                print(f"   📚 Disciplina: {prof_perfil.disciplina}")
                print(f"   🎓 Formação: {prof_perfil.formacao}")
        else:
            print("❌ Professor não encontrado")
        
        print("\n" + "="*50)
        
        # Verificar alunos
        print("\n👥 ALUNOS GERADOS:")
        for i in range(1, 11):
            email = f'aluno{i}@teste.com'
            usuario = Usuario.query.filter_by(email=email).first()
            
            if usuario:
                aluno = Aluno.query.filter_by(usuario_id=usuario.id).first()
                if aluno:
                    # Verificar questionário
                    respostas = QuestionarioNeuroLearn.query.filter_by(aluno_id=aluno.id).count()
                    
                    # Verificar perfil
                    perfil = PerfilAprendizagem.query.filter_by(aluno_id=aluno.id).first()
                    
                    print(f"\n🧑‍🎓 {usuario.nome}")
                    print(f"   📧 Email: {usuario.email}")
                    print(f"   🏫 Série: {aluno.serie_ano}")
                    print(f"   🎂 Idade: {aluno.idade} anos")
                    print(f"   📝 Respostas do questionário: {respostas}/67")
                    print(f"   📋 Questionário completo: {'✅' if aluno.questionario_completo else '❌'}")
                    print(f"   🧠 Perfil gerado: {'✅' if aluno.perfil_gerado else '❌'}")
                    
                    if perfil:
                        print(f"   🎯 Tipo de perfil: {perfil.tipo_perfil}")
                    else:
                        print("   ❌ Perfil não encontrado")
                else:
                    print(f"❌ Perfil do aluno {i} não encontrado")
            else:
                print(f"❌ Usuário aluno{i} não encontrado")
        
        # Estatísticas gerais
        print("\n" + "="*50)
        print("\n📊 ESTATÍSTICAS GERAIS:")
        
        total_usuarios = Usuario.query.count()
        total_alunos = Aluno.query.count()
        total_professores = Professor.query.count()
        total_questionarios = QuestionarioNeuroLearn.query.count()
        total_perfis = PerfilAprendizagem.query.count()
        
        print(f"👤 Total de usuários: {total_usuarios}")
        print(f"🧑‍🎓 Total de alunos: {total_alunos}")
        print(f"👨‍🏫 Total de professores: {total_professores}")
        print(f"📝 Total de respostas: {total_questionarios}")
        print(f"🧠 Total de perfis: {total_perfis}")
        
        # Verificar distribuição de tipos de perfil
        print("\n🎯 DISTRIBUIÇÃO DE PERFIS:")
        perfis_tipos = db.session.query(PerfilAprendizagem.tipo_perfil, db.func.count(PerfilAprendizagem.id)).group_by(PerfilAprendizagem.tipo_perfil).all()
        
        for tipo, count in perfis_tipos:
            print(f"   {tipo}: {count} aluno(s)")
        
        print("\n🎉 Verificação concluída!")
        print("\n💡 INSTRUÇÕES DE TESTE:")
        print("1. Acesse: http://127.0.0.1:5000")
        print("2. Faça login como professor: professor@teste.com / 123456")
        print("3. Ou faça login como aluno: aluno1@teste.com até aluno10@teste.com / 123456")
        print("4. Explore os perfis de aprendizagem gerados!")

if __name__ == '__main__':
    try:
        verificar_dados()
    except Exception as e:
        print(f"❌ Erro ao verificar dados: {e}")
        import traceback
        traceback.print_exc()

