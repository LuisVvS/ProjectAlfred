from logging import exception
from discord.ext import commands
from database.DB_connection import connection 
from database.models import create_task, update_task, delete_task, show_task

class TodoCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    #add a event listener to handle with error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #verify if the error is of the type MissingRequiredArgument
        if isinstance(error, commands.MissingRequiredArgument):
            #bot will send this message if we dont pass any argument
            await ctx.send("You need do pass arguments after this command")
        else:
            #handle with another errors
            await ctx.send("An error ocurred while running the program")
            raise error

    @commands.command()
    async def echo(self, ctx, *, arg):
        try:
            await ctx.send(f"You said {arg}")
        except Exception as e:
            await ctx.send(f"An error {e} has ocurried")

    #change the name of the command to "todo_add" for "add"
    @commands.command(name="add")
    async def todo_add(self, ctx,*, arg):
        try:
            if not arg: 
                return 
            #pass the argumento to add a task
            create_task(arg)
            await ctx.send(f"added {arg} to the list")
        except Exception as e:
            await ctx.send(f"Error occurried: {e}")



    #change the name of the command to "todo_delete" for "delete"
    @commands.command(name="delete")
    async def todo_delete(self,ctx, *, arg):
        try:
            delete_task(arg)
            await ctx.send(f"Task {arg} deleted succesfully")
        except Exception as e:
            await ctx.send(f"Error occurried: {e}")

    #change the name of the command to "todo_update" for "update"
    @commands.command(name="update")
    async def todo_update(self, ctx, task_id: int, *, nome : str):
        
        try:
            update_task(task_id,nome)
            await ctx.send(f"Task number {task_id} updated succesfully")
        except commands.BadArgument as e:
            await ctx.send("The arguments are invalid, please review them")
        except Exception as e:
            await ctx.send(f"Error occurried: {e}")

    #change the name of the command to "todo_show" for "show"
    @commands.command(name="show")
    async def todo_show(self, ctx):
        try:
            await ctx.send("------ Lista de tarefas ------")

            lista = show_task()

            for i in lista:
                await ctx.send(i)

            await ctx.send("------------------------------")
        except Exception as e:
            await ctx.send(f"Error occurried: {e}")
