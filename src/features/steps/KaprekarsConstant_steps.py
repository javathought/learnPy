from behave import *

from coderbyte.kaprekars_constant import KaprekarsConstant


@given("Le nombre {number:d}")
def step_impl(context, number):
    """
    :type context: behave.runner.Context
    """
    context.number = number


@when("on appelle la fonction KaprekarsConstant")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.actual = KaprekarsConstant(context.number)


@then("le nombre d'itérations est {expected:d}")
def step_impl(context, expected):
    """
    :type context: behave.runner.Context
    """
    assert context.actual == expected