"""
КОНСПЕКТ ПО РАБОТЕ С ДАТОЙ И ВРЕМЕНЕМ В PYTHON
Источник: https://www.w3schools.com/python/python_datetime.asp
"""

from datetime import datetime, date, time, timedelta
import time as tm

# =============================================
# 1. Основные классы модуля datetime
# =============================================

# 1.1 datetime - комбинированная дата и время
now = datetime.now()
print(now)  # 2023-08-04 12:30:45.123456

# 1.2 date - только дата (год, месяц, день)
today = date.today()
print(today)  # 2023-08-04

# 1.3 time - только время (часы, минуты, секунды, микросекунды)
current_time = time(12, 30, 45)
print(current_time)  # 12:30:45

# 1.4 timedelta - разница между датами/временем
delta = timedelta(days=5, hours=3)

# =============================================
# 2. Создание объектов даты и времени
# =============================================

# 2.1 Явное создание datetime
dt = datetime(2023, 8, 15, 14, 30)
print(dt)  # 2023-08-15 14:30:00

# 2.2 Создание из строки (парсинг)
date_str = "2023-12-31 23:59:59"
parsed_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed_dt)  # 2023-12-31 23:59:59

# 2.3 Создание из временной метки Unix
timestamp = 1691155800  # Количество секунд с 1970-01-01
dt_from_ts = datetime.fromtimestamp(timestamp)
print(dt_from_ts)  # 2023-08-04 12:30:00

# =============================================
# 3. Форматирование даты и времени
# =============================================

# 3.1 Преобразование в строку (strftime)
formatted = now.strftime("%d.%m.%Y %H:%M")
print(formatted)  # 04.08.2023 12:30

# 3.2 Основные форматы:
# %Y - год (4 цифры)   | %m - месяц (01-12)
# %d - день (01-31)    | %H - час (00-23)
# %M - минуты (00-59)  | %S - секунды (00-59)
# %A - день недели      | %B - название месяца

# 3.3 Локализация
# Для локализации нужно использовать locale
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
print(now.strftime("%d %B %Y"))  # 04 августа 2023

# =============================================
# 4. Арифметика с датами
# =============================================

# 4.1 Разница между датами
future_date = datetime(2024, 1, 1)
diff = future_date - now
print(diff.days)        # Количество дней
print(diff.total_seconds())  # Общее количество секунд

# 4.2 Добавление/вычитание времени
one_week_later = now + timedelta(weeks=1)
three_hours_earlier = now - timedelta(hours=3)
print(one_week_later)
print(three_hours_earlier)

# =============================================
# 5. Работа с часовыми поясами
# =============================================

# 5.1 Использование pytz (требуется установка)
# pip install pytz
import pytz

# 5.2 Создание времени с часовым поясом
utc_time = datetime.now(pytz.utc)
print(utc_time)  # 2023-08-04 09:30:00+00:00

# 5.3 Конвертация между поясами
moscow_tz = pytz.timezone('Europe/Moscow')
moscow_time = utc_time.astimezone(moscow_tz)
print(moscow_time)  # 2023-08-04 12:30:00+03:00

# =============================================
# 6. Модуль time (низкоуровневые операции)
# =============================================

# 6.1 Текущее время в секундах с эпохи
unix_time = tm.time()
print(unix_time)  # 1691155800.123456

# 6.2 Задержка выполнения
print("Начало паузы")
tm.sleep(2.5)  # Пауза 2.5 секунды
print("Конец паузы")

# 6.3 Измерение времени выполнения
start = tm.perf_counter()
# Длительная операция...
end = tm.perf_counter()
print(f"Время выполнения: {end - start:.4f} сек")

# =============================================
# 7. Практические примеры
# =============================================

# 7.1 Возраст человека
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year
    # Проверка, был ли уже день рождения в этом году
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

birthday = date(1990, 5, 15)
print(f"Возраст: {calculate_age(birthday)} лет")

# 7.2 Обратный отсчет до события
event_date = datetime(2024, 1, 1)
days_left = (event_date - now).days
print(f"До Нового года осталось: {days_left} дней")

# 7.3 Форматирование длительности
def format_duration(seconds):
    td = timedelta(seconds=seconds)
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

print(format_duration(123456))  # 1d 10h 17m 36s

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные классы:
   - datetime: дата и время
   - date: только дата
   - time: только время
   - timedelta: разница между датами

2. Форматирование:
   - strftime: объект → строка
   - strptime: строка → объект
   - Используйте директивы %Y, %m, %d и т.д.

3. Арифметика дат:
   - Разность дат возвращает timedelta
   - Добавление/вычитание с timedelta

4. Часовые пояса:
   - Используйте pytz для работы с часовыми поясами
   - Всегда храните время в UTC, конвертируйте для отображения
   - datetime.now(pytz.timezone('Europe/Moscow'))

5. Модуль time:
   - time.time(): текущее время в секундах с эпохи
   - time.sleep(): пауза в выполнении
   - time.perf_counter(): точное измерение времени

6. Best practices:
   - Для всех меток времени используйте UTC
   - Храните даты в базе данных как datetime объекты
   - Для пользовательского интерфейса форматируйте под локаль
   - Используйте timedelta для интервалов времени

7. Распространенные задачи:
   - Расчет возраста
   - Обратный отсчет до события
   - Форматирование длительности
   - Парсинг дат из разных форматов
   - Сравнение дат
"""