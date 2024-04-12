from uuid import UUID

from models.command import CommandModel
from repositories.command import CommandRepository

command_repository = CommandRepository()


async def get_command(command: str) -> str:
    return await command_repository.get_command(command)


async def get_command_by_start_input(command: str) -> CommandModel:
    return await command_repository.get_command_by_start_input(command)


async def insert_default_command_values():
    if await get_command("/start") is None:
        await command_repository.insert_default_command_values()


async def get_all_commands() -> list[CommandModel]:
    return await command_repository.get_all()


async def update_command_output(new_output: str, command_id: UUID):
    await command_repository.update_command_output(new_output, command_id)
