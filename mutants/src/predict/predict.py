"""Prediction utilities for the linear regression project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from linear_regression import estimatePrice
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


def x_build_parser__mutmut_orig() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_1() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = None
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_2() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description=None,
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_3() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="XXPredict a car price from mileageXX",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_4() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_5() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="PREDICT A CAR PRICE FROM MILEAGE",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_6() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument(None, nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_7() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs=None, type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_8() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=None, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_9() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help=None)
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_10() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument(nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_11() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_12() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_13() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, )
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_14() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("XXkmXX", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_15() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("KM", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_16() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="XX?XX", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_17() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="XXmileage in kilometersXX")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_18() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="MILEAGE IN KILOMETERS")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_19() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument(None, default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_20() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default=None, help="path to theta JSON")
    return parser


def x_build_parser__mutmut_21() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help=None)
    return parser


def x_build_parser__mutmut_22() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument(default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_23() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_24() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", )
    return parser


def x_build_parser__mutmut_25() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("XX--thetaXX", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_26() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--THETA", default="theta.json", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_27() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="XXtheta.jsonXX", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_28() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="THETA.JSON", help="path to theta JSON")
    return parser


def x_build_parser__mutmut_29() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="XXpath to theta JSONXX")
    return parser


def x_build_parser__mutmut_30() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta json")
    return parser


def x_build_parser__mutmut_31() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="PATH TO THETA JSON")
    return parser

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
    'x_build_parser__mutmut_31': x_build_parser__mutmut_31
}

def build_parser(*args, **kwargs):
    result = _mutmut_trampoline(x_build_parser__mutmut_orig, x_build_parser__mutmut_mutants, args, kwargs)
    return result 

build_parser.__signature__ = _mutmut_signature(x_build_parser__mutmut_orig)
x_build_parser__mutmut_orig.__name__ = 'x_build_parser'


def x__prompt_mileage__mutmut_orig() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_1() -> float:
    """Interactively request a valid mileage from the user."""

    while False:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_2() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = None
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_3() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(None)
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_4() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input(None))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_5() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("XXEnter mileage: XX"))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_6() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_7() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("ENTER MILEAGE: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_8() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print(None)
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_9() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("XXInvalid mileage. Please enter a number.XX")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_10() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("invalid mileage. please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_11() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("INVALID MILEAGE. PLEASE ENTER A NUMBER.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_12() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            break
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_13() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km <= 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_14() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 1:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_15() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print(None)
            continue
        return km


def x__prompt_mileage__mutmut_16() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("XXInvalid mileage. Must be a non-negative number.XX")
            continue
        return km


def x__prompt_mileage__mutmut_17() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("invalid mileage. must be a non-negative number.")
            continue
        return km


def x__prompt_mileage__mutmut_18() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("INVALID MILEAGE. MUST BE A NON-NEGATIVE NUMBER.")
            continue
        return km


def x__prompt_mileage__mutmut_19() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            break
        return km

x__prompt_mileage__mutmut_mutants : ClassVar[MutantDict] = {
'x__prompt_mileage__mutmut_1': x__prompt_mileage__mutmut_1, 
    'x__prompt_mileage__mutmut_2': x__prompt_mileage__mutmut_2, 
    'x__prompt_mileage__mutmut_3': x__prompt_mileage__mutmut_3, 
    'x__prompt_mileage__mutmut_4': x__prompt_mileage__mutmut_4, 
    'x__prompt_mileage__mutmut_5': x__prompt_mileage__mutmut_5, 
    'x__prompt_mileage__mutmut_6': x__prompt_mileage__mutmut_6, 
    'x__prompt_mileage__mutmut_7': x__prompt_mileage__mutmut_7, 
    'x__prompt_mileage__mutmut_8': x__prompt_mileage__mutmut_8, 
    'x__prompt_mileage__mutmut_9': x__prompt_mileage__mutmut_9, 
    'x__prompt_mileage__mutmut_10': x__prompt_mileage__mutmut_10, 
    'x__prompt_mileage__mutmut_11': x__prompt_mileage__mutmut_11, 
    'x__prompt_mileage__mutmut_12': x__prompt_mileage__mutmut_12, 
    'x__prompt_mileage__mutmut_13': x__prompt_mileage__mutmut_13, 
    'x__prompt_mileage__mutmut_14': x__prompt_mileage__mutmut_14, 
    'x__prompt_mileage__mutmut_15': x__prompt_mileage__mutmut_15, 
    'x__prompt_mileage__mutmut_16': x__prompt_mileage__mutmut_16, 
    'x__prompt_mileage__mutmut_17': x__prompt_mileage__mutmut_17, 
    'x__prompt_mileage__mutmut_18': x__prompt_mileage__mutmut_18, 
    'x__prompt_mileage__mutmut_19': x__prompt_mileage__mutmut_19
}

def _prompt_mileage(*args, **kwargs):
    result = _mutmut_trampoline(x__prompt_mileage__mutmut_orig, x__prompt_mileage__mutmut_mutants, args, kwargs)
    return result 

_prompt_mileage.__signature__ = _mutmut_signature(x__prompt_mileage__mutmut_orig)
x__prompt_mileage__mutmut_orig.__name__ = 'x__prompt_mileage'


def x_parse_args__mutmut_orig(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_1(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = None
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_2(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = None
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_3(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(None)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_4(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print(None)
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_5(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("XXToo many argumentsXX")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_6(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_7(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("TOO MANY ARGUMENTS")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_8(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print(None)
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_9(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("XXUsage:XX")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_10(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_11(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("USAGE:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_12(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print(None)
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_13(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("XX  make predict            # interactiveXX")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_14(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  MAKE PREDICT            # INTERACTIVE")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_15(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print(None)
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_16(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("XX  make predict <km>       # direct predictionXX")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_17(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  MAKE PREDICT <KM>       # DIRECT PREDICTION")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_18(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print(None)
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_19(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("XX  make train              # train the modelXX")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_20(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  MAKE TRAIN              # TRAIN THE MODEL")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_21(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(None)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_22(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(3)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_23(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = None
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_24(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is not None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_25(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = None
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_26(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is not None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_27(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 1.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_28(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km <= 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_29(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 1:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_30(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print(None)
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_31(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("XXERROR: invalid mileage (must be a non-negative number)XX")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_32(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("error: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_33(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: INVALID MILEAGE (MUST BE A NON-NEGATIVE NUMBER)")
        raise SystemExit(2)
    return km, args.theta


def x_parse_args__mutmut_34(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(None)
    return km, args.theta


def x_parse_args__mutmut_35(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    parser = build_parser()
    args, extra = parser.parse_known_args(argv)
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(3)
    return km, args.theta

x_parse_args__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_args__mutmut_1': x_parse_args__mutmut_1, 
    'x_parse_args__mutmut_2': x_parse_args__mutmut_2, 
    'x_parse_args__mutmut_3': x_parse_args__mutmut_3, 
    'x_parse_args__mutmut_4': x_parse_args__mutmut_4, 
    'x_parse_args__mutmut_5': x_parse_args__mutmut_5, 
    'x_parse_args__mutmut_6': x_parse_args__mutmut_6, 
    'x_parse_args__mutmut_7': x_parse_args__mutmut_7, 
    'x_parse_args__mutmut_8': x_parse_args__mutmut_8, 
    'x_parse_args__mutmut_9': x_parse_args__mutmut_9, 
    'x_parse_args__mutmut_10': x_parse_args__mutmut_10, 
    'x_parse_args__mutmut_11': x_parse_args__mutmut_11, 
    'x_parse_args__mutmut_12': x_parse_args__mutmut_12, 
    'x_parse_args__mutmut_13': x_parse_args__mutmut_13, 
    'x_parse_args__mutmut_14': x_parse_args__mutmut_14, 
    'x_parse_args__mutmut_15': x_parse_args__mutmut_15, 
    'x_parse_args__mutmut_16': x_parse_args__mutmut_16, 
    'x_parse_args__mutmut_17': x_parse_args__mutmut_17, 
    'x_parse_args__mutmut_18': x_parse_args__mutmut_18, 
    'x_parse_args__mutmut_19': x_parse_args__mutmut_19, 
    'x_parse_args__mutmut_20': x_parse_args__mutmut_20, 
    'x_parse_args__mutmut_21': x_parse_args__mutmut_21, 
    'x_parse_args__mutmut_22': x_parse_args__mutmut_22, 
    'x_parse_args__mutmut_23': x_parse_args__mutmut_23, 
    'x_parse_args__mutmut_24': x_parse_args__mutmut_24, 
    'x_parse_args__mutmut_25': x_parse_args__mutmut_25, 
    'x_parse_args__mutmut_26': x_parse_args__mutmut_26, 
    'x_parse_args__mutmut_27': x_parse_args__mutmut_27, 
    'x_parse_args__mutmut_28': x_parse_args__mutmut_28, 
    'x_parse_args__mutmut_29': x_parse_args__mutmut_29, 
    'x_parse_args__mutmut_30': x_parse_args__mutmut_30, 
    'x_parse_args__mutmut_31': x_parse_args__mutmut_31, 
    'x_parse_args__mutmut_32': x_parse_args__mutmut_32, 
    'x_parse_args__mutmut_33': x_parse_args__mutmut_33, 
    'x_parse_args__mutmut_34': x_parse_args__mutmut_34, 
    'x_parse_args__mutmut_35': x_parse_args__mutmut_35
}

def parse_args(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_args__mutmut_orig, x_parse_args__mutmut_mutants, args, kwargs)
    return result 

parse_args.__signature__ = _mutmut_signature(x_parse_args__mutmut_orig)
x_parse_args__mutmut_orig.__name__ = 'x_parse_args'


def x__read_theta__mutmut_orig(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(theta_path.read_text())
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(2)


def x__read_theta__mutmut_1(theta_path: Path) -> dict[str, Any]:
    try:
        raw = None
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(2)


def x__read_theta__mutmut_2(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(None)
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(2)


def x__read_theta__mutmut_3(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(theta_path.read_text())
        if isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(2)


def x__read_theta__mutmut_4(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(theta_path.read_text())
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(None)
        raise SystemExit(2)


def x__read_theta__mutmut_5(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(theta_path.read_text())
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(None)


def x__read_theta__mutmut_6(theta_path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(theta_path.read_text())
        if not isinstance(raw, dict):
            raise ValueError
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(3)

x__read_theta__mutmut_mutants : ClassVar[MutantDict] = {
'x__read_theta__mutmut_1': x__read_theta__mutmut_1, 
    'x__read_theta__mutmut_2': x__read_theta__mutmut_2, 
    'x__read_theta__mutmut_3': x__read_theta__mutmut_3, 
    'x__read_theta__mutmut_4': x__read_theta__mutmut_4, 
    'x__read_theta__mutmut_5': x__read_theta__mutmut_5, 
    'x__read_theta__mutmut_6': x__read_theta__mutmut_6
}

def _read_theta(*args, **kwargs):
    result = _mutmut_trampoline(x__read_theta__mutmut_orig, x__read_theta__mutmut_mutants, args, kwargs)
    return result 

_read_theta.__signature__ = _mutmut_signature(x__read_theta__mutmut_orig)
x__read_theta__mutmut_orig.__name__ = 'x__read_theta'


def x__parse_float__mutmut_orig(value: Any, theta_path: Path) -> float:
    if theta_path is None:
        raise AssertionError
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(2)


def x__parse_float__mutmut_1(value: Any, theta_path: Path) -> float:
    if theta_path is not None:
        raise AssertionError
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(2)


def x__parse_float__mutmut_2(value: Any, theta_path: Path) -> float:
    if theta_path is None:
        raise AssertionError
    try:
        return float(None)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(2)


def x__parse_float__mutmut_3(value: Any, theta_path: Path) -> float:
    if theta_path is None:
        raise AssertionError
    try:
        return float(value)
    except (TypeError, ValueError):
        print(None)
        raise SystemExit(2)


def x__parse_float__mutmut_4(value: Any, theta_path: Path) -> float:
    if theta_path is None:
        raise AssertionError
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(None)


def x__parse_float__mutmut_5(value: Any, theta_path: Path) -> float:
    if theta_path is None:
        raise AssertionError
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(3)

x__parse_float__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse_float__mutmut_1': x__parse_float__mutmut_1, 
    'x__parse_float__mutmut_2': x__parse_float__mutmut_2, 
    'x__parse_float__mutmut_3': x__parse_float__mutmut_3, 
    'x__parse_float__mutmut_4': x__parse_float__mutmut_4, 
    'x__parse_float__mutmut_5': x__parse_float__mutmut_5
}

def _parse_float(*args, **kwargs):
    result = _mutmut_trampoline(x__parse_float__mutmut_orig, x__parse_float__mutmut_mutants, args, kwargs)
    return result 

_parse_float.__signature__ = _mutmut_signature(x__parse_float__mutmut_orig)
x__parse_float__mutmut_orig.__name__ = 'x__parse_float'


def x__parse_optional_float__mutmut_orig(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is None else _parse_float(value, theta_path)


def x__parse_optional_float__mutmut_1(value: Any, theta_path: Path) -> float | None:
    if theta_path is not None:
        raise AssertionError
    return None if value is None else _parse_float(value, theta_path)


def x__parse_optional_float__mutmut_2(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is not None else _parse_float(value, theta_path)


def x__parse_optional_float__mutmut_3(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is None else _parse_float(None, theta_path)


def x__parse_optional_float__mutmut_4(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is None else _parse_float(value, None)


def x__parse_optional_float__mutmut_5(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is None else _parse_float(theta_path)


def x__parse_optional_float__mutmut_6(value: Any, theta_path: Path) -> float | None:
    if theta_path is None:
        raise AssertionError
    return None if value is None else _parse_float(value, )

x__parse_optional_float__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse_optional_float__mutmut_1': x__parse_optional_float__mutmut_1, 
    'x__parse_optional_float__mutmut_2': x__parse_optional_float__mutmut_2, 
    'x__parse_optional_float__mutmut_3': x__parse_optional_float__mutmut_3, 
    'x__parse_optional_float__mutmut_4': x__parse_optional_float__mutmut_4, 
    'x__parse_optional_float__mutmut_5': x__parse_optional_float__mutmut_5, 
    'x__parse_optional_float__mutmut_6': x__parse_optional_float__mutmut_6
}

def _parse_optional_float(*args, **kwargs):
    result = _mutmut_trampoline(x__parse_optional_float__mutmut_orig, x__parse_optional_float__mutmut_mutants, args, kwargs)
    return result 

_parse_optional_float.__signature__ = _mutmut_signature(x__parse_optional_float__mutmut_orig)
x__parse_optional_float__mutmut_orig.__name__ = 'x__parse_optional_float'


def x_load_theta__mutmut_orig(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_1(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = None
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_2(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(None)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_3(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_4(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 1.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_5(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 1.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_6(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = None
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_7(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(None)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_8(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = None
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_9(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(None, theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_10(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), None)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_11(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_12(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), )
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_13(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get(None, 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_14(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", None), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_15(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get(0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_16(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", ), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_17(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("XXtheta0XX", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_18(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("THETA0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_19(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 1.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_20(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = None
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_21(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(None, theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_22(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), None)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_23(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_24(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), )
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_25(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get(None, 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_26(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", None), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_27(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get(0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_28(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", ), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_29(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("XXtheta1XX", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_30(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("THETA1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_31(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 1.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_32(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = None
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_33(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(None, theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_34(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), None)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_35(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_36(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), )
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_37(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get(None), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_38(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("XXmin_kmXX"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_39(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("MIN_KM"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_40(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = None
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_41(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(None, theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_42(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), None)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_43(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_44(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), )
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_45(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get(None), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_46(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("XXmax_kmXX"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_47(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("MAX_KM"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_48(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = None
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_49(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(None, theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_50(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), None)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_51(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_52(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), )
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_53(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get(None), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_54(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("XXmin_priceXX"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_55(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("MIN_PRICE"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_56(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = None
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_57(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(None, theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_58(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), None)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_59(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_60(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), )
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_61(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get(None), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_62(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("XXmax_priceXX"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def x_load_theta__mutmut_63(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("MAX_PRICE"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price

x_load_theta__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_theta__mutmut_1': x_load_theta__mutmut_1, 
    'x_load_theta__mutmut_2': x_load_theta__mutmut_2, 
    'x_load_theta__mutmut_3': x_load_theta__mutmut_3, 
    'x_load_theta__mutmut_4': x_load_theta__mutmut_4, 
    'x_load_theta__mutmut_5': x_load_theta__mutmut_5, 
    'x_load_theta__mutmut_6': x_load_theta__mutmut_6, 
    'x_load_theta__mutmut_7': x_load_theta__mutmut_7, 
    'x_load_theta__mutmut_8': x_load_theta__mutmut_8, 
    'x_load_theta__mutmut_9': x_load_theta__mutmut_9, 
    'x_load_theta__mutmut_10': x_load_theta__mutmut_10, 
    'x_load_theta__mutmut_11': x_load_theta__mutmut_11, 
    'x_load_theta__mutmut_12': x_load_theta__mutmut_12, 
    'x_load_theta__mutmut_13': x_load_theta__mutmut_13, 
    'x_load_theta__mutmut_14': x_load_theta__mutmut_14, 
    'x_load_theta__mutmut_15': x_load_theta__mutmut_15, 
    'x_load_theta__mutmut_16': x_load_theta__mutmut_16, 
    'x_load_theta__mutmut_17': x_load_theta__mutmut_17, 
    'x_load_theta__mutmut_18': x_load_theta__mutmut_18, 
    'x_load_theta__mutmut_19': x_load_theta__mutmut_19, 
    'x_load_theta__mutmut_20': x_load_theta__mutmut_20, 
    'x_load_theta__mutmut_21': x_load_theta__mutmut_21, 
    'x_load_theta__mutmut_22': x_load_theta__mutmut_22, 
    'x_load_theta__mutmut_23': x_load_theta__mutmut_23, 
    'x_load_theta__mutmut_24': x_load_theta__mutmut_24, 
    'x_load_theta__mutmut_25': x_load_theta__mutmut_25, 
    'x_load_theta__mutmut_26': x_load_theta__mutmut_26, 
    'x_load_theta__mutmut_27': x_load_theta__mutmut_27, 
    'x_load_theta__mutmut_28': x_load_theta__mutmut_28, 
    'x_load_theta__mutmut_29': x_load_theta__mutmut_29, 
    'x_load_theta__mutmut_30': x_load_theta__mutmut_30, 
    'x_load_theta__mutmut_31': x_load_theta__mutmut_31, 
    'x_load_theta__mutmut_32': x_load_theta__mutmut_32, 
    'x_load_theta__mutmut_33': x_load_theta__mutmut_33, 
    'x_load_theta__mutmut_34': x_load_theta__mutmut_34, 
    'x_load_theta__mutmut_35': x_load_theta__mutmut_35, 
    'x_load_theta__mutmut_36': x_load_theta__mutmut_36, 
    'x_load_theta__mutmut_37': x_load_theta__mutmut_37, 
    'x_load_theta__mutmut_38': x_load_theta__mutmut_38, 
    'x_load_theta__mutmut_39': x_load_theta__mutmut_39, 
    'x_load_theta__mutmut_40': x_load_theta__mutmut_40, 
    'x_load_theta__mutmut_41': x_load_theta__mutmut_41, 
    'x_load_theta__mutmut_42': x_load_theta__mutmut_42, 
    'x_load_theta__mutmut_43': x_load_theta__mutmut_43, 
    'x_load_theta__mutmut_44': x_load_theta__mutmut_44, 
    'x_load_theta__mutmut_45': x_load_theta__mutmut_45, 
    'x_load_theta__mutmut_46': x_load_theta__mutmut_46, 
    'x_load_theta__mutmut_47': x_load_theta__mutmut_47, 
    'x_load_theta__mutmut_48': x_load_theta__mutmut_48, 
    'x_load_theta__mutmut_49': x_load_theta__mutmut_49, 
    'x_load_theta__mutmut_50': x_load_theta__mutmut_50, 
    'x_load_theta__mutmut_51': x_load_theta__mutmut_51, 
    'x_load_theta__mutmut_52': x_load_theta__mutmut_52, 
    'x_load_theta__mutmut_53': x_load_theta__mutmut_53, 
    'x_load_theta__mutmut_54': x_load_theta__mutmut_54, 
    'x_load_theta__mutmut_55': x_load_theta__mutmut_55, 
    'x_load_theta__mutmut_56': x_load_theta__mutmut_56, 
    'x_load_theta__mutmut_57': x_load_theta__mutmut_57, 
    'x_load_theta__mutmut_58': x_load_theta__mutmut_58, 
    'x_load_theta__mutmut_59': x_load_theta__mutmut_59, 
    'x_load_theta__mutmut_60': x_load_theta__mutmut_60, 
    'x_load_theta__mutmut_61': x_load_theta__mutmut_61, 
    'x_load_theta__mutmut_62': x_load_theta__mutmut_62, 
    'x_load_theta__mutmut_63': x_load_theta__mutmut_63
}

def load_theta(*args, **kwargs):
    result = _mutmut_trampoline(x_load_theta__mutmut_orig, x_load_theta__mutmut_mutants, args, kwargs)
    return result 

load_theta.__signature__ = _mutmut_signature(x_load_theta__mutmut_orig)
x_load_theta__mutmut_orig.__name__ = 'x_load_theta'


def x__warn_outside__mutmut_orig(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_1(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = None
    if min_val is None or max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_2(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None and max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_3(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is not None or max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_4(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is not None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_5(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_6(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if not (min_val < value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_7(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if not (min_val <= value < max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def x__warn_outside__mutmut_8(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(None)

x__warn_outside__mutmut_mutants : ClassVar[MutantDict] = {
'x__warn_outside__mutmut_1': x__warn_outside__mutmut_1, 
    'x__warn_outside__mutmut_2': x__warn_outside__mutmut_2, 
    'x__warn_outside__mutmut_3': x__warn_outside__mutmut_3, 
    'x__warn_outside__mutmut_4': x__warn_outside__mutmut_4, 
    'x__warn_outside__mutmut_5': x__warn_outside__mutmut_5, 
    'x__warn_outside__mutmut_6': x__warn_outside__mutmut_6, 
    'x__warn_outside__mutmut_7': x__warn_outside__mutmut_7, 
    'x__warn_outside__mutmut_8': x__warn_outside__mutmut_8
}

def _warn_outside(*args, **kwargs):
    result = _mutmut_trampoline(x__warn_outside__mutmut_orig, x__warn_outside__mutmut_mutants, args, kwargs)
    return result 

_warn_outside.__signature__ = _mutmut_signature(x__warn_outside__mutmut_orig)
x__warn_outside__mutmut_orig.__name__ = 'x__warn_outside'


def x_predict_price__mutmut_orig(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_1(km: float, theta_path: str = "XXtheta.jsonXX") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_2(km: float, theta_path: str = "THETA.JSON") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_3(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = None
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_4(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(None)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_5(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 or theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_6(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 != 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_7(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 1.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_8(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 != 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_9(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 1.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_10(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 1
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_11(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = None
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_12(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(None, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_13(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, None, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_14(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, None)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_15(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_16(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_17(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, )
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_18(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(None, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_19(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, None, "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_20(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), None)
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_21(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside((min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_22(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_23(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), )
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_24(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "XXmileageXX")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_25(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "MILEAGE")
    _warn_outside(price, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_26(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(None, (min_price, max_price), "price")
    return price


def x_predict_price__mutmut_27(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, None, "price")
    return price


def x_predict_price__mutmut_28(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), None)
    return price


def x_predict_price__mutmut_29(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside((min_price, max_price), "price")
    return price


def x_predict_price__mutmut_30(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, "price")
    return price


def x_predict_price__mutmut_31(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), )
    return price


def x_predict_price__mutmut_32(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "XXpriceXX")
    return price


def x_predict_price__mutmut_33(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "PRICE")
    return price

x_predict_price__mutmut_mutants : ClassVar[MutantDict] = {
'x_predict_price__mutmut_1': x_predict_price__mutmut_1, 
    'x_predict_price__mutmut_2': x_predict_price__mutmut_2, 
    'x_predict_price__mutmut_3': x_predict_price__mutmut_3, 
    'x_predict_price__mutmut_4': x_predict_price__mutmut_4, 
    'x_predict_price__mutmut_5': x_predict_price__mutmut_5, 
    'x_predict_price__mutmut_6': x_predict_price__mutmut_6, 
    'x_predict_price__mutmut_7': x_predict_price__mutmut_7, 
    'x_predict_price__mutmut_8': x_predict_price__mutmut_8, 
    'x_predict_price__mutmut_9': x_predict_price__mutmut_9, 
    'x_predict_price__mutmut_10': x_predict_price__mutmut_10, 
    'x_predict_price__mutmut_11': x_predict_price__mutmut_11, 
    'x_predict_price__mutmut_12': x_predict_price__mutmut_12, 
    'x_predict_price__mutmut_13': x_predict_price__mutmut_13, 
    'x_predict_price__mutmut_14': x_predict_price__mutmut_14, 
    'x_predict_price__mutmut_15': x_predict_price__mutmut_15, 
    'x_predict_price__mutmut_16': x_predict_price__mutmut_16, 
    'x_predict_price__mutmut_17': x_predict_price__mutmut_17, 
    'x_predict_price__mutmut_18': x_predict_price__mutmut_18, 
    'x_predict_price__mutmut_19': x_predict_price__mutmut_19, 
    'x_predict_price__mutmut_20': x_predict_price__mutmut_20, 
    'x_predict_price__mutmut_21': x_predict_price__mutmut_21, 
    'x_predict_price__mutmut_22': x_predict_price__mutmut_22, 
    'x_predict_price__mutmut_23': x_predict_price__mutmut_23, 
    'x_predict_price__mutmut_24': x_predict_price__mutmut_24, 
    'x_predict_price__mutmut_25': x_predict_price__mutmut_25, 
    'x_predict_price__mutmut_26': x_predict_price__mutmut_26, 
    'x_predict_price__mutmut_27': x_predict_price__mutmut_27, 
    'x_predict_price__mutmut_28': x_predict_price__mutmut_28, 
    'x_predict_price__mutmut_29': x_predict_price__mutmut_29, 
    'x_predict_price__mutmut_30': x_predict_price__mutmut_30, 
    'x_predict_price__mutmut_31': x_predict_price__mutmut_31, 
    'x_predict_price__mutmut_32': x_predict_price__mutmut_32, 
    'x_predict_price__mutmut_33': x_predict_price__mutmut_33
}

def predict_price(*args, **kwargs):
    result = _mutmut_trampoline(x_predict_price__mutmut_orig, x_predict_price__mutmut_mutants, args, kwargs)
    return result 

predict_price.__signature__ = _mutmut_signature(x_predict_price__mutmut_orig)
x_predict_price__mutmut_orig.__name__ = 'x_predict_price'


__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
