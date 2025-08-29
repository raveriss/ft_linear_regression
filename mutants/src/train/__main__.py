"""Command-line entry point for the train package."""

# pragma: no mutate
from __future__ import annotations

import argparse

from .train import gradient_descent, read_data, save_theta
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


def x__alpha_type__mutmut_orig(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_1(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = None
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_2(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(None)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_3(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            None
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_4(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "XXalpha must be a floating point numberXX"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_5(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "ALPHA MUST BE A FLOATING POINT NUMBER"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_6(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_7(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 1 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_8(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 <= alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_9(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha < 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_10(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 2:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def x__alpha_type__mutmut_11(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError(None)
    return alpha


def x__alpha_type__mutmut_12(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("XXalpha must be in the range (0, 1]XX")
    return alpha


def x__alpha_type__mutmut_13(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("ALPHA MUST BE IN THE RANGE (0, 1]")
    return alpha

x__alpha_type__mutmut_mutants : ClassVar[MutantDict] = {
'x__alpha_type__mutmut_1': x__alpha_type__mutmut_1, 
    'x__alpha_type__mutmut_2': x__alpha_type__mutmut_2, 
    'x__alpha_type__mutmut_3': x__alpha_type__mutmut_3, 
    'x__alpha_type__mutmut_4': x__alpha_type__mutmut_4, 
    'x__alpha_type__mutmut_5': x__alpha_type__mutmut_5, 
    'x__alpha_type__mutmut_6': x__alpha_type__mutmut_6, 
    'x__alpha_type__mutmut_7': x__alpha_type__mutmut_7, 
    'x__alpha_type__mutmut_8': x__alpha_type__mutmut_8, 
    'x__alpha_type__mutmut_9': x__alpha_type__mutmut_9, 
    'x__alpha_type__mutmut_10': x__alpha_type__mutmut_10, 
    'x__alpha_type__mutmut_11': x__alpha_type__mutmut_11, 
    'x__alpha_type__mutmut_12': x__alpha_type__mutmut_12, 
    'x__alpha_type__mutmut_13': x__alpha_type__mutmut_13
}

def _alpha_type(*args, **kwargs):
    result = _mutmut_trampoline(x__alpha_type__mutmut_orig, x__alpha_type__mutmut_mutants, args, kwargs)
    return result 

_alpha_type.__signature__ = _mutmut_signature(x__alpha_type__mutmut_orig)
x__alpha_type__mutmut_orig.__name__ = 'x__alpha_type'


def x__iters_type__mutmut_orig(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_1(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = None
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_2(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(None)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_3(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(None) from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_4(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("XXiters must be a positive integerXX") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_5(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("ITERS MUST BE A POSITIVE INTEGER") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_6(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters < 0:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_7(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 1:
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    return iters


def x__iters_type__mutmut_8(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError(None)
    return iters


def x__iters_type__mutmut_9(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("XXiters must be a positive integerXX")
    return iters


def x__iters_type__mutmut_10(value: str) -> int:
    """Return ``value`` as a positive integer."""

    try:
        iters = int(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    if iters <= 0:
        raise argparse.ArgumentTypeError("ITERS MUST BE A POSITIVE INTEGER")
    return iters

x__iters_type__mutmut_mutants : ClassVar[MutantDict] = {
'x__iters_type__mutmut_1': x__iters_type__mutmut_1, 
    'x__iters_type__mutmut_2': x__iters_type__mutmut_2, 
    'x__iters_type__mutmut_3': x__iters_type__mutmut_3, 
    'x__iters_type__mutmut_4': x__iters_type__mutmut_4, 
    'x__iters_type__mutmut_5': x__iters_type__mutmut_5, 
    'x__iters_type__mutmut_6': x__iters_type__mutmut_6, 
    'x__iters_type__mutmut_7': x__iters_type__mutmut_7, 
    'x__iters_type__mutmut_8': x__iters_type__mutmut_8, 
    'x__iters_type__mutmut_9': x__iters_type__mutmut_9, 
    'x__iters_type__mutmut_10': x__iters_type__mutmut_10
}

def _iters_type(*args, **kwargs):
    result = _mutmut_trampoline(x__iters_type__mutmut_orig, x__iters_type__mutmut_mutants, args, kwargs)
    return result 

_iters_type.__signature__ = _mutmut_signature(x__iters_type__mutmut_orig)
x__iters_type__mutmut_orig.__name__ = 'x__iters_type'


def x_build_parser__mutmut_orig() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_1() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = None  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_2() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description=None,
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_3() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="XXTrain the linear regression modelXX",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_4() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_5() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="TRAIN THE LINEAR REGRESSION MODEL",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_6() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        None,
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_7() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=None,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_8() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help=None,
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_9() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_10() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_11() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_12() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "XX--dataXX",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_13() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--DATA",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_14() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=False,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_15() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="XXpath to training data CSVXX",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_16() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data csv",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_17() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="PATH TO TRAINING DATA CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_18() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        None,
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_19() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=None,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_20() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=None,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_21() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help=None,
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_22() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_23() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_24() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_25() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_26() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "XX--alphaXX",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_27() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--ALPHA",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_28() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=1.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_29() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="XXlearning rate (0 < alpha <= 1)XX",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_30() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="LEARNING RATE (0 < ALPHA <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_31() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        None,
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_32() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=None,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_33() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=None,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_34() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help=None,
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_35() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_36() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_37() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_38() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_39() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "XX--itersXX",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_40() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--ITERS",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_41() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1001,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_42() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="XXnumber of iterationsXX",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_43() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="NUMBER OF ITERATIONS",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_44() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        None,
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_45() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default=None,
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_46() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help=None,
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_47() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_48() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_49() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_50() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "XX--thetaXX",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_51() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--THETA",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_52() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="XXtheta.jsonXX",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_53() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="THETA.JSON",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_54() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="XXpath to theta JSONXX",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_55() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta json",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def x_build_parser__mutmut_56() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="PATH TO THETA JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate

x_build_parser__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_parser__mutmut_1': x_build_parser__mutmut_1, 
    'x_build_parser__mutmut_2': x_build_parser__mutmut_2, 
    'x_build_parser__mutmut_3': x_build_parser__mutmut_3, 
    'x_build_parser__mutmut_4': x_build_parser__mutmut_4, 
    'x_build_parser__mutmut_5': x_build_parser__mutmut_5, 
    'x_build_parser__mutmut_6': x_build_parser__mutmut_6, 
    'x_build_parser__mutmut_7': x_build_parser__mutmut_7, 
    'x_build_parser__mutmut_8': x_build_parser__mutmut_8, 
    'x_build_parser__mutmut_9': x_build_parser__mutmut_9, 
    'x_build_parser__mutmut_10': x_build_parser__mutmut_10, 
    'x_build_parser__mutmut_11': x_build_parser__mutmut_11, 
    'x_build_parser__mutmut_12': x_build_parser__mutmut_12, 
    'x_build_parser__mutmut_13': x_build_parser__mutmut_13, 
    'x_build_parser__mutmut_14': x_build_parser__mutmut_14, 
    'x_build_parser__mutmut_15': x_build_parser__mutmut_15, 
    'x_build_parser__mutmut_16': x_build_parser__mutmut_16, 
    'x_build_parser__mutmut_17': x_build_parser__mutmut_17, 
    'x_build_parser__mutmut_18': x_build_parser__mutmut_18, 
    'x_build_parser__mutmut_19': x_build_parser__mutmut_19, 
    'x_build_parser__mutmut_20': x_build_parser__mutmut_20, 
    'x_build_parser__mutmut_21': x_build_parser__mutmut_21, 
    'x_build_parser__mutmut_22': x_build_parser__mutmut_22, 
    'x_build_parser__mutmut_23': x_build_parser__mutmut_23, 
    'x_build_parser__mutmut_24': x_build_parser__mutmut_24, 
    'x_build_parser__mutmut_25': x_build_parser__mutmut_25, 
    'x_build_parser__mutmut_26': x_build_parser__mutmut_26, 
    'x_build_parser__mutmut_27': x_build_parser__mutmut_27, 
    'x_build_parser__mutmut_28': x_build_parser__mutmut_28, 
    'x_build_parser__mutmut_29': x_build_parser__mutmut_29, 
    'x_build_parser__mutmut_30': x_build_parser__mutmut_30, 
    'x_build_parser__mutmut_31': x_build_parser__mutmut_31, 
    'x_build_parser__mutmut_32': x_build_parser__mutmut_32, 
    'x_build_parser__mutmut_33': x_build_parser__mutmut_33, 
    'x_build_parser__mutmut_34': x_build_parser__mutmut_34, 
    'x_build_parser__mutmut_35': x_build_parser__mutmut_35, 
    'x_build_parser__mutmut_36': x_build_parser__mutmut_36, 
    'x_build_parser__mutmut_37': x_build_parser__mutmut_37, 
    'x_build_parser__mutmut_38': x_build_parser__mutmut_38, 
    'x_build_parser__mutmut_39': x_build_parser__mutmut_39, 
    'x_build_parser__mutmut_40': x_build_parser__mutmut_40, 
    'x_build_parser__mutmut_41': x_build_parser__mutmut_41, 
    'x_build_parser__mutmut_42': x_build_parser__mutmut_42, 
    'x_build_parser__mutmut_43': x_build_parser__mutmut_43, 
    'x_build_parser__mutmut_44': x_build_parser__mutmut_44, 
    'x_build_parser__mutmut_45': x_build_parser__mutmut_45, 
    'x_build_parser__mutmut_46': x_build_parser__mutmut_46, 
    'x_build_parser__mutmut_47': x_build_parser__mutmut_47, 
    'x_build_parser__mutmut_48': x_build_parser__mutmut_48, 
    'x_build_parser__mutmut_49': x_build_parser__mutmut_49, 
    'x_build_parser__mutmut_50': x_build_parser__mutmut_50, 
    'x_build_parser__mutmut_51': x_build_parser__mutmut_51, 
    'x_build_parser__mutmut_52': x_build_parser__mutmut_52, 
    'x_build_parser__mutmut_53': x_build_parser__mutmut_53, 
    'x_build_parser__mutmut_54': x_build_parser__mutmut_54, 
    'x_build_parser__mutmut_55': x_build_parser__mutmut_55, 
    'x_build_parser__mutmut_56': x_build_parser__mutmut_56
}

def build_parser(*args, **kwargs):
    result = _mutmut_trampoline(x_build_parser__mutmut_orig, x_build_parser__mutmut_mutants, args, kwargs)
    return result 

build_parser.__signature__ = _mutmut_signature(x_build_parser__mutmut_orig)
x_build_parser__mutmut_orig.__name__ = 'x_build_parser'


def x_main__mutmut_orig(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_1(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = None
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_2(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(None)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_3(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = None
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_4(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(None)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_5(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(None)
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_6(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 3

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_7(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = None
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_8(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = None
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_9(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(None), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_10(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(None)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_11(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = None

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_12(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(None), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_13(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(None)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_14(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = None

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_15(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) * km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_16(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km + min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_17(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) * price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_18(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price + min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_19(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = None
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_20(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(None, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_21(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, None, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_22(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, None)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_23(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_24(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_25(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, )
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_26(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = None
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_27(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range * km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_28(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n / price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_29(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        None,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_30(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        None,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_31(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        None,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_32(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        None,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_33(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        None,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_34(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        None,
        max_price,
    )
    return 0


def x_main__mutmut_35(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        None,
    )
    return 0


def x_main__mutmut_36(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_37(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_38(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_39(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        max_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_40(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        min_price,
        max_price,
    )
    return 0


def x_main__mutmut_41(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        max_price,
    )
    return 0


def x_main__mutmut_42(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        )
    return 0


def x_main__mutmut_43(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    kms, prices = zip(*data)
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    return 1

x_main__mutmut_mutants : ClassVar[MutantDict] = {
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21, 
    'x_main__mutmut_22': x_main__mutmut_22, 
    'x_main__mutmut_23': x_main__mutmut_23, 
    'x_main__mutmut_24': x_main__mutmut_24, 
    'x_main__mutmut_25': x_main__mutmut_25, 
    'x_main__mutmut_26': x_main__mutmut_26, 
    'x_main__mutmut_27': x_main__mutmut_27, 
    'x_main__mutmut_28': x_main__mutmut_28, 
    'x_main__mutmut_29': x_main__mutmut_29, 
    'x_main__mutmut_30': x_main__mutmut_30, 
    'x_main__mutmut_31': x_main__mutmut_31, 
    'x_main__mutmut_32': x_main__mutmut_32, 
    'x_main__mutmut_33': x_main__mutmut_33, 
    'x_main__mutmut_34': x_main__mutmut_34, 
    'x_main__mutmut_35': x_main__mutmut_35, 
    'x_main__mutmut_36': x_main__mutmut_36, 
    'x_main__mutmut_37': x_main__mutmut_37, 
    'x_main__mutmut_38': x_main__mutmut_38, 
    'x_main__mutmut_39': x_main__mutmut_39, 
    'x_main__mutmut_40': x_main__mutmut_40, 
    'x_main__mutmut_41': x_main__mutmut_41, 
    'x_main__mutmut_42': x_main__mutmut_42, 
    'x_main__mutmut_43': x_main__mutmut_43
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
