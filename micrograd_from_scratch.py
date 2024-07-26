# %%
import math
import numpy as np
import matplotlib.pyplot as plt


# %%
# let's start by defining a simple function f(x) = 3x^2 - 4x + 5
def f(x):
    return 3 * x**2 - 4 * x + 5


print(f(3.0))
# %%
# let's plot this function
xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)

# %%
# let's define the derivative, i.e. gradient, of f(x) = 3x^2 - 4x + 5
# if we are going slightly to the right when at point 3, where do you expect to be? Are you going up or down?
h = 0.001
x = 3.0
f(x + h)

# so you are going up. Let's calculate the gradient
df = (f(x + h) - f(x)) / h
df
# %%
# we can also check at -3
x = -3.0
df = (f(x + h) - f(x)) / h
df
# %%
# how does this work when we have multiple variables/inputs?
# inputs
a = 2.0
b = -3.0
c = 10.0

d1 = a * b + c
a += h
d2 = a * b + c
dfda = (d2 - d1) / h
dfda


# %%
class Value:
    def __init__(self, data):  # initialise the object
        self.data = data

    def __repr__(
        self,
    ):  # overwrite an existing python method (repr) to print the object in a readable way; also called dunder mehod for double underscore
        return f"Value(data={self.data})"

    def __add__(self, other):  # overwrite dunder method to add two objects
        return Value(self.data + other.data)

    def __mul__(self, other):  # overwrite dunder method to multiply two objects
        return Value(self.data * other.data)


a = Value(2.0)
a
b = Value(-3.0)
c = Value(10.0)
d = a * b + c
d


# %%
# Now we want to extend this class so that we can check the previous value, the new value, and the operation that was performed to get the new value
class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self._prev = set(
            _children
        )  # note that we use the underscore to indicate that this is a private variable; i.e. it should not be accessed directly by the user but only by the class itself
        self._op = _op

    def __repr__(
        self,
    ):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")

# %%
a = Value(2.0)
a
# %%
a._prev
# %%
a._op
# %%
# So we see that the previous value is empty and the operation is empty because we have not performed any operations yet. Let's do that now:
b = Value(-3.0)
e = a*b
# %%
e
# %%
e._prev
# %%
e._op
# %%
# Let's add another operation
c = Value(10.0)
d = a*b + c
d
# %%
d._prev
# %%
d._op
# %%
# I find this a bit weird because we actually have two operations going on for d and d was just always the result of this operattion. So there is nothing "previous" really here. It seems a bit arbitrary that a*b = -6 is seen as a previous result and c=10 and that we do not have 3 previous results. Similarly, we only see the operation + and not the operation *. Let's see if it becomes clearer why this is the case...
