# mission-control-ai

Sistema inteligente de monitoramento de missão espacial desenvolvido para a Global Solution 2026.1 da FIAP.

---

## Descrição do Projeto

O **Mission Control AI** simula o monitoramento automatizado de uma missão espacial experimental. O sistema analisa ciclos de monitoramento com dados de temperatura, comunicação, bateria, oxigênio e estabilidade operacional, gerando alertas automáticos, calculando níveis de risco e produzindo um relatório final completo da missão.

---

## Identificação

| Campo | Informação |
|---|---|
| Nome da Missão | Russi |
| Nome da Equipe | Fiapers |

---

## Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
python mission_control.py
```

Nenhuma biblioteca externa é necessária. O sistema utiliza apenas recursos nativos do Python.

---

## Estrutura dos Dados

O sistema é baseado na matriz `dados_missao`, uma lista de listas onde cada linha representa um ciclo de monitoramento e cada coluna representa um parâmetro monitorado.

```python
dados_missao = [
    [temperatura, comunicacao, bateria, oxigenio, estabilidade],
    ...
]
```

| Posição | Parâmetro | Unidade |
|---|---|---|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (Bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

### Ciclos Simulados

| Ciclo | Temp | Comunic. | Bateria | Oxigênio | Estabilidade | Descrição |
|---|---|---|---|---|---|---|
| 1 | 24°C | 92% | 88% | 96% | 90% | Operação normal |
| 2 | 27°C | 80% | 72% | 94% | 85% | Elevação sutil de temperatura |
| 3 | 31°C | 65% | 58% | 91% | 70% | Alerta inicial térmico |
| 4 | 36°C | 42% | 38% | 87% | 55% | Degradação sistêmica |
| 5 | 39°C | 28% | 19% | 78% | 35% | Pico de criticidade total |
| 6 | 34°C | 55% | 32% | 82% | 50% | Tentativa parcial de recuperação |

---

## Regras de Alerta

### Temperatura (°C)
| Condição | Classificação |
|---|---|
| menor que 18°C | ATENÇÃO |
| de 18°C até 30°C | NORMAL |
| maior que 30°C até 35°C | ATENÇÃO |
| maior que 35°C | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|---|---|
| menor que 30% | CRÍTICO |
| de 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|---|---|
| menor que 20% | CRÍTICO |
| de 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|---|---|
| menor que 80% | CRÍTICO |
| de 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|---|---|
| menor que 40% | CRÍTICO |
| de 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação de Risco

Cada classificação gera uma pontuação por parâmetro:

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

A pontuação máxima por ciclo é **10 pontos** (5 parâmetros × 2 pontos).

---

## Classificação dos Ciclos

| Pontuação Total | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## Classificação Final da Missão

A classificação final é calculada com base no **risco médio geral** da missão (média das pontuações de todos os ciclos). Os mesmos limiares de ciclo são aplicados sobre esse valor médio:

| Risco Médio | Classificação Final |
|---|---|
| 0 a 2 | MISSÃO ESTÁVEL |
| maior que 2 até 5 | MISSÃO EM ATENÇÃO |
| maior que 5 | MISSÃO CRÍTICA |

---

## Análise de Tendência

O sistema compara a pontuação de risco do **primeiro ciclo** com a do **último ciclo**:

| Condição | Tendência |
|---|---|
| Último > Primeiro | Tendência de piora |
| Último < Primeiro | Tendência de melhora |
| Último = Primeiro | Missão permaneceu estável |

---

## Funções do Sistema

| Função | Descrição |
|---|---|
| `analisar_temperatura(valor)` | Classifica a temperatura e retorna status, pontos e detalhe |
| `analisar_comunicacao(valor)` | Classifica a comunicação e retorna status, pontos e detalhe |
| `analisar_bateria(valor)` | Classifica a bateria e retorna status, pontos e detalhe |
| `analisar_oxigenio(valor)` | Classifica o oxigênio e retorna status, pontos e detalhe |
| `analisar_estabilidade(valor)` | Classifica a estabilidade e retorna status, pontos e detalhe |
| `classificar_ciclo(pontos)` | Retorna a classificação do ciclo com base na pontuação total |
| `gerar_recomendacao(classif, criticos)` | Gera recomendações automáticas baseadas no estado do ciclo |
| `analisar_tendencia(primeiro, ultimo)` | Compara o risco do primeiro e último ciclo |
| `identificar_area_mais_afetada(pontos)` | Identifica a área com maior pontuação de risco acumulada |
| `executar_sistema()` | Função central que processa todos os ciclos e gera o relatório final |

---

## Recomendações Automáticas

O sistema gera recomendações específicas por área crítica detectada:

| Área Crítica | Recomendação |
|---|---|
| Temperatura | Verificar controle térmico da missão |
| Comunicação | Tentar restabelecer contato com a base |
| Bateria | Ativar modo de economia de energia |
| Oxigênio | Acionar protocolo de suporte à vida |
| Estabilidade | Reduzir operações não essenciais |

---

## Requisitos Atendidos

- [x] Nome da missão e da equipe
- [x] Matriz `dados_missao` com 6 ciclos e 5 parâmetros
- [x] Lista de áreas monitoradas
- [x] Mínimo de 5 funções (10 funções implementadas)
- [x] Estrutura de repetição para percorrer os ciclos
- [x] Estruturas condicionais para gerar alertas
- [x] Cálculo de risco por ciclo
- [x] Classificação de cada ciclo
- [x] Análise de tendência da missão
- [x] Identificação da área mais afetada
- [x] Relatório final exibido no terminal
- [x] Recomendações automáticas por área crítica