from service.models import Car, Location, Cargo
from django.core.management.base import BaseCommand, CommandParser

def delete_info_of_models() -> None:
  """
  Функция для удаления всех данных из БД.
  """
  Car.objects.all().delete()
  print('Данные из таблицы Car удалены!')
  Location.objects.all().delete()
  print('Данные из таблицы Location удалены!')
  Cargo.objects.all().delete()
  print('Данные из таблицы Cargo удалены!')


class Command(BaseCommand):
  help = 'Удаление таблиц из БД'

  def add_arguments(self, parser: CommandParser):
    parser.add_argument('--delete', action='store_true', help='Очистка таблиц БД')

  def handle(self, *args, **options):
    try:
      delete_info_of_models()
    except Exception as ex:
      print(f'Ошибка ввода команды: {ex}')
