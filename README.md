 📱 Relatório Técnico de Engenharia de QA e Governança Mobile
> **Status do Projeto:** Homologação Parcial Controlada (Não recomendado para produção)  
> **Link Oficial do Repositório:** `https://github.com/LucianaOrli/teste-caixa-preta-automacao-clouddy`



 🏛️ Governança e Ambiente Técnico

 Informações de Emissão
| Atributo de Governança | Detalhe Técnico |
| :--- | :--- |
| **Responsável Técnica** | Luciana |
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
