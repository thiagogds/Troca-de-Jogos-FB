def admin_attrs(**kwargs):

    def decorate(function):
        for key, value in kwargs.items():
            setattr(function, key, value)

        return function

    return decorate
