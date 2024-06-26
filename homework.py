from dataclasses import asdict, dataclass

MESSAGE: str = (
    'Тип тренировки: {training_type}; '
    'Длительность: {duration:.3f} ч.; '
    'Дистанция: {distance:.3f} км; '
    'Ср. скорость: {speed:.3f} км/ч; '
    'Потрачено ккал: {calories:.3f}.'
)


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        """Получить информационное сообщение о тренировке."""
        return MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65  # Константа количества метров в одном шаге.
    MIN_IN_H: int = 60  # Константа для перевода часов в минуты.
    M_IN_KM: int = 1000  # Константа для перевода километров в метры.

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18  # Константа умножения
    # калорий при беге.
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79  # Константа увеличения
    # калорий при беге.

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий для бега (Running)."""
        return (
            (
                self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT
            )
            * self.weight
            / self.M_IN_KM
            * self.duration
            * self.MIN_IN_H
        )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    K_1: float = 0.035  # Коэффициент 1 подсчета калорий при спортивной ходьбе.
    K_2: float = 0.029  # Коэффициент 2 подсчета калорий при спортивной ходьбе.
    M_IN_SM: float = 100  # Константа для перевода метра в сантиметры.
    KPH_TO_MPS: float = 0.278  # Константа для перевода км/ч в м/c.

    def __init__(
        self, action: int, duration: float, weight: float, height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий
        для спортивной ходьбы (SportsWalking).
        """
        return (
            (
                self.K_1 * self.weight
                + (
                    (self.get_mean_speed() * self.KPH_TO_MPS) ** 2
                    / (self.height / self.M_IN_SM)
                )
                * self.K_2
                * self.weight
            )
            * self.duration
            * self.MIN_IN_H
        )


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38  # Константа количества метров в одном гребке.
    SPEED_COEFF: float = 1.1  # Константа увеличения калорий при плавании.
    MULT_COEFF: float = 2  # Константа умножения калорий при плавании.

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        count_pool: int,
        length_pool: float,
    ) -> None:
        super().__init__(action, duration, weight)
        self.count_pool = count_pool
        self.length_pool = length_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения для плавания (Swimming)."""
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий для плавания (Swimming)."""
        return (
            (self.get_mean_speed() + self.SPEED_COEFF)
            * self.MULT_COEFF
            * self.weight
            * self.duration
        )


class Cat:
    def __init__(self, height: int, weight: int) -> None:
        self.height = height
        self.weight = weight


class Dance:
    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float,
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_type_dict: dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking,
        'CAT': Cat,  # Исправлено на Cat (вместо Dog),
        # т.к. падал NameError при каждом старте даже
        # при 'except NameError' в блоке '__main__'
        'DANCE': Dance,
        'NO_TYPE': None,
    }

    if workout_type not in workout_type_dict:
        raise KeyError(
            'Пустое значение (None) или'
            f'неверный код тренировки: {workout_type}'
        )
    return workout_type_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
        ('DANCE', [7000, 2, 75, 180]),
        ('CAT', [77, 1, 250, 200]),
        ('SWM', [1, 80, 25, 40]),
        ('NO_TYPE', [1, 80, 25, 40]),
        ('JUMP', [1, 80, 25, 40]),
    ]

    for workout_type, data in packages:
        try:
            training = read_package(workout_type, data)
            main(training)
        except KeyError:
            print('Неизвестный тип терировки')
        except TypeError as t:
            if 'positional' in repr(t):
                print('Передано неверное количество аргументов')
            if 'NoneType' in repr(t):
                print('Передано пустое значение (NoneType)')
        except AttributeError:
            print('Данный класс не содержит нужного метода или атрибута')
#  Благодарю за доп. задание
