
M_IN_KM: int = 1000


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    MIN_IN_H: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # distance: float = self.get_distance()
        # speed: float = self.get_mean_speed()
        # calories: float = self.get_spent_calories()
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / M_IN_KM * self.duration * self.MIN_IN_H)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    K_1: float = 0.035  # Коэффициент для подсчета калорий.
    K_2: float = 0.029  # Коэффициент для подсчета калорий.
    M_IN_SM: float = 0.01
    S_IN_MIN: int = 3600

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.K_1 * self.weight
                + ((self.get_mean_speed() / self.S_IN_MIN
                    * M_IN_KM)**2 / self.height * self.M_IN_SM)
                * self.K_2 * self.weight) * self.duration * self.MIN_IN_H)


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, 
                 stroke_count: int, 
                 action: int, 
                 duration: float, 
                 weight: float, 
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.stroke_count = stroke_count
        self.height = height


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'RUN':
        return Running(*[data])
    if workout_type == 'WLK':
        return Running(*[data])
    if workout_type == 'SWM':
        return Running(*[data])
    return None


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
