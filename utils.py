import subprocess

class Shell:
    """
    Вспомогательный класс для выполнения команд на unix-подобной ОС
    """

class FIO:
    """
    Выполняет команды FIO, собирает отчеты
    """

class Raid:
    """
    Выполняет команды RAID
    """

    def __init__(self, raid_manager):
        pass

    @staticmethod
    def run(command):
        result = None
        result = subprocess.call(command, text=True)
        return result

class ISCSI:
    """
    Настраивает iSCSI соединение
    """

