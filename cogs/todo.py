from discord.ext import commands
from database.DB_connection import connection 
from database.models import create_task, update_task, delete_task, show_task

class TodoCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(f"You said {arg}")

    #change the name of the command to "todo_add" for "add"
    @commands.command(name="add")
    async def todo_add(self, ctx,*, arg):

        #pass the argumento to add a task
        create_task(arg)

        await ctx.send(f"added {arg} to the list")


    #change the name of the command to "todo_delete" for "delete"
    @commands.command(name="delete")
    async def todo_delete(self,ctx, *, arg):

        delete_task(arg)
        
        await ctx.send(f"Task {arg} deleted succesfully")

    #change the name of the command to "todo_update" for "update"
    @commands.command(name="update")
    async def todo_update(self, ctx, task_id: int, *, nome : str):
        
        update_task(task_id,nome)
        await ctx.send(f"Task number {task_id} updated succesfully")

    #change the name of the command to "todo_show" for "show"
    @commands.command(name="show")
    async def todo_show(self, ctx):
        await ctx.send("------ Lista de tarefas ------")

        lista = show_task()

        for i in lista:
            await ctx.send(i)

        await ctx.send("------------------------------")
