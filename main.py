import discord
from discord.ext import commands
import datetime
from datetime import *
import asyncio
from chaveBOT import chaveBOT
from funcoes import verificacao

bot = commands.Bot(
    description='Um bot feito para um trabalho universitário', command_prefix='.')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Digite .ajuda"))
    print("""
    ----------------------------------
                Bot Online!
       Feito por: Bruno Durão Silva
         e Gustavo Santos Rocha
  Projeto AV3 de Tec. e Ling. Progamação:
            Bot lembrete discord
                build v1.0
    ----------------------------------
     versão da API discord.py:""", discord.__version__, """
    ----------------------------------

Registro de ações no console:
""")


# Eventos de erro (Comando não encontrado, sem requerimentos ou requerimento errado)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):  # Comando não encontrado
        await ctx.send("Este comando não existe.")

    # Faltou argumento (somar a + b -> somar 1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltam Argumentos. Digite .ajuda para saber como utilizar o comando corretamente!")

    # Argumento inválido (somar a + b -> somar 1 danilo)
    if isinstance(error, commands.BadArgument):
        await ctx.send("Argumento inválido. Digite .ajuda para saber como utilizar o comando corretamente!")


@bot.command()  # Comando de teste para ver se o bot pode mandar mensagens no servidor
async def teste(ctx):
    await ctx.message.add_reaction("✅")
    await ctx.send("Teste concluido!")
    print("Teste concluido.")

# Variável global que pode ser utilizada em varias funções assíncrionas (async def)
global datahoje
datahoje = datetime.now()  # Função da biblioteca datetime que pega a data e hora atual


# "@bot.command()" Indica que a função a seguir é um comando seguindo a API discord.py

@bot.command()  # Comando para salvar um lembrete para hoje
async def lembretehoje(ctx, horario: str, *, descricao: str = ""):

    if verificacao(hora=horario) == True:
        if descricao == "":
            mensagemBot = await ctx.send(f"O horário: '{horario}' foi armazenado")

        else:
            mensagemBot = await ctx.send(f"O horário: '{horario}' e a descrição: '{descricao}' foram armazenados")

        await mensagemBot.pin()  # Fixa a mensagem no servidor

        # Variável global que pode ser acessada em outras funções (def)
        global horalembretehoje
        global descricaohoje    # Idem
        descricaohoje = descricao  # Recebe o parâmetro passado pelo usuário
        datahoje = datetime.now()  # Atualiza o horário e data atuais armazenado no bot

        # Coleta a string passada pelo usuário (xx:xx) e transforma em um objeto datetime
        horalembretehoje = datetime.strptime(horario, "%H:%M")
        horalembretehoje = horalembretehoje.replace(day=int(datahoje.day))
        # Troca o dia, mês e ano pelos atuais armazenados no bot
        horalembretehoje = horalembretehoje.replace(month=int(datahoje.month))
        horalembretehoje = horalembretehoje.replace(year=int(datahoje.year))
        print(f"Horário armazenado por {ctx.author}: " + str(horalembretehoje))
        return horalembretehoje, descricaohoje  # Atualiza as variáveis globalmente

    else:
        await ctx.send(f"O horário: '{horario}' é inválido!")


@bot.command() # Comando para salvar um lembrete com data
async def lembretedia(ctx, horario: str, dia: str, *, descricao: str = ""):

    if verificacao(data=dia) == True:
        if descricao == "":
            mensagemBot = await ctx.send(f"O horário '{horario}' e o dia '{dia}' foram armazenados")

        else:
            await ctx.send(f"O horário '{horario}', o dia '{dia}' e a descrição '{descricao}' foram armazenados")

        objetivo = horario+" "+dia
        datahoje = datetime.now()
        global horalembretedia
        global descricaodia
        descricaodia = descricao
        horalembretedia = datetime.strptime(objetivo, "%H:%M %d/%m")
        horalembretedia = horalembretedia.replace(year=int(datahoje.year))
        print(f"Data armazenada por {ctx.author}: {str(horalembretedia)}")
        return horalembretedia, descricaodia

    else:
        await ctx.send(f"O horário '{horario}' e/ou o dia '{dia}' são inválidos!")


@bot.command() # Comando para confirmar o lembrete salvo
async def confirmarlembrete(ctx, lembrete: str):
    datahoje = datetime.now()

    if lembrete == "hoje":
        deltatempo = horalembretehoje-datahoje
        if deltatempo.total_seconds() < 0:
            await ctx.send("Impossível guardar lembrete! O horário expirou.")
        else:
            await ctx.send("O lembrete foi ativado!")
            descricao = descricaohoje
            print(
                f"Tempo até o lembrete: {deltatempo.total_seconds()} Segundos")
            await asyncio.sleep(deltatempo.total_seconds())
            if descricao == "":
                await ctx.send(f"Lembrete do dia! @everyone")
            else:
                await ctx.send(f"Lembrete do dia: '{descricao}' @everyone")

    elif lembrete == "dia":
        deltatempo = horalembretedia-datahoje
        if deltatempo.total_seconds() < 0:
            await ctx.send("Impossível guardar lembrete! O horário expirou.")
        else:
            await ctx.send("O lembrete foi ativado!")
            descricao1 = descricaodia
            print(
                f"Segundos até o lembrete programado: {deltatempo.total_seconds()}")
            await asyncio.sleep(deltatempo.total_seconds())
            await ctx.send(f"Lembrete! {descricao1} @everyone")


@bot.command()  # Comando de teste para ver se o bot pode mandar mensagens no servidor
async def dataagora(ctx):
    datahoje = datetime.now()
    await ctx.send(str(datahoje.strftime("**Hora atual:** %H:%M.\n**Data atual:** %d/%m/%Y.")))
    print(
        f'Horário atual exibido! {datahoje.strftime("Hora atual: %H:%M. Data atual: %d/%m/%Y.")}')


@bot.command() # Comando de ajuda, mostra todos os outros comandos
async def ajuda(ctx):
    embed = discord.Embed(
        title="Aqui estão todos os comandos do bot atualmente:", color=0x000080)
    embed.add_field(name="**ajuda**",
                    value="Mostra estes comandos", inline=False)
    embed.add_field(
        name="**teste**", value="Um comando de teste, verifica se o bot está funcional.", inline=False)
    embed.add_field(name="**lembretehoje**",
                    value="Salva o horário como o lembrete de hoje. Uso: **lembretehoje 23:59 (descrição opcional)**", inline=False)
    embed.add_field(name="**lembretedia**",
                    value="Salva um horário e um dia específico para o lembrete. Uso correto: **.lembretedia 23:59 31/12 (descrição opcional)**", inline=False)
    embed.add_field(name="**confirmarlembrete**",
                    value="Confirma um dos horários salvos e o utiliza como lembrete. Uso correto: **.ativar lembrete hoje/dia**", inline=False)
    embed.add_field(name="**sugestao**",
                    value="E-mail para contato de sugestões para o bot.", inline=False)
    embed.add_field(
        name="**fale**", value="O bot fala o que você quiser. Uso correto: **.fale** (**o que o bot falará**).", inline=False)
    embed.add_field(name="**renomear**",
                    value="Bota o nome que você quiser no bot. Uso correto: **.renomear** (**novo nome do bot**).", inline=False)
    embed.add_field(name="**limpar**",
                    value="Limpe o chat. Uso correto: **.limpar** (**quantidade**) [sem quantidade informada, serão apagadas 100 mensagens].", inline=False)
    embed.add_field(name="**Autoria**",
                    value="Bot feito por Bruno Durão Silva e Gustavo Santos Rocha", inline=False)
    await ctx.send(embed=embed)


@bot.command() # Comando para limpar o chat
async def limpar(ctx, quantidade=100):
    await ctx.channel.purge(limit=quantidade + 1)
    print("O chat foi limpo por {}!".format(ctx.author))


@bot.command() # Comando para contatar os desenvolvedores
async def sugestao(ctx):
    await ctx.send("Sugestões são bem vindas! E-mail para contato: **contato.brunodurao@gmail.com** ou **k13gustavo@gmail.com**")


@bot.command() # Comando para excluir mensagens no chat
async def fale(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)
    print("O bot falou '{}' no chat!".format(arg))


@bot.command() # Comando para trocar o nome do Bot
async def renomear(ctx, *, name: str):
    await bot.user.edit(username=name)

chave = int(input(
    """O bot pode iniciar?
1 = sim
0 = não
resposta: """
))
if chave == 1:
    print("Bot iniciado")
    bot.run(chaveBOT)
