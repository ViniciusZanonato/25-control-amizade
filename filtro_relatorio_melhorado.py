#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtro MELHORADO para relatórios de neurodivergência
Equipe Control + Amizade - CodeRace 2025
"""

import json
import sqlite3
from datetime import datetime
from typing import Dict, Any, List
from filtro_relatorio_neurodivergencia import FiltroRelatorioNeurodivergencia

class FiltroRelatorioMelhorado(FiltroRelatorioNeurodivergencia):
    """Versão melhorada do filtro com acesso ao banco de dados"""
    
    def __init__(self, db_path="sistema_educacional.db"):
        super().__init__()
        self.db_path = db_path
    
    def buscar_perfis_db(self) -> List[Dict[str, Any]]:
        """Busca todos os perfis no banco de dados"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = """
            SELECT 
                u.nome as nome_aluno,
                a.serie_ano,
                p.perfil_geral,
                p.potenciais_expressivos,
                p.potenciais_cognitivos,
                p.indicios_neurodivergencias,
                p.recomendacoes_professores,
                p.reforco_motivacional,
                p.tipo_perfil,
                p.data_geracao
            FROM perfil_aprendizagem p
            JOIN aluno a ON p.aluno_id = a.id
            JOIN usuario u ON a.usuario_id = u.id
            ORDER BY p.data_geracao DESC
            """
            
            cursor.execute(query)
            perfis = [dict(row) for row in cursor.fetchall()]
            conn.close()
            
            return perfis
            
        except Exception as e:
            print(f"Erro ao buscar perfis: {e}")
            return []
    
    def gerar_relatorio_completo_sistema(self) -> str:
        """Gera relatório completo de todos os perfis do sistema"""
        perfis = self.buscar_perfis_db()
        
        if not perfis:
            return "\n❌ Nenhum perfil encontrado no banco de dados.\n"
        
        relatorio = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    RELATÓRIO COMPLETO DO SISTEMA NEUROLEARN                 ║
║                          Equipe Control + Amizade                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

📊 ESTATÍSTICAS GERAIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Data do Relatório: {datetime.now().strftime('%d/%m/%Y às %H:%M')}
🎓 Total de Perfis: {len(perfis)}

📈 DISTRIBUIÇÃO POR TIPOS DE PERFIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        # Contar tipos de perfil
        tipos_count = {}
        for perfil in perfis:
            tipo = perfil.get('tipo_perfil', 'Não definido')
            tipos_count[tipo] = tipos_count.get(tipo, 0) + 1
        
        for tipo, count in sorted(tipos_count.items()):
            relatorio += f"• {self._obter_tipo_perfil_formatado(tipo)}: {count} aluno(s)\n"
        
        relatorio += "\n🎯 PERFIS INDIVIDUAIS\n"
        relatorio += "━" * 78 + "\n\n"
        
        # Adicionar cada perfil
        for i, perfil in enumerate(perfis, 1):
            relatorio += f"👤 ALUNO {i}: {perfil['nome_aluno']}\n"
            relatorio += f"📚 Série: {perfil['serie_ano']}\n"
            relatorio += f"🏷️  Tipo: {self._obter_tipo_perfil_formatado(perfil.get('tipo_perfil', ''))}\n"
            relatorio += f"📅 Gerado em: {perfil['data_geracao']}\n\n"
            
            # Perfil formatado
            perfil_dados = {
                'perfil_geral': perfil.get('perfil_geral', ''),
                'potenciais_expressivos': perfil.get('potenciais_expressivos', ''),
                'potenciais_cognitivos': perfil.get('potenciais_cognitivos', ''),
                'indicios_neurodivergencias': perfil.get('indicios_neurodivergencias', ''),
                'recomendacoes_professores': perfil.get('recomendacoes_professores', ''),
                'reforco_motivacional': perfil.get('reforco_motivacional', ''),
                'tipo_perfil': perfil.get('tipo_perfil', '')
            }
            
            relatorio_individual = self.formatar_relatorio_detalhado(
                perfil_dados, 
                perfil['nome_aluno'], 
                perfil['serie_ano']
            )
            
            relatorio += relatorio_individual + "\n"
            relatorio += "─" * 78 + "\n\n"
        
        relatorio += f"""
🎯 RESUMO EXECUTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Sistema com {len(perfis)} perfis de aprendizagem analisados
• Distribuição equilibrada entre diferentes tipos de perfil
• Recomendações personalizadas para cada aluno
• Base para estratégias pedagógicas individualizadas

───────────────────────────────────────────────────────────────────────────────
Gerado pelo Sistema NeuroLearn - Equipe Control + Amizade
📧 Suporte: control.amizade@neurolearn.com
───────────────────────────────────────────────────────────────────────────────
"""
        
        return relatorio
    
    def exportar_json_melhorado(self, arquivo_saida="perfis_exportados.json"):
        """Exporta todos os perfis em formato JSON melhorado"""
        perfis = self.buscar_perfis_db()
        
        dados_exportacao = {
            "metadata": {
                "sistema": "NeuroLearn v2.0",
                "equipe": "Control + Amizade",
                "data_exportacao": datetime.now().isoformat(),
                "total_perfis": len(perfis)
            },
            "perfis": []
        }
        
        for perfil in perfis:
            # Aplicar filtro para cada perfil
            perfil_json = {
                'perfil_geral': perfil.get('perfil_geral', ''),
                'potenciais_expressivos': perfil.get('potenciais_expressivos', ''),
                'potenciais_cognitivos': perfil.get('potenciais_cognitivos', ''),
                'indicios_neurodivergencias': perfil.get('indicios_neurodivergencias', ''),
                'recomendacoes_professores': perfil.get('recomendacoes_professores', ''),
                'reforco_motivacional': perfil.get('reforco_motivacional', ''),
                'tipo_perfil': perfil.get('tipo_perfil', '')
            }
            
            perfil_resumido = self.gerar_relatorio_resumido(perfil_json)
            
            dados_exportacao["perfis"].append({
                "aluno": {
                    "nome": perfil['nome_aluno'],
                    "serie": perfil['serie_ano'],
                    "data_geracao": perfil['data_geracao']
                },
                "perfil_completo": perfil_json,
                "perfil_resumido": perfil_resumido,
                "relatorio_formatado": self.formatar_relatorio_detalhado(
                    perfil_json, perfil['nome_aluno'], perfil['serie_ano']
                )
            })
        
        try:
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                json.dump(dados_exportacao, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Dados exportados para: {arquivo_saida}")
            return arquivo_saida
            
        except Exception as e:
            print(f"❌ Erro ao exportar: {e}")
            return None

def main():
    print("🔍 FILTRO MELHORADO DE RELATÓRIOS DE NEURODIVERGÊNCIA")
    print("" + "=" * 60)
    
    filtro = FiltroRelatorioMelhorado()
    
    # Gerar relatório completo
    print("\n📊 Gerando relatório completo do sistema...")
    relatorio_completo = filtro.gerar_relatorio_completo_sistema()
    
    # Salvar relatório
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"relatorio_sistema_completo_{timestamp}.txt"
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(relatorio_completo)
        print(f"✅ Relatório salvo: {nome_arquivo}")
    except Exception as e:
        print(f"❌ Erro ao salvar relatório: {e}")
    
    # Exportar JSON
    print("\n📄 Exportando dados em JSON...")
    arquivo_json = filtro.exportar_json_melhorado(f"perfis_sistema_{timestamp}.json")
    
    if arquivo_json:
        print(f"✅ JSON exportado: {arquivo_json}")
    
    print("\n🎯 Processamento concluído!")

if __name__ == "__main__":
    main()

