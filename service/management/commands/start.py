from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = ('Выполнение команд для создания и применения миграции,'
          'добавлению по умолчанию 20 машин в БД, выгрузки данных из файла uszips.csv в БД,'
          'создания суперпользователя.')

  def handle(self, *args, **options) -> None:
    try:
      management.call_command('makemigrations')
      management.call_command('migrate')
      management.call_command('loadlocation')
      management.call_command('addcar')
      management.call_command('createsuperuser')

    except Exception as ex:
      print(f'Ошибка {ex}')
