from contextlib import ExitStack


class BlackObj(object):
    __slots__ = ['value']

    def __init__(self):
        self.value = None


def singleton(cls):
    """
    Singleton decorator

    :param cls: Python class object to enforce as a singleton
    :return: Instance of cls.
    """

    instance = {}

    def get_instance(*args, **kwargs):
        """
        Get the singleton instance of the class, and instantiate it if wasn't already.

        :param args: Positional arguments passed to the constructor of the class
        :param kwargs: Nominal arguments passed to the constructor of the class
        :return: Instance of cls associated with this singleton function
        """
        if cls not in instance.keys():
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class TestContext(ExitStack):
    """Singleton Wrapper of ExitStack."""
