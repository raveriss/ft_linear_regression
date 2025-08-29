"""Basic linear regression helpers."""

from __future__ import annotations
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x_estimatePrice__mutmut_orig(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) + float(theta1) * float(x)


def x_estimatePrice__mutmut_1(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) - float(theta1) * float(x)


def x_estimatePrice__mutmut_2(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(None) + float(theta1) * float(x)


def x_estimatePrice__mutmut_3(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) + float(theta1) / float(x)


def x_estimatePrice__mutmut_4(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) + float(None) * float(x)


def x_estimatePrice__mutmut_5(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) + float(theta1) * float(None)

x_estimatePrice__mutmut_mutants : ClassVar[MutantDict] = {
'x_estimatePrice__mutmut_1': x_estimatePrice__mutmut_1, 
    'x_estimatePrice__mutmut_2': x_estimatePrice__mutmut_2, 
    'x_estimatePrice__mutmut_3': x_estimatePrice__mutmut_3, 
    'x_estimatePrice__mutmut_4': x_estimatePrice__mutmut_4, 
    'x_estimatePrice__mutmut_5': x_estimatePrice__mutmut_5
}

def estimatePrice(*args, **kwargs):
    result = _mutmut_trampoline(x_estimatePrice__mutmut_orig, x_estimatePrice__mutmut_mutants, args, kwargs)
    return result 

estimatePrice.__signature__ = _mutmut_signature(x_estimatePrice__mutmut_orig)
x_estimatePrice__mutmut_orig.__name__ = 'x_estimatePrice'


def x_estimate_price__mutmut_orig(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, theta0, theta1)


def x_estimate_price__mutmut_1(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(None, theta0, theta1)


def x_estimate_price__mutmut_2(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, None, theta1)


def x_estimate_price__mutmut_3(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, theta0, None)


def x_estimate_price__mutmut_4(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(theta0, theta1)


def x_estimate_price__mutmut_5(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, theta1)


def x_estimate_price__mutmut_6(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, theta0, )

x_estimate_price__mutmut_mutants : ClassVar[MutantDict] = {
'x_estimate_price__mutmut_1': x_estimate_price__mutmut_1, 
    'x_estimate_price__mutmut_2': x_estimate_price__mutmut_2, 
    'x_estimate_price__mutmut_3': x_estimate_price__mutmut_3, 
    'x_estimate_price__mutmut_4': x_estimate_price__mutmut_4, 
    'x_estimate_price__mutmut_5': x_estimate_price__mutmut_5, 
    'x_estimate_price__mutmut_6': x_estimate_price__mutmut_6
}

def estimate_price(*args, **kwargs):
    result = _mutmut_trampoline(x_estimate_price__mutmut_orig, x_estimate_price__mutmut_mutants, args, kwargs)
    return result 

estimate_price.__signature__ = _mutmut_signature(x_estimate_price__mutmut_orig)
x_estimate_price__mutmut_orig.__name__ = 'x_estimate_price'
