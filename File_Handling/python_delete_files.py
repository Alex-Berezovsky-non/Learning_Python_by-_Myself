"""
КОНСПЕКТ ПО УДАЛЕНИЮ ФАЙЛОВ И ДИРЕКТОРИЙ В PYTHON
Источник: https://www.w3schools.com/python/python_file_remove.asp
"""

import os
import shutil

# =============================================
# 1. Удаление файлов
# =============================================

# 1.1 Основной метод: os.remove()
try:
    os.remove("file_to_delete.txt")
    print("Файл успешно удален")
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Нет прав на удаление файла")
except Exception as e:
    print(f"Ошибка при удалении: {e}")

# 1.2 Альтернатива: os.unlink() (аналог os.remove())
try:
    os.unlink("another_file.txt")
    print("Файл успешно удален (unlink)")
except OSError as e:
    print(f"Ошибка удаления: {e.strerror}")

# =============================================
# 2. Удаление директорий
# =============================================

# 2.1 Удаление ПУСТОЙ директории: os.rmdir()
try:
    os.rmdir("empty_directory")
    print("Пустая директория удалена")
except FileNotFoundError:
    print("Директория не найдена")
except OSError as e:
    print(f"Ошибка: {e.strerror} - директория не пуста или нет прав")

# 2.2 Удаление НЕпустой директории: shutil.rmtree()
try:
    shutil.rmtree("directory_with_files")
    print("Директория с содержимым удалена")
except FileNotFoundError:
    print("Директория не найдена")
except PermissionError:
    print("Нет прав на удаление")
except Exception as e:
    print(f"Ошибка удаления: {e}")

# =============================================
# 3. Безопасное удаление
# =============================================

# 3.1 Проверка существования перед удалением
file_path = "temp_file.txt"

if os.path.exists(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} удален")
    except Exception as e:
        print(f"Ошибка удаления: {e}")
else:
    print(f"Файл {file_path} не существует")

# 3.2 Проверка типа объекта
path_to_delete = "some_path"

if os.path.exists(path_to_delete):
    if os.path.isfile(path_to_delete):
        os.remove(path_to_delete)
        print("Файл удален")
    elif os.path.isdir(path_to_delete):
        shutil.rmtree(path_to_delete)
        print("Директория удалена")
    else:
        print("Неизвестный тип объекта")
else:
    print("Объект не существует")

# 3.3 Удаление с корзины (более безопасное)
try:
    import send2trash
    send2trash.send2trash("file_to_recycle.txt")
    print("Файл перемещен в корзину")
except ImportError:
    print("Модуль send2trash не установлен. Используем полное удаление.")
    try:
        os.remove("file_to_recycle.txt")
    except Exception as e:
        print(f"Ошибка удаления: {e}")

# =============================================
# 4. Удаление по шаблону (нескольких файлов)
# =============================================

# 4.1 Удаление всех .tmp файлов в директории
import glob

for file_path in glob.glob("temp_files/*.tmp"):
    try:
        os.remove(file_path)
        print(f"Удален: {file_path}")
    except Exception as e:
        print(f"Ошибка удаления {file_path}: {e}")

# 4.2 Удаление всех файлов в директории
def clear_directory(dir_path):
    if not os.path.isdir(dir_path):
        print(f"{dir_path} не является директорией")
        return
    
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Ошибка удаления {file_path}: {e}")

# clear_directory("temp_folder")

# =============================================
# 5. Практические примеры
# =============================================

# 5.1 Очистка временных файлов
def clean_temp_files():
    temp_dirs = [
        "/tmp",
        os.path.join(os.getenv("TEMP", ""), "my_app"),
        "local_temp"
    ]
    
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            print(f"Очистка {temp_dir}")
            for file in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Удален файл: {file}")
                except Exception as e:
                    print(f"Ошибка удаления {file_path}: {e}")

# clean_temp_files()

# 5.2 Удаление устаревших файлов
import time
def delete_old_files(directory, days=30):
    now = time.time()
    cutoff = now - (days * 86400)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_time = os.path.getmtime(file_path)
            if file_time < cutoff:
                try:
                    os.remove(file_path)
                    print(f"Удален устаревший файл: {filename}")
                except Exception as e:
                    print(f"Ошибка удаления {file_path}: {e}")

# delete_old_files("logs", days=7)

# 5.3 Полное удаление приложения
def uninstall_app(app_dir):
    # Удаление файлов приложения
    if os.path.exists(app_dir):
        try:
            shutil.rmtree(app_dir)
            print(f"Директория приложения {app_dir} удалена")
        except Exception as e:
            print(f"Ошибка удаления директории: {e}")
    
    # Удаление ярлыков и записей в реестре (для Windows)
    if os.name == 'nt':
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software", 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteKey(key, "MyApp")
            print("Записи реестра удалены")
        except Exception as e:
            print(f"Ошибка очистки реестра: {e}")

# uninstall_app("C:/Program Files/MyApp")

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные методы удаления:
   - Файлы: os.remove(), os.unlink()
   - Пустые директории: os.rmdir()
   - Непустые директории: shutil.rmtree()

2. Обработка ошибок:
   - Всегда используйте try-except при удалении
   - Основные исключения: FileNotFoundError, PermissionError, OSError
   - Проверяйте существование объекта перед удалением (os.path.exists())

3. Безопасное удаление:
   - Проверяйте тип объекта (файл или директория)
   - Используйте send2trash для перемещения в корзину
   - Для важных данных реализуйте подтверждение перед удалением

4. Продвинутые сценарии:
   - Удаление по шаблону (glob.glob())
   - Рекурсивное удаление (shutil.rmtree())
   - Удаление устаревших файлов (по времени модификации)
   - Очистка временных файлов

5. Best practices:
   - Всегда делайте бэкап перед массовым удалением
   - Проверяйте права доступа
   - Для кросс-платформенности используйте os.path
   - Логируйте операции удаления
   - Предоставляйте пользователю возможность отмены

6. Особенности:
   - В Linux/Mac может потребоваться sudo для удаления системных файлов
   - shutil.rmtree() удаляет без возможности восстановления
   - Удаление открытых файлов может вызвать ошибки (особенно в Windows)

7. Предупреждения:
   - Будьте осторожны с путями вроде '/' или 'C:\' - можно удалить всю систему!
   - Дважды проверяйте путь перед удалением
   - Не удаляйте файлы без верификации

8. Альтернативы полному удалению:
   - Перемещение в корзину (send2trash)
   - Архивация вместо удаления
   - Переименование с префиксом "_old"
   - Физическое уничтожение данных для конфиденциальной информации
"""