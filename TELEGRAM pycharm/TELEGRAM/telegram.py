import telebot

chave_api = "7849162515:AAFfncNNnS5srksESWQ2Cw9PfYAE4N5Z-Vw"

bot = telebot.TeleBot(chave_api)




@bot.message_handler(commands =["OPCAO1"])
def opcao1(mensagem):
    texto = """ Pra fazer seu cadastro, precisamos dos seguintes dados:
  - Nome completo
  - Endereço
  - CNPJ/CPF
  - Celular
    Envie tudo para: cadastro@gmail.com. 
    Assim que confirmarmos, nossa equipe entra em contato."""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["OPCAO2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, """Fica tranquilo(a), nosso time vai te procurar
    Mas se quiser agilizar, é só mandar um e-mail pra gente:
    contatoorcamento@gmail.com
    """)

@bot.message_handler(commands=["OPCAO3"])
def opcao3(mensaegem):
    bot.reply_to(mensaegem, """Precisando de ajuda?

Eduardo: (11) 0000-0000
Maria: (11) 1111-1111
E-mails: teste123@gmail.com | teste321@gmail.com
Nosso time espera seu contato!""")




def verificar(mensagem):
    return True



@bot.message_handler(func=verificar)
def responder (mensagem):
    texto =""" ESCOLHA UMA DAS OPÇÕES ABAIXO (clique no link)
        /OPCAO1 FAZER CADASTRO:
        /OPCAO2 FAZER UM ORÇAMENTO:
        /OPCAO3 ENTRAR EM CONTATO COM VENDEDOR:
    responder qualquer outra função não irar funcionar!   
    """
    bot.reply_to(mensagem, texto)


bot.polling()