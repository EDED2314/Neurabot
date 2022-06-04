from main import commands, discord

@commands.command(name="hi", description="Says hi the the person you specify", guild=discord.Object(id=941049795949264969))
async def self(interaction:discord.Interaction, name:str):
    await interaction.response.send_message('Hi, ' + name)