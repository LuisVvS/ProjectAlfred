from discord.ext import commands


todo_list = []

class TodoCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"You said {arg}")

    @commands.command()
    async def todo_add(self, ctx,*, arg):
        todo_list.append(f"{arg}")
        await ctx.send("added to the list")

    @commands.command()
    async def todo_show(self, ctx):
        await ctx.send("------ Lista de tarefas ------")
        for i in todo_list:
            await ctx.send(i)
        await ctx.send("------------------------------")
