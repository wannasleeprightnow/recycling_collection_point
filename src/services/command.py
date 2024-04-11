from repositories.command import CommandRepository

command_repository = CommandRepository()


async def get_command_output(command: str) -> str:
    return await command_repository.get_command_output(command)


async def insert_default_command_values():
    if await get_command_output("/start") is None:
        await command_repository.insert_default_command_values()
