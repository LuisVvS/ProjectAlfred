from discord.ext import commands
from database.DB_connection import connection 


class TodoCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"You said {arg}")

    @commands.command()

    async def todo_add(self, ctx,*, arg):
        cursor = connection().cursor()

        cursor.execute("INSERT INTO Todo(nome) VALUES(%s)", (arg))

        connection().commit()

        await ctx.send("added to the list")

    @commands.command()
    async def todo_show(self, ctx):
        await ctx.send("------ Lista de tarefas ------")

        cursor = connection().cursor()

        cursor.execute("SELECT * FROM Todo")


        rows = cursor.fetchall()

        for i in rows:
            await ctx.send(i)
        await ctx.send("------------------------------")
