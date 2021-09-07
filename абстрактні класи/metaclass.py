# Метаклассы - это классы для классов.
# Метаклассы предоставляют схемы для создания классов.
# По умолчанию у каждого класса есть метакласс (он называется type).
# Чтобы создать собственный метакласс, вам необходимо унаследовать type:
import abc


class AttributeInitType(type):

    def __call__(self, *args, **kwargs):
        """ Вызов класса создает новый объект. """
        # Перво-наперво создадим сам объект...
        obj = type.__call__(self, *args)
        # ...и добавим ему переданные в вызове аргументы в качестве атрибутов.
        for name in kwargs:
            setattr(obj, name, kwargs[name])
        # вернем готовый объект
        return obj


class Man(object):
    __metaclass__ = AttributeInitType


me = Man(height=180, weigth=80)
print(me.height)  # 180


# Вы также можете написать метод __new__ ,
# который предотвращает создание экземпляров классов без абстрактных методов:

class NonEmptyABC(object):
    __metaclass__ = abc.ABCMeta

    def __new__(cls, *args, **kwargs):
        # check if ANY abstractmethod exists
        for parentcls in cls.__mro__:
            if any(getattr(attr, '__isabstractmethod__', False)
                   for attr in vars(parentcls).values()):
                break
        else:
            msg = 'Abstract class {} cannot be instantiated'.format(cls.__name__)
            raise TypeError(msg)

        return super(NonEmptyABC, cls).__new__(cls, *args, **kwargs)


class EmptyAbstractClass(NonEmptyABC):
    pass


class NonemptyAbstractClass(NonEmptyABC):
    @abc.abstractmethod
    def foo(self):
        pass


class NonemptyChild(NonemptyAbstractClass):
    def foo(self):
        pass


NonemptyChild()  # works because "foo" is an abstractmethod
EmptyAbstractClass()  # throws TypeError because there are no abstractmethods
