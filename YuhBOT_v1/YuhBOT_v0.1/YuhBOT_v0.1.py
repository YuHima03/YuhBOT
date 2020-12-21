#モジュール読み込みのログ表示用
def ImportModuleLog(name, tf = 0):
    if tf == 1:
        print(f"**{str(name)}の読み込みに成功しました")
    else:
        print(f"**{str(name)}の読み込み中にエラーが発生した為、関連する機能が利用できません")

#////////////////////////////////
#//                            //
#// ここからモジュール読み込み //
#//                            //
#////////////////////////////////

#DiscordBot
try:
    import discord
    from discord.ext import commands
    bot = commands.Bot(command_prefix='y!')
    ImportModuleLog(str("discord.py"),1)
except:
    ImportModuleLog(str("discord.py"))

#怪しい日本語
try:
    import ayashii_japanese
    from ayashii_japanese import convert as GenerateAyashiiNihongo
    ImportModuleLog(str("ayashii_japanese.py"),1)
except ModuleNotFoundError as err:
    ImportModuleLog(str("ayashii_japanese.py"))

#ランダム返信
try:
    import random_reply
    if random_reply.reload_file('all') == -1:
        print("File loading failed!")
    else:
        print("File loading success!")
except ModuleNotFoundError as err:
    ImportModuleLog(str("random_reply"))

#モジュール再読み込み
def reload(name) -> str:
    pass

#/////////////////////////
#//                     //
#// ここからbotの設定等 //
#//                     //
#/////////////////////////

#help_command
class JPHelp(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.no_category = "カテゴリ未設定"
        self.command_attrs["description"] = "コマンドリストを表示します。"

    def command_not_found(self,ctx):
        return f"{ctx} というコマンドは存在しません。"

#console
@bot.event
async def on_ready():
    print('*{0.user}にログインしました'.format(bot))


#//////////////////////////////
#//                          //
#// ここからコマンドイベント //
#//                          //
#//////////////////////////////

#reply_to_"草"_msg
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.find("草") != -1:
        await message.channel.send(random_reply.rand_rep.kusa())

    await bot.process_commands(message)

#commands
@bot.command()
async def dict(ctx,*opt) -> str:
    if len(opt) >= 1:
        return
    if str(opt[1])=='list':
        pass
    elif str(opt[1]=='add'):
        for i in opt[2:]:
            random_reply.dict_add.opt[0](str(opt[i]))

@bot.command()
async def kusa(ctx,target,*arg):
    pass

@bot.command()
async def info(ctx):
    await ctx.send("YuhBOT_v0.1")

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def AyasiiNihongo(ctx, arg):
    try:
        await ctx.send(GenerateAyashiiNihongo(str(arg)))
    except NameError:
        await ctx.send("この機能は現在利用できません。\n`y!reload`コマンドを実行するか管理者にお問い合わせください")

#実行
bot.run('token')