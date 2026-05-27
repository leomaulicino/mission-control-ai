"""
FIAP - Global Solution 2026.1
Componente: Pensamento Computacional e Automação com Python
Projeto: Mission Control AI - Sistema Inteligente de Monitoramento Espacial
"""

# 1. Informações de Identificação da Missão e Equipe
NOME_MISSAO = "Russi"
NOME_EQUIPE = "Fiapers"

# 2. Áreas Monitoradas Correlacionadas com as Colunas da Matriz
AREAS_MONITORADAS = [
    "Temperatura interna",      # Coluna 0
    "Comunicação com a base",   # Coluna 1
    "Sistema de energia",       # Coluna 2
    "Suporte de oxigênio",      # Coluna 3
    "Estabilidade operacional"  # Coluna 4
]

# 3. Matriz Principal de Dados Simulados (Mínimo de 6 Ciclos)
dados_missao = [
    [24, 92, 88, 96, 90],  # Ciclo 1: Estável / Operação Normal
    [27, 80, 72, 94, 85],  # Ciclo 2: Elevação sutil de temperatura
    [31, 65, 58, 91, 70],  # Ciclo 3: Alerta inicial térmico
    [36, 42, 38, 87, 55],  # Ciclo 4: Degradação sistêmica (Atenção/Crítico)
    [39, 28, 19, 78, 35],  # Ciclo 5: Pico de criticidade total
    [34, 55, 32, 82, 50]   # Ciclo 6: Tentativa parcial de recuperação
]


# --- FUNÇÕES DE ANÁLISE DE PARÂMETROS INDIVIDUAIS ---

def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (classificacao, pontos, detalhe)."""
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa"
    elif 18 <= valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif 30 < valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """Classifica a comunicação e retorna (classificacao, pontos, detalhe)."""
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif 30 <= valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    """Classifica a bateria e retorna (classificacao, pontos, detalhe)."""
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif 20 <= valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    """Classifica o oxigênio e retorna (classificacao, pontos, detalhe)."""
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif 80 <= valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (classificacao, pontos, detalhe)."""
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif 40 <= valor <= 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# --- FUNÇÕES DE SÍNTESE E LÓGICA DO SISTEMA ---

def classificar_ciclo(pontos_ciclo):
    """Retorna a classificação de criticidade do ciclo baseado nos pontos."""
    if 0 <= pontos_ciclo <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontos_ciclo <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(classif_ciclo, alertas_nao_normais):
    """
    Gera diretrizes de ação baseadas no estado do ciclo.
    Recebe alertas_nao_normais: lista de áreas em ATENÇÃO ou CRÍTICO.
    Recomendações são geradas para qualquer parâmetro fora do normal,
    conforme o comportamento esperado descrito no enunciado (seção 12).
    """
    if classif_ciclo == "MISSÃO ESTÁVEL" and not alertas_nao_normais:
        return "Manter operação normal e continuar monitoramento."

    recomendacoes = []

    if "Temperatura" in alertas_nao_normais:
        recomendacoes.append("verificar controle térmico da missão")
    if "Comunicação" in alertas_nao_normais:
        recomendacoes.append("tentar restabelecer contato com a base")
    if "Bateria" in alertas_nao_normais:
        recomendacoes.append("ativar modo de economia de energia")
    if "Oxigênio" in alertas_nao_normais:
        recomendacoes.append("acionar protocolo de suporte à vida")
    if "Estabilidade" in alertas_nao_normais:
        recomendacoes.append("reduzir operações não essenciais")

    if recomendacoes:
        return "Ações necessárias: " + "; ".join(recomendacoes) + "."

    return "Monitorar sistemas em atenção e preparar plano de contingência."


def analisar_tendencia(pontos_primeiro, pontos_ultimo):
    """Compara o risco do primeiro e do último ciclo para inferir tendência."""
    if pontos_ultimo > pontos_primeiro:
        return "A missão apresentou tendência de piora."
    elif pontos_ultimo < pontos_primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    """Retorna o índice e a pontuação da área com maior risco acumulado."""
    maior_pontuacao = -1
    indice = 0
    for idx, pts in enumerate(pontos_por_area):
        if pts > maior_pontuacao:
            maior_pontuacao = pts
            indice = idx
    return indice, maior_pontuacao


def gerar_relatorio_final(total_ciclos, med_temp, med_com, med_bat, med_oxi, med_est,
                          ciclo_mais_critico_index, maior_risco_encontrado,
                          risco_medio_geral, ciclos_criticos_contador,
                          tendencia_string, pontos_por_area,
                          area_mais_afetada_string, classificacao_final_missao,
                          conclusao_string):
    """Renderiza o bloco de Relatório Final da Missão no terminal."""
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}\n")
    print(f"Quantidade de ciclos analisados: {total_ciclos}\n")
    print(f"Média de temperatura: {med_temp:.2f} °C")
    print(f"Média de comunicação: {med_com:.2f}%")
    print(f"Média de bateria: {med_bat:.2f}%")
    print(f"Média de oxigênio: {med_oxi:.2f}%")
    print(f"Média de estabilidade: {med_est:.2f}%\n")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico_index}")
    print(f"Maior pontuação de risco: {maior_risco_encontrado}")
    print(f"Risco médio da missão: {risco_medio_geral:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos_contador}\n")
    print("Tendência da missão:")
    print(f" {tendencia_string}\n")
    print("Pontuação acumulada por área:")
    for area, pts in zip(AREAS_MONITORADAS, pontos_por_area):
        print(f" {area}: {pts} pontos")
    print(f"\nÁrea mais afetada:\n {area_mais_afetada_string}\n")
    print("Classificação final da missão:")
    print(f" {classificacao_final_missao}\n")
    print("Conclusão:")
    print(f" {conclusao_string}")


def executar_sistema():
    """
    Função central do Mission Control AI.
    Percorre todos os ciclos da matriz dados_missao, exibe o log de cada ciclo
    no terminal e ao final chama gerar_relatorio_final() com os dados acumulados.
    """
    total_ciclos = len(dados_missao)

    # Variáveis de acumulação para o Relatório Final
    soma_temperatura  = 0
    soma_comunicacao  = 0
    soma_bateria      = 0
    soma_oxigenio     = 0
    soma_estabilidade = 0

    pontos_por_area          = [0, 0, 0, 0, 0]  # Índices iguais às colunas da matriz
    pontos_ciclos_historico  = []
    ciclos_criticos_contador = 0
    ciclo_mais_critico_index = 0
    maior_risco_encontrado   = -1

    # Cabeçalho
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {total_ciclos}")
    print("=" * 60)

    # Processamento iterativo dos ciclos
    for i in range(total_ciclos):
        ciclo_num = i + 1
        t_val, c_val, b_val, o_val, e_val = dados_missao[i]

        # Acumulação de valores brutos para cálculo das médias
        soma_temperatura  += t_val
        soma_comunicacao  += c_val
        soma_bateria      += b_val
        soma_oxigenio     += o_val
        soma_estabilidade += e_val

        # Análise individual de cada parâmetro
        t_class, t_pts, t_det = analisar_temperatura(t_val)
        c_class, c_pts, c_det = analisar_comunicacao(c_val)
        b_class, b_pts, b_det = analisar_bateria(b_val)
        o_class, o_pts, o_det = analisar_oxigenio(o_val)
        e_class, e_pts, e_det = analisar_estabilidade(e_val)

        # Acumulação de pontos de risco por área
        pontos_por_area[0] += t_pts
        pontos_por_area[1] += c_pts
        pontos_por_area[2] += b_pts
        pontos_por_area[3] += o_pts
        pontos_por_area[4] += e_pts

        # Pontuação e classificação do ciclo
        pontos_totais_ciclo = t_pts + c_pts + b_pts + o_pts + e_pts
        pontos_ciclos_historico.append(pontos_totais_ciclo)
        status_ciclo = classificar_ciclo(pontos_totais_ciclo)

        if status_ciclo == "MISSÃO CRÍTICA":
            ciclos_criticos_contador += 1

        if pontos_totais_ciclo > maior_risco_encontrado:
            maior_risco_encontrado   = pontos_totais_ciclo
            ciclo_mais_critico_index = ciclo_num

        # CORREÇÃO: coleta áreas em ATENÇÃO ou CRÍTICO (não apenas CRÍTICO)
        # para que recomendações sejam geradas a partir do primeiro sinal de alerta,
        # alinhado ao comportamento do exemplo da seção 12 do enunciado.
        alertas_nao_normais = []
        if t_class != "NORMAL":
            alertas_nao_normais.append("Temperatura")
        if c_class != "NORMAL":
            alertas_nao_normais.append("Comunicação")
        if b_class != "NORMAL":
            alertas_nao_normais.append("Bateria")
        if o_class != "NORMAL":
            alertas_nao_normais.append("Oxigênio")
        if e_class != "NORMAL":
            alertas_nao_normais.append("Estabilidade")

        recomendacao = gerar_recomendacao(status_ciclo, alertas_nao_normais)

        # Exibição do log do ciclo
        print(f"\nCICLO {ciclo_num}")
        print("-" * 60)
        print(f"Temperatura: {t_val} °C | {t_class} | {t_det}")
        print(f"Comunicação: {c_val}% | {c_class} | {c_det}")
        print(f"Bateria: {b_val}% | {b_class} | {b_det}")
        print(f"Oxigênio: {o_val}% | {o_class} | {o_det}")
        print(f"Estabilidade: {e_val}% | {e_class} | {e_det}")
        print(f"Pontuação de risco do ciclo: {pontos_totais_ciclo}")
        print(f"Classificação do ciclo: {status_ciclo}")
        print(f"Recomendação: {recomendacao}")

    # Cálculo dos indicadores finais
    med_temp = soma_temperatura  / total_ciclos
    med_com  = soma_comunicacao  / total_ciclos
    med_bat  = soma_bateria      / total_ciclos
    med_oxi  = soma_oxigenio     / total_ciclos
    med_est  = soma_estabilidade / total_ciclos
    risco_medio_geral = sum(pontos_ciclos_historico) / total_ciclos

    indice_area, _ = identificar_area_mais_afetada(pontos_por_area)
    area_mais_afetada_string = AREAS_MONITORADAS[indice_area]

    tendencia_string = analisar_tendencia(
        pontos_ciclos_historico[0],
        pontos_ciclos_historico[-1]
    )

    # Classificação final baseada no risco médio geral
    # (mesmos limiares por ciclo aplicados à média — documentado no README)
    if risco_medio_geral <= 2:
        classificacao_final_missao = "MISSÃO ESTÁVEL"
        conclusao_string = "A missão operou dentro de parâmetros aceitáveis."
    elif risco_medio_geral <= 5:
        classificacao_final_missao = "MISSÃO EM ATENÇÃO"
        conclusao_string = (
            "A missão apresentou instabilidade relevante durante a operação. "
            "Apesar da tentativa de recuperação no último ciclo, ainda existem "
            "sistemas em atenção e a equipe deve manter o plano de contingência ativo."
        )
    else:
        classificacao_final_missao = "MISSÃO CRÍTICA"
        conclusao_string = (
            "A missão operou sob severa degradação de sistemas críticos de sobrevivência. "
            "Acionar protocolo de emergência imediatamente."
        )

    gerar_relatorio_final(
        total_ciclos, med_temp, med_com, med_bat, med_oxi, med_est,
        ciclo_mais_critico_index, maior_risco_encontrado,
        risco_medio_geral, ciclos_criticos_contador,
        tendencia_string, pontos_por_area,
        area_mais_afetada_string, classificacao_final_missao,
        conclusao_string
    )


if __name__ == "__main__":
    executar_sistema()