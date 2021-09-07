# Aбстрактные классы - это классы, которые не могут быть созданы.
# Это так, потому что абстрактные классы не определяют реализацию функций.
# Вместо этого вы указываете только сигнатуры методов и типы свойств (иногда),
# и каждый дочерний класс должен предоставлять свою собственную реализацию.
# Обратите внимание, что по-прежнему можно предоставить некоторую реализацию.
# Например, абстрактный класс может реализовать конструктор по умолчанию..

# Итак, абстрактный метод получает атрибут __isabstractmethod__ при назначении ему
# декоратора. Атрибуты после наследования от абстрактного класса собираются во
# множестве "__abstractmethods__" класса-наследника. Если множество не пустое, и
# программист пытается создать объект класса, то будет вызвано исключение
# TypeError со списком неопределенных методов.

# В Python абстракция реализована через abcмодуль во встроенной библиотеке.
# Это простейший пример того, как его использовать:
from abc import ABC, abstractmethod


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self, data):
        pass


