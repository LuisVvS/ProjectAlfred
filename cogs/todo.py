from discord.ext import commands
from database.DB_connection import connection 
from database.models import create_task, update_task, delete_task, show_task

class TodoCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"You said {arg}")

    @commands.command(name="add")
    async def todo_add(self, ctx,*, arg):
        
        create_task(arg)

        await ctx.send(f"added {arg} to the list")

    @commands.command(name="delete")
    async def todo_delete(self,ctx, *, arg):
        ...

    @commands.command(name="update")
    async def todo_update(self, ctx, *, arg):
        ...

    @commands.command(name="show")
    async def todo_show(self, ctx):
        await ctx.send("------ Lista de tarefas ------")

        cursor = connection().cursor()

        cursor.execute("SELECT * FROM Todo")


        rows = cursor.fetchall()

        for i in rows:
            await ctx.send(i)
        await ctx.send("------------------------------")
