"""
КОНСПЕКТ ПО PIP - МЕНЕДЖЕРУ ПАКЕТОВ PYTHON
Источник: https://www.w3schools.com/python/python_pip.asp
"""

# =============================================
# 1. Основы PIP
# =============================================

# PIP (Pip Installs Packages) - система управления пакетами Python
# Позволяет устанавливать и управлять дополнительными библиотеками

# 1.1 Проверка установки pip
# В командной строке:
# pip --version

# 1.2 Установка pip (если не установлен)
# Скачайте get-pip.py: https://bootstrap.pypa.io/get-pip.py
# Затем выполните:
# python get-pip.py

# =============================================
# 2. Основные команды
# =============================================

# 2.1 Установка пакета
# pip install package_name

# Примеры:
# pip install numpy       # Установка NumPy
# pip install pandas      # Установка Pandas
# pip install requests    # Установка Requests

# 2.2 Установка конкретной версии
# pip install package_name==version

# Пример:
# pip install django==3.2.8

# 2.3 Установка из requirements.txt
# pip install -r requirements.txt

# 2.4 Обновление пакета
# pip install --upgrade package_name

# Пример:
# pip install --upgrade pip

# 2.5 Удаление пакета
# pip uninstall package_name

# Пример:
# pip uninstall requests

# 2.6 Просмотр установленных пакетов
# pip list

# 2.7 Поиск пакетов
# pip search "query"

# Пример:
# pip search "web framework"

# 2.8 Просмотр информации о пакете
# pip show package_name

# Пример:
# pip show numpy

# =============================================
# 3. Файл requirements.txt
# =============================================

# 3.1 Создание файла requirements.txt
# pip freeze > requirements.txt

# 3.2 Содержимое файла (пример):
"""
numpy==1.21.0
pandas==1.3.0
django==3.2.8
"""

# 3.3 Установка из requirements.txt
# pip install -r requirements.txt

# =============================================
# 4. Виртуальные окружения
# =============================================

# 4.1 Создание виртуального окружения
# python -m venv myenv

# 4.2 Активация окружения:
# Windows: myenv\Scripts\activate
# Linux/Mac: source myenv/bin/activate

# 4.3 Деактивация:
# deactivate

# =============================================
# 5. Продвинутое использование
# =============================================

# 5.1 Установка из GitHub
# pip install git+https://github.com/user/repo.git

# 5.2 Установка из локального каталога
# pip install /path/to/package

# 5.3 Установка в режиме разработки (-e)
# pip install -e .

# 5.4 Ограничение версий Python
# pip install "package_name>=1.0,<2.0"

# =============================================
# 6. Решение проблем
# =============================================

# 6.1 Ошибки прав доступа
# Используйте: pip install --user package_name

# 6.2 Проблемы с зависимостями
# pip check

# 6.3 Очистка кэша
# pip cache purge

# 6.4 Использование альтернативных репозиториев
# pip install -i https://pypi.org/simple/ package_name

# =============================================
# 7. Практические примеры
# =============================================

# 7.1 Установка пакетов для веб-разработки
"""
pip install django
pip install flask
pip install requests
pip install beautifulsoup4
"""

# 7.2 Установка пакетов для data science
"""
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install jupyter
"""

# 7.3 Установка пакетов для работы с ИИ
"""
pip install tensorflow
pip install torch
pip install openai
pip install transformers
"""

# 7.4 Создание requirements.txt для проекта
# pip freeze > requirements.txt

"""
КЛЮЧЕВЫЕ ТЕЗИСЫ:
1. Основные команды:
   - install: установка пакета
   - uninstall: удаление пакета
   - freeze: список установленных пакетов
   - list: список установленных пакетов
   - show: информация о пакете

2. Файл requirements.txt:
   - Содержит список зависимостей проекта
   - Создается командой pip freeze > requirements.txt
   - Устанавливается командой pip install -r requirements.txt

3. Виртуальные окружения:
   - Изолируют зависимости проектов
   - Создаются через python -m venv env_name
   - Активируются через source env_name/bin/activate (Linux/Mac) или env_name\Scripts\activate (Windows)

4. Best practices:
   - Всегда используйте виртуальные окружения
   - Поддерживайте актуальный requirements.txt
   - Фиксируйте версии пакетов для воспроизводимости
   - Регулярно обновляйте зависимости (pip install --upgrade)
   - Используйте pip check для проверки конфликтов

5. Распространенные пакеты:
   - Веб: Django, Flask, Requests
   - Data Science: NumPy, Pandas, Matplotlib
   - Машинное обучение: TensorFlow, PyTorch, Scikit-learn
   - Инструменты разработки: Jupyter, Black, Pylint

6. Источники пакетов:
   - Основной репозиторий: PyPI (https://pypi.org/)
   - Альтернативные репозитории: Anaconda, private repositories
   - Установка напрямую из GitHub/GitLab

7. Версионирование:
   - ~= : совместимые версии
   - == : конкретная версия
   - >= : минимальная версия
   - < : исключение версий

8. Для Windows:
   - Убедитесь, что Python и pip добавлены в PATH
   - Используйте командную строку с правами администратора при необходимости
   - Для решения проблем с путями используйте: py -m pip ...
"""