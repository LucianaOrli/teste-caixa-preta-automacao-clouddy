 Teste Funcional do tipo Caixa Preta - Automação de fumaça


🚀Projeto de Teste de Software - App ClouDDy
"Este projeto aplica a técnica de Caixa Preta através de uma suíte de Testes de Fumaça (Smoke Tests) automatizados, garantindo que as funcionalidades críticas do ClouDDy (Instalação e Boot) estejam estáveis antes de prosseguir para testes mais profundos."

 
Este projeto apresenta o relatório técnico e os scripts de teste do App ClouDDy.
🚀 Tecnologias e Ferramentas
* **S.O.:** Linux (Ubuntu/Debian)
* **Linguagem:** Python 3.x
* **Framework:** Pytest / Playwright
* **Ambiente:** Android SDK / ADB / Emulador x86_64

🚀 Execução do Projeto

Para reproduzir os testes e a automação de fumaça em ambiente Linux:

1. Instale o APK via terminal: `adb install clouddy.apk`
2. Execute a suite de testes: `pytest tests/`
   

📊 Relatório de Testes (Matriz de Resultados)

| ID | Cenário | Resultado | Classificação | Justificativa |
| :--- | :--- | :--- | :--- | :--- |
| **CT01** | Instalação e Boot | Passou | Caminho Feliz | Sucesso na instalação via ADB no Linux. |
| **CT02** | Segurança de Pasta | Falhou | **ERRO** | Erro humano: Omissão de senha no design. |
| **CT03** | Validação de URL | Falhou | **DEFEITO** | Bug no código: Aceita links malformados. |
| **CT04** | Estresse Vídeo 4K | Falhou | **FALHA** | O sistema encerra (Crash) durante o uso. |
| **CT05** | Tratamento Offline | Falhou | **FALHA** | O sistema trava (ANR) sem dar retorno. |


🧠 Glossário ISTQB Aplicado
* **ERRO:** Omissão de requisitos de segurança (CT02).
* **DEFEITO:** Lógica de validação de URL incorreta no código (CT03).
* **FALHA:** Crash do sistema em 4K e travamento offline (CT04 e CT05).


🚀 Tecnologias e Ferramentas
* **S.O.:** Linux (Ubuntu/Debian)
* **Linguagem:** Python 3.x
* **Framework:** Pytest / Playwright
* **Ambiente:** Android SDK / ADB / Emulador x86_64

