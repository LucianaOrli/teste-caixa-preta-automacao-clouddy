 🚀 Teste Funcional do tipo Caixa Preta - Automação de Fumaça
    **Projeto de Teste de Software - App ClouDDy**


Este projeto aplica a técnica de Caixa Preta através de uma suíte de Testes de Fumaça (Smoke Tests) automatizados, apresentando o relatório técnico e a validação da integridade lógica do aplicativo ClouDDy em ambiente mobile.


 🚀 Tecnologias e Ferramentas Utilizadas
* **S.O.:** Linux (Ubuntu/Debian)
* **Linguagem:** Python 3.x
* **Framework:** Pytest
* **Ambiente:** Android SDK / ADB (Android Debug Bridge) / Emulador x86_64


 🚀 Execução do Projeto

Para reproduzir os testes e a automação de fumaça em ambiente Linux:

1. Instale o APK via terminal: `adb install clouddy.apk`
2. Execute a suíte de testes: `pytest tests/`

 
 📊 Relatório de Testes (Matriz de Resultados)

| ID | Cenário | Resultado | Classificação | Justificativa |
| :--- | :--- | :--- | :--- | :--- |
| **CT01** | Instalação e Boot | Passou | Caminho Feliz | Sucesso na instalação via ADB no Linux. |
| **CT02** | Segurança de Pasta | Falhou | **ERRO** | Erro humano: Omissão de senha no design. |
| **CT03** | Validação de URL | Falhou | **DEFEITO** | Bug no código: Aceita links malformados. |
| **CT04** | Estresse Vídeo 4K | Falhou | **FALHA** | O sistema encerra (Crash) durante o uso. |
| **CT05** | Tratamento Offline | Falhou | **FALHA** | O sistema trava (ANR) sem dar retorno. |



🧠 Glossário ISTQB Aplicado
* **ERRO:** Omissão de requisitos de segurança (CT02). Uma ação humana incorreta na fase de design.
* **DEFEITO:** Lógica de validação de URL incorreta no código (CT03). O "bug" físico escrito no sistema.
* **FALHA:** Crash do sistema em 4K e travamento offline (CT04 e CT05). O comportamento incorreto visível durante a execução do app.
