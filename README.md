ClouDDy — QA Automation & Functional Testing

📌 1. Objetivo

Validar o comportamento funcional do aplicativo ClouDDy em ambiente Android utilizando testes caixa-preta com automação de Smoke Tests.

O foco da validação inclui:

* Instalação e inicialização da aplicação
* Segurança funcional básica
* Validação de entradas
* Estabilidade operacional
* Comportamento em cenário offline


🧰 2. Stack de Ferramentas

* Sistema Operacional: Linux (Ubuntu/Debian)
* Linguagem: Python 3.x
* Framework de testes: Pytest
* Android SDK
* ADB (Android Debug Bridge)
* Emulador Android (x86_64)
* Logcat (monitoramento de logs)


🎯 3. Estratégia de Teste

A abordagem combina:

* Testes funcionais do tipo caixa-preta
* Execução de Smoke Tests automatizados
* Análise baseada em risco
* Monitoramento de logs para identificação de falhas

Os cenários foram priorizados com base no impacto ao usuário final e na criticidade do sistema.


⚠️ 4. Análise de Risco

| Cenário             | Impacto                                                 | Nível de Risco |
| ------------------- | ------------------------------------------------------- | -------------- |
| Segurança de Pasta  | Possível acesso indevido a conteúdo do usuário          | Alto           |
| Validação de URL    | Entrada inválida pode gerar comportamento inconsistente | Médio          |
| Reprodução de Mídia | Possível crash durante execução                         | Crítico        |
| Tratamento Offline  | Aplicação pode travar sem conectividade                 | Alto           |



▶️ 5. Execução do Projeto


5.1 Instalar o APK no emulador

```bash
adb install clouddy.apk

5.2 Executar os testes automatizados

```bash
pytest tests/
```

📁 6. Estrutura do Projeto

```text
tests/
 ├── test_smoke.py
 ├── test_validation.py
 ├── test_offline.py
 └── test_core.py


📊 7. Resultados dos Testes


| ID   | Cenário                    | Resultado | Classificação |
| ---- | -------------------------- | --------- | ------------- |
| CT01 | Instalação e inicialização | Passou    | Sucesso       |
| CT02 | Segurança de pasta         | Falhou    | ERRO          |
| CT03 | Validação de URL           | Falhou    | DEFEITO       |
| CT04 | Reprodução de mídia        | Falhou    | FALHA         |
| CT05 | Tratamento offline         | Falhou    | FALHA         |

 📘 8. Classificação (ISTQB)


* **ERRO:** ação humana durante definição, design ou implementação do sistema
* **DEFEITO:** problema no software que pode gerar comportamento incorreto
* **FALHA:** comportamento incorreto observado durante a execução

📌 9. Observações Técnicas

* Execução realizada em emulador Android (x86_64)
* Logs analisados via Logcat
* Automação executada com Pytest
* Cenários baseados em análise de risco funcional

 🔗 10. Evidências
Repositório com automação e testes:
