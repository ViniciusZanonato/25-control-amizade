# NeuroLearn - Sistema de Identificação de Neurodivergência

## 👥 Equipe: Control + Amizade

### 🎯 Integrantes da Equipe

- **Carlos Vinicius Garcia Zanonato** - Programador e Apresentador
- **Nicoly De Souza Silva** - Design e Programação  
- **Diulha Bilhão** - Apresentação, Solução de problemas e geração de ideias
- **Bruna Rafaela Brinque dos Santos** - Análise e Documentação

---

## 📚 Tema / Área do Problema

**Tema:** Inteligência Artificial Aplicada à Educação  
**Área do Problema:** Educação

---

## 🎯 Problema a ser Resolvido

**Dificuldade de Pedagogos no ensino e reconhecimento de alunos com neurodivergência**

Professores e educadores enfrentam grandes desafios para:
- Identificar precocemente sinais de neurodivergência em estudantes
- Adaptar metodologias de ensino para diferentes perfis de aprendizagem
- Oferecer suporte adequado sem diagnósticos especializados
- Compreender as necessidades individuais de cada aluno

---

## 💡 Descrição da Solução Proposta

O **NeuroLearn** é um sistema inteligente que utiliza IA para auxiliar educadores na identificação e suporte a alunos com neurodivergência. Nossa solução oferece:

### 🧠 Funcionalidades Principais:

1. **Questionário NeuroLearn (67 questões)**
   - Avaliação baseada em 7 dimensões do desenvolvimento
   - Análise de padrões comportamentais e cognitivos
   - Detecção de indicadores de TDAH, TEA, Dislexia e Superdotação

2. **Análise por Inteligência Artificial**
   - Processamento através da API Google Gemini
   - Geração de perfis personalizados de aprendizagem
   - Identificação de potenciais e necessidades específicas

3. **Relatórios Detalhados e Filtrados**
   - Perfis completos de cada estudante
   - Recomendações pedagógicas personalizadas
   - Estratégias de reforço motivacional
   - Sugestões de adaptações curriculares

4. **Dashboard para Professores**
   - Visão consolidada de todos os alunos
   - Filtros por tipo de perfil
   - Acompanhamento do progresso individual
   - Ferramentas de apoio pedagógico

5. **Sistema de Proteção de Dados**
   - Alunos não acessam seus próprios perfis completos
   - Informações sensíveis restritas a educadores
   - Conformidade com LGPD

### 🎨 Diferenciais da Solução:

- **Baseado em Ontopsicologia**: Fundamentação científica sólida
- **Interface Intuitiva**: Design pensado para educadores
- **Processamento Inteligente**: IA especializada em análise educacional
- **Relatórios Visuais**: Informações claras e acionáveis
- **Suporte Personalizado**: Estratégias específicas para cada perfil

---

## 🛠️ Tecnologias Utilizadas

### **Linguagens de Programação:**
- **Python 3.6+** - Backend e processamento de dados
- **JavaScript (ES6+)** - Interatividade frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização e responsividade
- **SQL** - Consultas ao banco de dados

### **Frameworks e Bibliotecas:**
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **Jinja2** - Engine de templates
- **Werkzeug** - Utilitários web e segurança

### **Banco de Dados:**
- **SQLite** - Banco relacional leve e eficiente
- **Estrutura normalizada** - Otimizada para consultas educacionais

### **Inteligência Artificial:**
- **Google Gemini API** - Processamento de linguagem natural
- **Prompt Engineering** - Técnicas avançadas de IA conversacional
- **Análise Preditiva** - Identificação de padrões comportamentais

### **Segurança e Autenticação:**
- **Hash de senhas** - Proteção de credenciais
- **Sessões seguras** - Controle de acesso
- **Validação de dados** - Prevenção de ataques

### **Ferramentas de Desenvolvimento:**
- **Git** - Controle de versão
- **VS Code** - Ambiente de desenvolvimento
- **Postman** - Testes de API
- **SQLite Browser** - Administração do banco

---

## 🚀 Como Funciona o Sistema

### **1. Cadastro e Autenticação**
```
Professor/Aluno → Registro → Login → Dashboard Personalizado
```

### **2. Processo de Avaliação**
```
Aluno → Questionário (67 questões) → IA Analisa → Perfil Gerado
```

### **3. Análise e Relatórios**
```
Perfil → Filtros Aplicados → Relatório Detalhado → Recomendações
```

### **4. Acompanhamento Pedagógico**
```
Professor → Dashboard → Perfis dos Alunos → Estratégias Personalizadas
```

---

## 📊 Estrutura do Projeto

```
NeuroLearn/
├── 🐍 app.py                           # Aplicação principal Flask
├── 🔧 filtro_relatorio_neurodivergencia.py  # Sistema de filtros
├── ⚡ filtro_relatorio_melhorado.py    # Versão otimizada dos filtros
├── 🗃️ sistema_educacional.db          # Banco de dados SQLite
├── 🎨 templates/                       # Templates HTML
│   ├── 🏠 index.html                   # Página inicial
│   ├── 👨‍🏫 dashboard_professor.html     # Dashboard do professor
│   ├── 👨‍🎓 dashboard_aluno.html         # Dashboard do aluno
│   ├── ❓ questionario_neurolearn.html  # Questionário principal
│   ├── 📊 relatorio_detalhado.html     # Relatórios formatados
│   └── 📋 *.html                       # Outras páginas
├── 🔧 init_db.py                      # Inicialização do banco
├── 🔄 migrar_db.py                    # Migrações do banco
├── 🚀 iniciar_servidor.py             # Script de inicialização
├── 📦 requirements.txt                # Dependências Python
└── 📖 README.md                       # Esta documentação
```

---

## 🎯 Resultados e Impacto

### **Benefícios para Educadores:**
- ✅ Identificação precoce de neurodivergências
- ✅ Estratégias pedagógicas personalizadas
- ✅ Redução do tempo de avaliação manual
- ✅ Suporte baseado em evidências científicas

### **Benefícios para Estudantes:**
- ✅ Ensino adaptado ao perfil individual
- ✅ Maior engajamento e motivação
- ✅ Desenvolvimento de potenciais únicos
- ✅ Suporte adequado às necessidades específicas

### **Benefícios para Instituições:**
- ✅ Melhoria nos indicadores educacionais
- ✅ Redução da evasão escolar
- ✅ Otimização de recursos pedagógicos
- ✅ Compliance com legislação inclusiva

---

## 🔧 Instalação e Uso

### **Pré-requisitos:**
- Python 3.6 ou superior
- SQLite 3
- Conexão com internet (para IA)

### **Instalação:**

1. **Clone o repositório:**
```bash
git clone [repositorio-neurolearn]
cd CodeRace-2025
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados:**
```bash
python init_db.py
```

4. **Inicie o servidor:**
```bash
python iniciar_servidor.py
```

5. **Acesse o sistema:**
```
http://localhost:5000
```

---

## 📈 Funcionalidades Avançadas

### **Sistema de Filtros Inteligentes:**
- Análise de consistência de respostas
- Detecção de padrões contraditórios
- Geração de relatórios executivos
- Exportação em múltiplos formatos

### **Análise Preditiva:**
- Identificação de tendências de aprendizagem
- Predição de necessidades futuras
- Sugestões proativas de intervenção
- Acompanhamento longitudinal

### **Relatórios Personalizados:**
- Visualizações gráficas interativas
- Comparativos entre períodos
- Métricas de progresso individual
- Dashboards executivos

---


## 📜 Licença e Uso

Projeto desenvolvido para o **CodeRace 2025** pela equipe **Control + Amizade**.  
Todos os direitos reservados.

---

### 🎉 "Transformando a educação através da tecnologia e da compreensão humana" - Equipe Control + Amizade

