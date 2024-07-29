# %%
# Find the deriv. of 2x at x=3
class Term:
    def __init__(self, type, **kwargs) -> None:
        self.type = type
        if type == "scalar":
            self.value = kwargs["value"]
        elif type == "exp":
            self.power = kwargs["power"]
        elif type == "prod":
            self.u = kwargs["u"]
            self.v = kwargs["v"]

    def _power_rule(self, evaluated_at):
        return self.power * evaluated_at ** (self.power - 1)

    def _scalar_rule(self):
        return 0

    def _product_rule(self, evaluated_at):
        return self.u.evaluate_deriv(evaluated_at) * self.v.evaluate(
            evaluated_at
        ) + self.u.evaluate(evaluated_at) * self.v.evaluate_deriv(evaluated_at)

    def evaluate(self, evaluated_at):
        if self.type == "scalar":
            return self.value
        elif self.type == "exp":
            return evaluated_at**self.power
        elif self.type == "prod":
            return self.u.evaluate(evaluated_at) * self.v.evaluate(evaluated_at)

    def evaluate_deriv(self, evaluated_at=None):
        if self.type == "scalar":
            return self._scalar_rule()
        elif self.type == "exp":
            return self._power_rule(evaluated_at)
        elif self.type == "prod":
            return self._product_rule(evaluated_at)


my_scalar = Term(type="scalar", value=2)
my_exp = Term(type="exp", power=2)
my_prod = Term(type="prod", u=my_scalar, v=my_exp)
my_super_prod = Term(type="prod", u=my_prod, v=my_exp)

# %%
my_super_prod.evaluate_deriv(3)
