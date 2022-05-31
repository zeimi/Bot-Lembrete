import discord
from discord.ext import commands, tasks
from discord.utils import get
import datetime
from datetime import *
import asyncio

bot = commands.Bot(description='Um bot feito para um trabalho universitário', command_prefix='.')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Digite .ajuda"))
    print("""
    ----------------------------------
                Bot Online!
       Feito por: Bruno Durão Silva
         e Gustavo Santos Rocha
        Projeto AV3 de programação:
            Bot lembrete discord
                build v0.1
    ----------------------------------
    versão da API discord.py:""", discord.__version__, """
    ----------------------------------
Registro de ações no console:""")


@bot.event # Eventos de erro (Comando não encontrado, sem requerimentos ou requerimento errado)
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): # Comando não encontrado
        await ctx.send("Este comando não existe.")

    if isinstance(error, commands.MissingRequiredArgument): # Faltou argumento (somar a + b -> somar 1)
        await ctx.send("Faltam Argumentos. Digite .ajuda para saber como utilizar o comando corretamente!")

    if isinstance(error, commands.BadArgument): # Argumento inválido (somar a + b -> somar 1 danilo)
        await ctx.send("Argumento inválido. Digite .ajuda para saber como utilizar o comando corretamente!")


@bot.command() # Comando de teste para ver se o bot pode mandar mensagens no servidor
async def teste(ctx):
    await ctx.message.add_reaction("✅")
    await ctx.send("Teste concluido!")
    print("Teste concluido!")

global datahoje # Variável global que pode ser utilizada em varias funções assíncrionas (async def)
datahoje = datetime.now() # Função da biblioteca datetime que pega a data e hora atual

@bot.command()
async def lembretehoje(ctx, horario: str): 
    await ctx.send(f"O horário: '{horario}' foi armazenado")
    global horalembretehoje
    datahoje = datetime.now()
    horalembretehoje = datetime.strptime(horario, "%H:%M")
    horalembretehoje = horalembretehoje.replace(day=int(datahoje.day))
    horalembretehoje = horalembretehoje.replace(month=int(datahoje.month))
    horalembretehoje = horalembretehoje.replace(year=int(datahoje.year))
    print("Horário armazenado: "+ str(horalembretehoje))
    return horalembretehoje

@bot.command()
async def lembretedia(ctx, horario: str, dia: str): 
    await ctx.send(f"O horário '{horario}' e o dia '{dia}' foram armazenados")
    objetivo = horario+" "+dia
    datahoje = datetime.now()
    global horalembretedia
    horalembretedia = datetime.strptime(objetivo, "%H:%M %d/%m")
    horalembretedia = horalembretedia.replace(year=int(datahoje.year))
    print(f"Data armazenada: {str(horalembretedia)}")
    return horalembretedia

@bot.command()
async def ativarlembrete(ctx, lembrete: str):
    datahoje = datetime.now()
    if lembrete == "hoje":
        deltatempo = horalembretehoje-datahoje
        if deltatempo.total_seconds() < 0:
            await ctx.send("Impossível guardar lembrete! O horário expirou.")
        else:
            await ctx.send("O lembrete foi ativado!")
            print(deltatempo.total_seconds())
            await asyncio.sleep(deltatempo.total_seconds())
            await ctx.send("Lembrete do dia! @everyone")
    elif lembrete == "dia":
        deltatempo = horalembretedia-datahoje
        if deltatempo.total_seconds() < 0:
            await ctx.send("Impossível guardar lembrete! O horário expirou.")
        else:
            await ctx.send("O lembrete foi ativado!")
            print(deltatempo.total_seconds())
            await asyncio.sleep(deltatempo.total_seconds())
            await ctx.send("Lembrete programado! @everyone")


@bot.command() # Comando de teste para ver se o bot pode mandar mensagens no servidor
async def dataagora(ctx):
    datahoje = datetime.now()
    await ctx.message.add_reaction("✅")
    await ctx.send(str(datahoje.strftime("**Data atual:** %H:%M.\n**Hora atual:** %d/%m/%Y.")))
    print("Horário atual exibido!")


@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(title="Aqui estão todos os comandos do bot atualmente:", color=0x000080)
    embed.add_field(name="**ajuda**", value="Mostra estes comandos", inline=False)
    embed.add_field(name="**teste**", value="Um comando de teste, verifica se o bot está funcional.", inline=False)
    embed.add_field(name="**lembretehoje**", value="Salva o horário como o lembrete de hoje. Uso: **lembretehoje 23:59**", inline=False)
    embed.add_field(name="**cargos**", value="Escolha um cargo usando reações.", inline=False)
    embed.add_field(name="**somar**", value="Soma dois números inteiros. Uso correto: **.somar 1 1**", inline=False)
    embed.add_field(name="**multiplicar**", value="Multiplica dois números inteiros. Uso correto: **.multiplicar 1 1**",
                    inline=False)
    embed.add_field(name="**dividir**", value="Divide dois números inteiros. Uso correto: **.dividar 1 1**",
                    inline=False)
    embed.add_field(name="**expulsar**", value="Expulsa um usuário do servidor. Uso correto: **.expulsar @usuario**",
                    inline=False)
    embed.add_field(name="**banir**", value="Bane um usuário do servidor. Uso correto: **.banir @usuario**",
                    inline=False)
    embed.add_field(name="**desbanir**",
                    value="Tira o banimento de um usuário banido do servidor. Uso correto: **.desbanir usuario#0000**",
                    inline=False)
    embed.add_field(name="**admin**",
                    value="Verifica se o usuário é um administrador do servidor. Uso correto: **.admin @usuario**",
                    inline=False)
    embed.add_field(name="**sugestao**", value="E-mail para contato de sugestões para o bot.", inline=False)
    embed.add_field(name="**fale**",
                    value="O bot vira seu papagaio pessoal. Uso correto: **.fale** (**o que o bot falará**).",
                    inline=False)
    embed.add_field(name="**limpar**",
                    value="Limpe o chat. Uso correto: **.limpar** (**quantidade**) [sem quantidade informada, serão apagadas 100 mensagens].",
                    inline=False)
    embed.add_field(name="**Autoria**", value="Bot feito por Bruno Durão Silva e Gustavo Santos Rocha", inline=False)
    await ctx.send(embed=embed)



@bot.command()
async def limpar(ctx, quantidade=100):
    await ctx.channel.purge(limit=quantidade + 1)
    print("O chat foi limpo por {}!".format(ctx.author))


chave = int(input("""O bot pode iniciar?
1 = sim
0 = não
resposta: """))
if chave == 1:
    print("Bot iniciado")
    bot.run('OTc5ODY0MDI3NzU0Nzk5MTE0.GZGv1B.y8pYxqu_L9wm903qaESlboq-0GtFhDj02j4j1s')
