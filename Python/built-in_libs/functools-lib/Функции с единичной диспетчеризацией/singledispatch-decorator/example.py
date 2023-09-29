from functools import singledispatch
from datetime import datetime
from numbers import Real


"""
    Единичная диспетчеризация начинается с определения функции, которая 
    будет использоваться по умолчанию для всех незарегистрированных типов. 
"""


@singledispatch
def report(value):
    return f"raw: {value}"


@report.register
def _(value: datetime):
    return f"dt: {value.isoformat()}"


@report.register
def _(value: complex):
    return f"complex: {value.real}{value.imag:+}j"


@report.register
def _(value: Real):
    return f"real: {value:f}"


"""
    Аннотации типов необязательны, но мы использовали их как элементы хорошего тона. 
    Если вы не хотите использовать аннотации типов, укажите регистрируемый тип в качестве аргумента метода register( )
"""


@report.register(complex)
def _(value):
    return f"complex: {value.real}{value.imag:+}j"


@report.register(Real)
def _(value):
    return f"real: {value:f}"
