
class Parent(object):

    def __init__(self, i = 0):
        self.i = i

    def fnc(self, arg_1, arg_2 = 0):

        if arg_1 == 7:
            raise MyError('Error text')
        if arg_2:
            return arg_1 * arg_2 * self.i
        else:
            return arg_1 * arg_1 * self.i


class First(Parent):
    pass

class Second(Parent):
    pass

class A(First):

    def __init__(self):
        super(A, self).__init__()
        self.i = 3

    def isFirst(self):
        return 1

    @property
    def isSecond(self):
        return 0

    @isSecond.setter
    def isSecond(self, value):
        raise AttributeError


class MyError(BaseException):
    v = 'Error text'
