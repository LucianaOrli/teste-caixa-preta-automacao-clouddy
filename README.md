**💎 RESUMO EXECUTIVO**

Este projeto consolida uma estratégia de Quality Engineering mobile orientada a **risco, governança e rastreabilidade, aplicada ao aplicativo ClouDDy em abordagem black-box executada em dispositivos Android físicos**.
**A suíte de automação utiliza Pytest, ADB e observabilidade via Logcat, cobrindo validações funcionais, stress testing, resiliência offline e análise de estabilidade sob condições reais de degradação operacional**.

**A avaliação segue princípios de classificação de criticidade, separação entre erro, defeito e falha, e governança de homologação, permitindo análise estruturada da confiabilidade do sistema em ambiente próximo à produção**.
Os resultados demonstram conformidade parcial em fluxos básicos, porém evidenciam falhas críticas de estabilidade, segurança lógica, validação de entradas e **gerenciamento de recursos, incluindo crashes (SIGSEGV) e estados de ANR sob carga e desconectividade**.
O sistema encontra-se em estado de homologação parcial controlada, não recomendado para produção até mitigação das não conformidades críticas identificadas.
Decisão técnica: sistema não atende critérios de produção devido a falhas críticas de estabilidade e resiliência. 

 
 📱 Relatório Técnico Governança de QA e Mobile
 **Status do Projeto:** Homologação Parcial Controlada (Não recomendado para produção)  

 Governança e Ambiente Técnico

 Informações de Emissão
| Atributo de Governança | Detalhe Técnico |
| :--- | :--- |

| **Projeto Avaliado** | ClouDDy (Abordagem Caixa-Preta) |
| **Data de Emissão** | 17 de Maio de 2026 |
| **Versão do Documento** | 1.0 — Governança Técnica Consolidada |



 Matriz de Infraestrutura
| Item | Detalhe | Item | Detalhe |
| :--- | :--- | :--- | :--- |
| **Plataforma** | Android | **Framework Principal** | Pytest |
| **Linguagem** | Python 3.x | **Comunicação Mobile** | Android Debug Bridge (ADB) |
| **Coleta de Logs** | Android Logcat | **Método Homologação** | Dispositivo Físico Real |
| **Aparelho Principal** | Motorola (ID: ZF5252JKFQ) | **Aparelho Secundário**| Nokia C21 Plus (Execução Limitada) |



 🎯 Escopo da Validação

```diff
+ COBERTO: Instalação/Inicialização, Validação Estrutural, Stress Testing (4K), Resiliência Offline, Observabilidade via Logcat.
- NÃO COBERTO: Pentest (Segurança Ofensiva), Engenharia Reversa, Testes Instrumentados (White-Box), Compatibilidade iOS.

# 📱 Relatório Técnico de Engenharia de QA e Governança Mobile
> **Status do Projeto:** Homologação Parcial Controlada (Não recomendado para produção)  
> **Link Oficial do Repositório:** `https://github.com/LucianaOrli/teste-caixa-preta-automacao-clouddy`



📊 Resultados Consolidados (Normativa ISTQB)
1. Definições de Estados
SUCESSO: Execução aderente aos critérios de aceitação.

ERRO: Interferência humana ou operacional externa ao software.

DEFEITO: Imperfeição lógica ou estrutural existente na aplicação.

FALHA: Manifestação visível de quebra operacional em tempo de execução.


ID,  Cenário de Teste, Criticidade, Resultado, Classificação ISTQB, Impacto Operacional
CT01, Instalação e Inicialização, Baixa, PASSOU, SUCESSO, Ambiente estável em uso inicial
CT02, Segurança de Pasta, Alta, FALHOU, DEFEITO,  Bypass de senha e exposição de dados
CT03, Validação de URL, Média, FALHOU, DEFEITO,  Inconsistência por payloads inválidos
CT04, Stress Multimídia 4K, Crítica, FALHOU,F ALHA, Crash abrupto do App (SIGSEGV)
CT05, Resiliência Offline, Alta, FALHOU, FALHA, Travamento de interface (Estado ANR)
CT05-A, Interferência Operacional,N /A, IDENTIFICADO, ERRO, Wi-Fi reativado antes do fim do script

⚠️ Nota de Governança sobre o CT05-A: O evento de rede foi classificado estritamente como ERRO (interferência humana externa) e isolado para não mascarar a real qualidade do software sob teste.

🛠️ Detalhamento Técnico das Ocorrências
Campo	Detalhamento Técnico das Ocorrências
✅ CT01	
Instalação e Inicialização


• Deploy via ADB e bootstrap concluídos sem inconsistências operacionais.

❌ CT02	
Segurança de Diretórios


• Severidade: ALTA


• Evidência: Quebra de confidencialidade no fluxo de pastas restritas.


• Recomendação: Aplicar validação obrigatória de autenticação e controle de sessão.

❌ CT03	
Validação de URL


• Severidade: MÉDIA


• Evidência: Aceite de entradas inválidas sem tratamento de erro.


• Recomendação: Implementar Regex de validação e sanitização defensiva de inputs.

❌ CT04	
Reprodução Multimídia 4K


• Severidade: CRÍTICA


• Evidência: Logcat registrou Fatal Exception por exaustão da Main Thread.


• Recomendação: Adicionar buffer adaptativo e fallback automático de resolução.

❌ CT05	
Resiliência Offline


• Severidade: ALTA


• Evidência: Queda abrupta de rede gerou congelamento completo (ANR).


• Recomendação: Desacoplar chamadas de rede da Main Thread e aplicar retry exponencial.


Exportar para as Planilhas

🧠 Avaliação Formal de Usabilidade (UX)
Classificação Final: PARCIALMENTE APROVADA

Pontos Positivos: Onboarding simples, baixa curva de aprendizado e navegação fluida em cenários ideais (caminho feliz).

Pontos Críticos: Ausência total de tratamento de falhas para o usuário, congelamento em modo offline e falta de feedback visual em transições em segundo plano.

Impacto no Negócio: Alto risco de rejeição e perda de retenção de usuários devido à percepção de instabilidade técnica do produto.

📐 Arquitetura do Projeto de Automação
│Bash
├── tests/
│   └── test_logic_integrity.py      # Script principal de asserções lógicas
│
├── evidence/
│   ├── screenshots/                 # Capturas de tela dos estados de rede
│   ├── logs/                        # Buffers extraídos do Logcat
│   └── reports/                     # Relatórios HTML gerados pelo Pytest
│
├── utils/
│   ├── adb_manager.py               # Orquestrador de comandos ADB
│   ├── logcat_monitor.py            # Capturador assíncrono de exceções
│   └── network_controller.py        # Simulador de perda de conectividade
│
├── requirements.txt                 # Dependências do ecossistema Python
└── README.md                        # Documentação técnica

Fluxo de Execução
Plaintext


Inicialização ➔ Deploy APK via ADB ➔ Execução Pytest ➔ Monitoramento Logcat ➔ Captura de Evidências ➔ Geração do Relatório HTML



 📸 Evidências de Execução 

A suíte de automação gerou os artefatos de homologação que estão publicados na raiz deste repositório:

* **Relatórios de Execução:** [report.html](./report.html) / [evidence.relatório.html](./evidence.relatório.html) *(Dashboards interativos com o status das asserções do Pytest).*
* ** Captura de Logs do Sistema:** [logcat.txt](./logcat.txt) *(Dump real do Android Logcat isolando o crash SIGSEGV do CT04 e o travamento ANR do CT05).*
* **Evidências Visuais (Hardware Físico):** [1.evidence.moto.png](./1.evidence.moto.png) e [2.evidence.moto.png](./2.evidence.moto.png) *(Prints reais capturados diretamente do dispositivo Motorola durante os estados de falha).*


**Conclusão Executiva Final**

O aplicativo ClouDDy demonstra maturidade funcional satisfatória para fluxos básicos e de instalação, mas não possui resiliência ou segurança lógica adequadas para publicação em ambiente de produção.

Recomenda-se o bloqueio do deploy produtivo até que as falhas críticas de Crash (CT04) e ANR (CT05) sejam devidamente mitigadas pela equipe de desenvolvimento.
