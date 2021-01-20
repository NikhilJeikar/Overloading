CallBacksFunctions = {}
DefaultFunctions = {}


class DNC:
    __doc__ = "This class is used to declare a parameter type to any while overloading"


class Default:
    __doc__ = "This class is used to declare a method as default when there is no method is available to call"


def Overload(*Types):
    def Wrapper(Name):
        name = Name.__name__
        Callback = CallBacksFunctions.get(name)
        tup = tuple(i for i in Types)
        if len(tup) == 1 and tup[0] == Default:
            DefaultFunctions[name] = Name
        else:
            if Callback is None:
                Function = {tup: Name}
                CallBacksFunctions[name] = Function
            else:
                find = Callback.get(tup)
                if find is None:
                    Callback[tup] = Name

        def Caller(*Args):
            Search = tuple(i.__class__ for i in Args)
            keys = list(Callback.keys())
            final = []
            for key in keys:
                index = 0
                Found = True
                for i in Search:
                    if index < len(key):
                        if i != key[index] and key[index] != DNC:
                            Found = False
                            break
                        index = index + 1
                if Found:
                    if len(Search) == len(key):
                        final.append(key)
            if len(final) >= 1:
                function = Callback[final[len(final) - 1]]
                print(function)
                if function is None:
                    default = DefaultFunctions.get(name)
                    if default is None:
                        class FunctionNotFound(Exception):
                            pass

                        raise FunctionNotFound("No Such overloaded or default function exist")
                    else:
                        function = default
                return function(*Args)
            else:
                class FunctionNotFound(Exception):
                    pass

                default = DefaultFunctions.get(name)
                print(default, name)
                if default is None:
                    raise FunctionNotFound("No Such overloaded or default function exist")
                else:
                    function = default
                return function(*Args)

        return Caller

    return Wrapper

# Use Overload as decorator
# Pass Default as argument  to make it as default if nothing is suitable to run
# DNC can be passed to make that variable type as don't care

"""
Example 


@Overload(int)
class A:
    def __init__(self, y):
        print(y)


@Overload(DNC, DNC)
class A:
    def __init__(self, x, y):
        print(x, y)


@Overload(Default)
class A:
    def __init__(self, y):
        print(2, y)


A(1)
A(10, 1)
A(1.2)
A("a")

"""
