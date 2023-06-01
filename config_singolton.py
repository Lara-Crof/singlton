'''
Напишите python class, который читает стандартный файл конфигурации,
имеющий структуру [секция], ключ=значение.
2. Напишите конструктор этого класса, который принимает параметр - путь к файлу
3. Напишите методы класса:
- get (получение данных конфигурационного файла по секциям, по ключу)
- reload (перечитывание файла, входящий параметр - путь к файлу)
Класс должен быть написан в паттерне проектирования Singletone.
'''
import configparser
from typing import Optional


path = 'airflow.cfg'

class ConfigFile(configparser.ConfigParser):
    """Класс, который читает стандартный файл конфигурации,
    имеющий структуру [секция], ключ=значение.
    """

    config = None

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigFile, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, path: Optional[str]=None) -> None:
        super().__init__()
        self.path = path
        self.config = self.reload()

    
    def reload(self) -> configparser.SectionProxy:
        """Перечитывание файла, входящий параметр - путь к файлу."""
        with open(self.path) as conf:
            self.config = self.read_file(conf)
        return self.config
    
if __name__ == '__main__':
    test_conf = ConfigFile(path)
    print(test_conf.get('core', 'dags_folder'))
    test_conf.reload()
    conf2 = ConfigFile(path)
    assert test_conf == conf2
    print(test_conf['core']['dags_are_paused_at_creation'])
