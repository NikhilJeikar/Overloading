# Overloading
<pre>
This can be used to overload a function or class.
It has DNC type which is used to declare type a don't care
You can use Default as type to generalize a function if nothing suit the call

Example:


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
<\pre>
