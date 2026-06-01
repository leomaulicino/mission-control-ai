"""
FIAP - Global Solution 2026.1
Componente: Pensamento Computacional e Automacao com Python
Projeto: Mission Control AI - Sistema Inteligente de Monitoramento Espacial

Missao: Russi Space
Satelite experimental de monitoramento atmosferico em orbita baixa.
Narrativa dos ciclos:
  Ciclo 1 - Lancamento e estabilizacao inicial
  Ciclo 2 - Aquecimento progressivo dos sistemas
  Ciclo 3 - Alerta termico inicial detectado
  Ciclo 4 - Degradacao de energia e comunicacao
  Ciclo 5 - Pico de criticidade: colapso de bateria e temperatura
  Ciclo 6 - Inicio de recuperacao, sistemas ainda comprometidos
  Ciclo 7 - Temperatura normalizada, energia em recomposicao
  Ciclo 8 - Estabilizacao progressiva, operacao restaurada
"""

# -------------------------------------------------
# 1. Identificacao da Missao e Equipe
# -------------------------------------------------
NOME_MISSAO = "Russi"
NOME_EQUIPE = "Fiapers"

# -------------------------------------------------
# 2. Areas Monitoradas (correlacionadas as colunas da matriz)
# -------------------------------------------------
AREAS_MONITORADAS = [
    "Temperatura interna",      # Coluna 0
    "Comunicacao com a base",   # Coluna 1
    "Sistema de energia",       # Coluna 2
    "Suporte de oxigenio",      # Coluna 3
    "Estabilidade operacional"  # Coluna 4
]

# -------------------------------------------------
# 3. Matriz Principal de Dados Simulados
# Missao Russi Space - satelite experimental de monitoramento atmosferico
# Cada linha representa um ciclo [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# -------------------------------------------------
dados_missao = [
    [22, 95, 91, 97, 93],  # Ciclo 1: Lancamento e estabilizacao inicial
    [29, 88, 84, 95, 88],  # Ciclo 2: Aquecimento progressivo dos sistemas
    [33, 76, 61, 93, 74],  # Ciclo 3: Alerta termico inicial detectado
    [38, 48, 43, 90, 62],  # Ciclo 4: Degradacao de energia e comunicacao
    [41, 22, 17, 83, 41],  # Ciclo 5: Pico de criticidade - colapso de bateria e temperatura
    [37, 35, 26, 86, 53],  # Ciclo 6: Inicio de recuperacao, sistemas ainda comprometidos
    [30, 61, 47, 91, 71],  # Ciclo 7: Temperatura normalizada, energia em recomposicao
    [25, 83, 68, 94, 86],  # Ciclo 8: Estabilizacao progressiva, operacao restaurada
]


# -------------------------------------------------
# FUNCOES DE ANALISE DE PARAMETROS INDIVIDUAIS
# -------------------------------------------------

def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (classificacao, pontos, detalhe).

    Regras:
        < 18 C         -> ATENCAO (1 pt)  - temperatura anormalmente baixa
        18 C a 30 C    -> NORMAL  (0 pt)
        30 C a 35 C    -> ATENCAO (1 pt)  - temperatura elevada
        > 35 C         -> CRITICO (2 pts) - risco de superaquecimento
    """
    if valor < 18:
        return "ATENCAO", 1, "Temperatura baixa"
    elif 18 <= valor <= 30:
        return "NORMAL", 0, "Temperatura estavel"
    elif 30 < valor <= 35:
        return "ATENCAO", 1, "Temperatura elevada"
    else:
        return "CRITICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    """Classifica a comunicacao e retorna (classificacao, pontos, detalhe).

    Regras:
        < 30%   -> CRITICO (2 pts)
        30%-59% -> ATENCAO (1 pt)
        >= 60%  -> NORMAL  (0 pt)
    """
    if valor < 30:
        return "CRITICO", 2, "Comunicacao com a base em nivel critico"
    elif 30 <= valor <= 59:
        return "ATENCAO", 1, "Comunicacao instavel"
    else:
        return "NORMAL", 0, "Comunicacao estavel"


def analisar_bateria(valor):
    """Classifica a bateria e retorna (classificacao, pontos, detalhe).

    Regras:
        < 20%   -> CRITICO (2 pts)
        20%-49% -> ATENCAO (1 pt)
        >= 50%  -> NORMAL  (0 pt)
    """
    if valor < 20:
        return "CRITICO", 2, "Bateria em nivel critico"
    elif 20 <= valor <= 49:
        return "ATENCAO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estavel"


def analisar_oxigenio(valor):
    """Classifica o oxigenio e retorna (classificacao, pontos, detalhe).

    Regras:
        < 80%   -> CRITICO (2 pts)
        80%-89% -> ATENCAO (1 pt)
        >= 90%  -> NORMAL  (0 pt)
    """
    if valor < 80:
        return "CRITICO", 2, "Oxigenio em nivel critico"
    elif 80 <= valor <= 89:
        return "ATENCAO", 1, "Oxigenio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigenio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (classificacao, pontos, detalhe).

    Regras:
        < 40%   -> CRITICO (2 pts)
        40%-69% -> ATENCAO (1 pt)
        >= 70%  -> NORMAL  (0 pt)
    """
    if valor < 40:
        return "CRITICO", 2, "Estabilidade operacional critica"
    elif 40 <= valor <= 69:
        return "ATENCAO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# -------------------------------------------------
# FUNCOES DE SINTESE E LOGICA DO SISTEMA
# -------------------------------------------------

def classificar_ciclo(pontos_ciclo):
    """Retorna a classificacao de criticidade do ciclo com base nos pontos.

    Faixas (secao 8 do enunciado):
        0-2  pts -> MISSAO ESTAVEL
        3-5  pts -> MISSAO EM ATENCAO
        6-10 pts -> MISSAO CRITICA
    """
    if 0 <= pontos_ciclo <= 2:
        return "MISSAO ESTAVEL"
    elif 3 <= pontos_ciclo <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def gerar_recomendacao(classif_ciclo, alertas_nao_normais):
    """Gera diretrizes de acao baseadas no estado do ciclo.

    Parametros:
        classif_ciclo       - classificacao do ciclo (string)
        alertas_nao_normais - lista de areas em ATENCAO ou CRITICO

    Logica:
        - Ciclo estavel sem alertas    -> mensagem de manutencao normal
        - MISSAO CRITICA com 4+ alertas -> mensagem consolidada de emergencia
        - Demais casos                 -> lista de acoes por area afetada
    """
    if classif_ciclo == "MISSAO ESTAVEL" and not alertas_nao_normais:
        return "Manter operacao normal e continuar monitoramento."

    if classif_ciclo == "MISSAO CRITICA" and len(alertas_nao_normais) >= 4:
        return ("Ativar modo de seguranca e priorizar suporte a vida, "
                "energia e comunicacao.")

    recomendacoes = []

    if "Temperatura" in alertas_nao_normais:
        recomendacoes.append("verificar controle termico da missao")
    if "Comunicacao" in alertas_nao_normais:
        recomendacoes.append("tentar restabelecer contato com a base")
    if "Bateria" in alertas_nao_normais:
        recomendacoes.append("ativar modo de economia de energia")
    if "Oxigenio" in alertas_nao_normais:
        recomendacoes.append("acionar protocolo de suporte a vida")
    if "Estabilidade" in alertas_nao_normais:
        recomendacoes.append("reduzir operacoes nao essenciais")

    if recomendacoes:
        return "Acoes necessarias: " + "; ".join(recomendacoes) + "."

    return "Monitorar sistemas em atencao e preparar plano de contingencia."


def analisar_tendencia(pontos_primeiro, pontos_ultimo):
    """Compara o risco do primeiro e do ultimo ciclo para inferir tendencia.

    Conforme secao 9 do enunciado:
        ultimo > primeiro -> tendencia de piora
        ultimo < primeiro -> tendencia de melhora
        ultimo = primeiro -> missao estavel em relacao ao inicio
    """
    if pontos_ultimo > pontos_primeiro:
        return "A missao apresentou tendencia de piora."
    elif pontos_ultimo < pontos_primeiro:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(pontos_por_area):
    """Retorna o indice e a pontuacao da area com maior risco acumulado.

    Em caso de empate, retorna a area de menor indice (primeira encontrada).
    """
    maior_pontuacao = -1
    indice = 0
    for idx, pts in enumerate(pontos_por_area):
        if pts > maior_pontuacao:
            maior_pontuacao = pts
            indice = idx
    return indice, maior_pontuacao


def gerar_relatorio_final(contexto):
    """Renderiza o bloco de Relatorio Final da Missao no terminal.

    Parametro:
        contexto - dicionario com todos os indicadores calculados em
                   executar_sistema().
    """
    print("\n" + "=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}\n")
    print(f"Quantidade de ciclos analisados: {contexto['total_ciclos']}\n")
    print(f"Media de temperatura:   {contexto['med_temp']:.2f} C")
    print(f"Media de comunicacao:   {contexto['med_com']:.2f}%")
    print(f"Media de bateria:       {contexto['med_bat']:.2f}%")
    print(f"Media de oxigenio:      {contexto['med_oxi']:.2f}%")
    print(f"Media de estabilidade:  {contexto['med_est']:.2f}%\n")
    print(f"Ciclo mais critico:            Ciclo {contexto['ciclo_mais_critico_index']}")
    print(f"Maior pontuacao de risco:      {contexto['maior_risco']}")
    print(f"Risco medio da missao:         {contexto['risco_medio']:.2f}")
    print(f"Quantidade de ciclos criticos: {contexto['ciclos_criticos']}\n")
    print("Tendencia da missao:")
    print(f"  {contexto['tendencia']}\n")
    print("Pontuacao acumulada por area:")
    for area, pts in zip(AREAS_MONITORADAS, contexto['pontos_por_area']):
        print(f"  {area}: {pts} pontos")
    print(f"\nArea mais afetada:\n  {contexto['area_mais_afetada']}\n")
    print("Classificacao final da missao:")
    print(f"  {contexto['classificacao_final']}\n")
    print("Conclusao:")
    print(f"  {contexto['conclusao']}")
    print("=" * 60)


def executar_sistema():
    """Funcao central do Mission Control AI.

    Percorre todos os ciclos da matriz dados_missao, exibe o log detalhado
    de cada ciclo no terminal e ao final monta o dicionario de contexto
    para chamar gerar_relatorio_final().
    """
    total_ciclos = len(dados_missao)

    soma_temperatura  = 0
    soma_comunicacao  = 0
    soma_bateria      = 0
    soma_oxigenio     = 0
    soma_estabilidade = 0

    pontos_por_area          = [0, 0, 0, 0, 0]
    pontos_ciclos_historico  = []
    ciclos_criticos_contador = 0
    ciclo_mais_critico_index = 0
    maior_risco_encontrado   = -1

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {total_ciclos}")
    print("=" * 60)

    for i, ciclo_dados in enumerate(dados_missao):
        ciclo_num = i + 1
        t_val, c_val, b_val, o_val, e_val = ciclo_dados

        soma_temperatura  += t_val
        soma_comunicacao  += c_val
        soma_bateria      += b_val
        soma_oxigenio     += o_val
        soma_estabilidade += e_val

        t_class, t_pts, t_det = analisar_temperatura(t_val)
        c_class, c_pts, c_det = analisar_comunicacao(c_val)
        b_class, b_pts, b_det = analisar_bateria(b_val)
        o_class, o_pts, o_det = analisar_oxigenio(o_val)
        e_class, e_pts, e_det = analisar_estabilidade(e_val)

        pontos_por_area[0] += t_pts
        pontos_por_area[1] += c_pts
        pontos_por_area[2] += b_pts
        pontos_por_area[3] += o_pts
        pontos_por_area[4] += e_pts

        pontos_totais_ciclo = t_pts + c_pts + b_pts + o_pts + e_pts
        pontos_ciclos_historico.append(pontos_totais_ciclo)
        status_ciclo = classificar_ciclo(pontos_totais_ciclo)

        if status_ciclo == "MISSAO CRITICA":
            ciclos_criticos_contador += 1

        if pontos_totais_ciclo > maior_risco_encontrado:
            maior_risco_encontrado   = pontos_totais_ciclo
            ciclo_mais_critico_index = ciclo_num

        alertas_nao_normais = []
        if t_class != "NORMAL":
            alertas_nao_normais.append("Temperatura")
        if c_class != "NORMAL":
            alertas_nao_normais.append("Comunicacao")
        if b_class != "NORMAL":
            alertas_nao_normais.append("Bateria")
        if o_class != "NORMAL":
            alertas_nao_normais.append("Oxigenio")
        if e_class != "NORMAL":
            alertas_nao_normais.append("Estabilidade")

        recomendacao = gerar_recomendacao(status_ciclo, alertas_nao_normais)

        print(f"\nCICLO {ciclo_num}")
        print("-" * 60)
        print(f"Temperatura:  {t_val} C  | {t_class} | {t_det}")
        print(f"Comunicacao:  {c_val}%  | {c_class} | {c_det}")
        print(f"Bateria:      {b_val}%  | {b_class} | {b_det}")
        print(f"Oxigenio:     {o_val}%  | {o_class} | {o_det}")
        print(f"Estabilidade: {e_val}%  | {e_class} | {e_det}")
        print(f"Pontuacao de risco do ciclo: {pontos_totais_ciclo}")
        print(f"Classificacao do ciclo: {status_ciclo}")
        print(f"Recomendacao: {recomendacao}")

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

    if risco_medio_geral <= 2:
        classificacao_final = "MISSAO ESTAVEL"
        conclusao = (
            "A missao operou dentro de parametros aceitaveis em todos os ciclos. "
            "Sistemas estaveis e sem ocorrencias criticas relevantes."
        )
    elif risco_medio_geral <= 5:
        classificacao_final = "MISSAO EM ATENCAO"
        conclusao = (
            "A missao apresentou instabilidade relevante durante a operacao. "
            "Apesar da tendencia de recuperacao nos ultimos ciclos, a equipe deve "
            "manter o plano de contingencia ativo e monitorar os sistemas de perto."
        )
    else:
        classificacao_final = "MISSAO CRITICA"
        conclusao = (
            "A missao operou sob severa degradacao de sistemas criticos. "
            "Acionar protocolo de emergencia imediatamente e priorizar "
            "energia, comunicacao e suporte a vida."
        )

    contexto = {
        "total_ciclos":             total_ciclos,
        "med_temp":                 med_temp,
        "med_com":                  med_com,
        "med_bat":                  med_bat,
        "med_oxi":                  med_oxi,
        "med_est":                  med_est,
        "ciclo_mais_critico_index": ciclo_mais_critico_index,
        "maior_risco":              maior_risco_encontrado,
        "risco_medio":              risco_medio_geral,
        "ciclos_criticos":          ciclos_criticos_contador,
        "tendencia":                tendencia_string,
        "pontos_por_area":          pontos_por_area,
        "area_mais_afetada":        area_mais_afetada_string,
        "classificacao_final":      classificacao_final,
        "conclusao":                conclusao,
    }

    gerar_relatorio_final(contexto)


if __name__ == "__main__":
    executar_sistema()