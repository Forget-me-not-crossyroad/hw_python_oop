# Модуль фитнес-трекера
## Финальный проект спринта: модуль фитнес-трекера
Задачей итогового проекта второго спринта курса "Python-разработчик" было создать программный модуль для фитнес-трекера, используя парадигму ООП. Модуль должен рассчитывать и отображать результаты тренировки.


Данный модуль должен выполнять следующие функции:
* принимать от блока датчиков информацию о прошедшей тренировке,
* определять вид тренировки,
* рассчитывать результаты тренировки,
* выводить информационное сообщение о результатах тренировки.


Информационное сообщение, получаемое пользователем, отображает следующие данные:
* тип тренировки (бег, ходьба или плавание);
* длительность тренировки;
* дистанция, которую преодолел пользователь, в километрах;
* среднюю скорость на дистанции, в км/ч;
* расход энергии, в килокалориях.

Фитнес-трекер можно использовать для следующих видов тренировок:
* Бег
* Плавание
* Спортивная ходьба
*********
## Технологии

[![Python Badge](https://img.shields.io/badge/-Python-blue?style=for-the-badge&labelColor=black&logo=python&logoColor=ffff00)](#)
[![VSCode Badge](https://img.shields.io/badge/-VSCode-blue?style=for-the-badge&labelColor=grey&logo=visualstudiocode&logoColor=white)](#)
[![Flake8 Badge](https://img.shields.io/badge/-Flake8-black?style=for-the-badge&labelColor=grey)](#)

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw_python_oop.git
```

или

```bash
git clone git@github.com:themasterid/hw_python_oop.git
```

Переходим в папку с проектом:

```bash
cd hw_python_oop
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Для деактивации виртуального окружения выполним (после работы):
```bash
deactivate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
