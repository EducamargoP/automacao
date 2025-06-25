💬 PASSO A PASSO – Criando um bot de perguntas e respostas no Telegram
Acesse o Telegram e procure pelo BotFather.

Crie um bot com ele e receba sua chave de API.

No PyCharm, instale a biblioteca com:

bash
pip install pytelegrambotapi
No código, crie uma variável para armazenar sua chave API.

Use bot.polling() para manter o bot sempre ativo (como um loop infinito).

Crie um decorador com @ e uma função def para definir o comportamento do bot.

Use @bot.message_handler() para capturar as mensagens e definir quando o bot deve responder.

------------------------------------------------------------------------------------------------------------

Automação com Jupyter, Selenium e Telegram
💻 PASSO A PASSO – Criando um robô que escreve automaticamente
Instalação de pacotes
Selenium e WebDriver precisam ser instalados via terminal no Jupyter.

Selenium: Comanda o navegador de forma automática.

WebDriver: Identifica a versão do navegador instalado, evitando a necessidade de inserir manualmente a versão correta.

Manipulação de elementos no site
find_element: Método usado para localizar elementos na página, geralmente com xpath.

xpath: Para encontrá-lo, clique com o botão direito no site e selecione Inspecionar.

.send_keys: Permite escrever dentro de um objeto identificado via xpath.

Jupyter e Anaconda
Faça o download e instale.

Após adicionar, acesse pelo terminal. O Jupyter será aberto no navegador automaticamente.

O que uma API faz?
Neste contexto, a API foi feita para acessar um site e realizar cadastros automaticamente.
