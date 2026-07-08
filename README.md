# simulador-edge-cloud
# Mini-Simulador: Alocação de Tarefas em Edge-Cloud

Este projeto é um protótipo desenvolvido em Python para simular e automatizar a decisão de alocação de processos em uma infraestrutura distribuída. O sistema escolhe de forma inteligente onde executar cada tarefa, dividindo a carga entre servidores de Borda (Edge) e de Nuvem (Cloud).

## 🧠 Lógica do Simulador

O sistema toma decisões baseadas em duas variáveis principais de cada tarefa: **Demanda de CPU** e **Necessidade de Baixa Latência**.

A infraestrutura simulada possui:
- **2 Servidores de Borda (Edge):** Baixa latência (10ms), mas com capacidade de processamento limitada (50 unidades cada).
- **1 Servidor em Nuvem (Cloud):** Maior latência (100ms), mas com alta capacidade de processamento (1000 unidades).

**Regras de Alocação:**
1. Tarefas que exigem tempo de resposta rápido são enviadas prioritariamente para a Borda.
2. Tarefas de processamento geral (ou pesadas demais) vão direto para a Nuvem.
3. **Mecanismo de Transbordo:** Se os servidores de Borda atingirem sua capacidade máxima, as novas tarefas que exigem baixa latência são redirecionadas automaticamente para a Nuvem para evitar falhas no sistema, assumindo a penalidade de latência da rede.

## 🚀 Como executar o projeto

O código foi escrito em Python puro, sem a necessidade de bibliotecas externas. 

**Pré-requisitos:**
- Python 3.x instalado na máquina.

**Passo a passo:**
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
