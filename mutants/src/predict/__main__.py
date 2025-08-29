"""Command-line entry point for the predict package."""

# pragma: no mutate
from __future__ import annotations

from .predict import parse_args, predict_price
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


def x_main__mutmut_orig(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_1(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = None
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_2(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(None)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_3(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = None
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_4(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(None, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_5(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, None)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_6(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_7(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, )
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_8(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 2  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_9(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print(None)
    return 0


def x_main__mutmut_10(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("XX0XX" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_11(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price != 0 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_12(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 1 else f"Predicted price: {price:.2f} €")
    return 0


def x_main__mutmut_13(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
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
    'x_main__mutmut_13': x_main__mutmut_13
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
