class MyClass:
    def public_method(self):
        pass

    def public_attribute(self):
        self.public_var = 10

class MyClass:
    def _protected_method(self):
        pass

    def _protected_attribute(self):
        self._protected_var = 10

class MyClass:
    def __private_method(self):
        pass

    def __private_attribute(self):
        self.__private_var = 10