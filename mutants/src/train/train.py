"""Training data utilities for the linear regression project."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
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


def x__float_field__mutmut_orig(value: str, line_number: int) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def x__float_field__mutmut_1(value: str, line_number: int) -> float:
    try:
        result = None
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def x__float_field__mutmut_2(value: str, line_number: int) -> float:
    try:
        result = float(None)
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def x__float_field__mutmut_3(value: str, line_number: int) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(None) from None
    if math.isnan(result):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def x__float_field__mutmut_4(value: str, line_number: int) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(None):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def x__float_field__mutmut_5(value: str, line_number: int) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        raise ValueError(None)
    return result

x__float_field__mutmut_mutants : ClassVar[MutantDict] = {
'x__float_field__mutmut_1': x__float_field__mutmut_1, 
    'x__float_field__mutmut_2': x__float_field__mutmut_2, 
    'x__float_field__mutmut_3': x__float_field__mutmut_3, 
    'x__float_field__mutmut_4': x__float_field__mutmut_4, 
    'x__float_field__mutmut_5': x__float_field__mutmut_5
}

def _float_field(*args, **kwargs):
    result = _mutmut_trampoline(x__float_field__mutmut_orig, x__float_field__mutmut_mutants, args, kwargs)
    return result 

_float_field.__signature__ = _mutmut_signature(x__float_field__mutmut_orig)
x__float_field__mutmut_orig.__name__ = 'x__float_field'


def x__parse_row__mutmut_orig(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_1(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = None
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_2(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get(None)
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_3(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("XXkmXX")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_4(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("KM")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_5(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = None
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_6(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get(None)
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_7(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("XXpriceXX")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_8(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("PRICE")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_9(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None and price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_10(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is not None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_11(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is not None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_12(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(None)
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_13(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = None
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_14(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(None, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_15(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, None)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_16(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_17(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, )
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_18(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = None
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_19(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(None, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_20(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, None)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_21(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_22(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, )
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_23(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km <= 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_24(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 1:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_25(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(None)
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_26(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price <= 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_27(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 1:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def x__parse_row__mutmut_28(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(None)
    return km, price

x__parse_row__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse_row__mutmut_1': x__parse_row__mutmut_1, 
    'x__parse_row__mutmut_2': x__parse_row__mutmut_2, 
    'x__parse_row__mutmut_3': x__parse_row__mutmut_3, 
    'x__parse_row__mutmut_4': x__parse_row__mutmut_4, 
    'x__parse_row__mutmut_5': x__parse_row__mutmut_5, 
    'x__parse_row__mutmut_6': x__parse_row__mutmut_6, 
    'x__parse_row__mutmut_7': x__parse_row__mutmut_7, 
    'x__parse_row__mutmut_8': x__parse_row__mutmut_8, 
    'x__parse_row__mutmut_9': x__parse_row__mutmut_9, 
    'x__parse_row__mutmut_10': x__parse_row__mutmut_10, 
    'x__parse_row__mutmut_11': x__parse_row__mutmut_11, 
    'x__parse_row__mutmut_12': x__parse_row__mutmut_12, 
    'x__parse_row__mutmut_13': x__parse_row__mutmut_13, 
    'x__parse_row__mutmut_14': x__parse_row__mutmut_14, 
    'x__parse_row__mutmut_15': x__parse_row__mutmut_15, 
    'x__parse_row__mutmut_16': x__parse_row__mutmut_16, 
    'x__parse_row__mutmut_17': x__parse_row__mutmut_17, 
    'x__parse_row__mutmut_18': x__parse_row__mutmut_18, 
    'x__parse_row__mutmut_19': x__parse_row__mutmut_19, 
    'x__parse_row__mutmut_20': x__parse_row__mutmut_20, 
    'x__parse_row__mutmut_21': x__parse_row__mutmut_21, 
    'x__parse_row__mutmut_22': x__parse_row__mutmut_22, 
    'x__parse_row__mutmut_23': x__parse_row__mutmut_23, 
    'x__parse_row__mutmut_24': x__parse_row__mutmut_24, 
    'x__parse_row__mutmut_25': x__parse_row__mutmut_25, 
    'x__parse_row__mutmut_26': x__parse_row__mutmut_26, 
    'x__parse_row__mutmut_27': x__parse_row__mutmut_27, 
    'x__parse_row__mutmut_28': x__parse_row__mutmut_28
}

def _parse_row(*args, **kwargs):
    result = _mutmut_trampoline(x__parse_row__mutmut_orig, x__parse_row__mutmut_mutants, args, kwargs)
    return result 

_parse_row.__signature__ = _mutmut_signature(x__parse_row__mutmut_orig)
x__parse_row__mutmut_orig.__name__ = 'x__parse_row'


def x_read_data__mutmut_orig(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_1(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = None
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_2(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(None)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_3(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = None
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_4(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(None)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_5(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames == ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_6(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["XXkmXX", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_7(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["KM", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_8(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "XXpriceXX"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_9(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "PRICE"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_10(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError(None)
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_11(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("XXinvalid CSV format (expected columns: km,price)XX")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_12(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid csv format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_13(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("INVALID CSV FORMAT (EXPECTED COLUMNS: KM,PRICE)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_14(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = None
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_15(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(None, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_16(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, None) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_17(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_18(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, ) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_19(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(None, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_20(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=None)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_21(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_22(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, )]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_23(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=3)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_24(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(None) from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_25(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if rows:
        raise ValueError("no data rows found")
    return rows


def x_read_data__mutmut_26(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError(None)
    return rows


def x_read_data__mutmut_27(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("XXno data rows foundXX")
    return rows


def x_read_data__mutmut_28(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("NO DATA ROWS FOUND")
    return rows

x_read_data__mutmut_mutants : ClassVar[MutantDict] = {
'x_read_data__mutmut_1': x_read_data__mutmut_1, 
    'x_read_data__mutmut_2': x_read_data__mutmut_2, 
    'x_read_data__mutmut_3': x_read_data__mutmut_3, 
    'x_read_data__mutmut_4': x_read_data__mutmut_4, 
    'x_read_data__mutmut_5': x_read_data__mutmut_5, 
    'x_read_data__mutmut_6': x_read_data__mutmut_6, 
    'x_read_data__mutmut_7': x_read_data__mutmut_7, 
    'x_read_data__mutmut_8': x_read_data__mutmut_8, 
    'x_read_data__mutmut_9': x_read_data__mutmut_9, 
    'x_read_data__mutmut_10': x_read_data__mutmut_10, 
    'x_read_data__mutmut_11': x_read_data__mutmut_11, 
    'x_read_data__mutmut_12': x_read_data__mutmut_12, 
    'x_read_data__mutmut_13': x_read_data__mutmut_13, 
    'x_read_data__mutmut_14': x_read_data__mutmut_14, 
    'x_read_data__mutmut_15': x_read_data__mutmut_15, 
    'x_read_data__mutmut_16': x_read_data__mutmut_16, 
    'x_read_data__mutmut_17': x_read_data__mutmut_17, 
    'x_read_data__mutmut_18': x_read_data__mutmut_18, 
    'x_read_data__mutmut_19': x_read_data__mutmut_19, 
    'x_read_data__mutmut_20': x_read_data__mutmut_20, 
    'x_read_data__mutmut_21': x_read_data__mutmut_21, 
    'x_read_data__mutmut_22': x_read_data__mutmut_22, 
    'x_read_data__mutmut_23': x_read_data__mutmut_23, 
    'x_read_data__mutmut_24': x_read_data__mutmut_24, 
    'x_read_data__mutmut_25': x_read_data__mutmut_25, 
    'x_read_data__mutmut_26': x_read_data__mutmut_26, 
    'x_read_data__mutmut_27': x_read_data__mutmut_27, 
    'x_read_data__mutmut_28': x_read_data__mutmut_28
}

def read_data(*args, **kwargs):
    result = _mutmut_trampoline(x_read_data__mutmut_orig, x_read_data__mutmut_mutants, args, kwargs)
    return result 

read_data.__signature__ = _mutmut_signature(x_read_data__mutmut_orig)
x_read_data__mutmut_orig.__name__ = 'x_read_data'


def x_gradient_descent__mutmut_orig(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_1(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = None
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_2(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 1.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_3(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = None
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_4(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 1.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_5(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = None
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_6(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(None)
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_7(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(None):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_8(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = None
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_9(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) * m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_10(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum(None) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_11(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) + y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_12(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 - theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_13(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 / x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_14(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = None
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_15(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) * m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_16(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(None) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_17(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) / x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_18(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) + y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_19(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 - theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_20(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 / x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_21(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = None
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_22(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha / dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_23(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = None
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_24(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha / dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_25(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 = tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_26(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 += tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_27(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 = tmp_theta1
    return theta0, theta1


def x_gradient_descent__mutmut_28(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 += tmp_theta1
    return theta0, theta1

x_gradient_descent__mutmut_mutants : ClassVar[MutantDict] = {
'x_gradient_descent__mutmut_1': x_gradient_descent__mutmut_1, 
    'x_gradient_descent__mutmut_2': x_gradient_descent__mutmut_2, 
    'x_gradient_descent__mutmut_3': x_gradient_descent__mutmut_3, 
    'x_gradient_descent__mutmut_4': x_gradient_descent__mutmut_4, 
    'x_gradient_descent__mutmut_5': x_gradient_descent__mutmut_5, 
    'x_gradient_descent__mutmut_6': x_gradient_descent__mutmut_6, 
    'x_gradient_descent__mutmut_7': x_gradient_descent__mutmut_7, 
    'x_gradient_descent__mutmut_8': x_gradient_descent__mutmut_8, 
    'x_gradient_descent__mutmut_9': x_gradient_descent__mutmut_9, 
    'x_gradient_descent__mutmut_10': x_gradient_descent__mutmut_10, 
    'x_gradient_descent__mutmut_11': x_gradient_descent__mutmut_11, 
    'x_gradient_descent__mutmut_12': x_gradient_descent__mutmut_12, 
    'x_gradient_descent__mutmut_13': x_gradient_descent__mutmut_13, 
    'x_gradient_descent__mutmut_14': x_gradient_descent__mutmut_14, 
    'x_gradient_descent__mutmut_15': x_gradient_descent__mutmut_15, 
    'x_gradient_descent__mutmut_16': x_gradient_descent__mutmut_16, 
    'x_gradient_descent__mutmut_17': x_gradient_descent__mutmut_17, 
    'x_gradient_descent__mutmut_18': x_gradient_descent__mutmut_18, 
    'x_gradient_descent__mutmut_19': x_gradient_descent__mutmut_19, 
    'x_gradient_descent__mutmut_20': x_gradient_descent__mutmut_20, 
    'x_gradient_descent__mutmut_21': x_gradient_descent__mutmut_21, 
    'x_gradient_descent__mutmut_22': x_gradient_descent__mutmut_22, 
    'x_gradient_descent__mutmut_23': x_gradient_descent__mutmut_23, 
    'x_gradient_descent__mutmut_24': x_gradient_descent__mutmut_24, 
    'x_gradient_descent__mutmut_25': x_gradient_descent__mutmut_25, 
    'x_gradient_descent__mutmut_26': x_gradient_descent__mutmut_26, 
    'x_gradient_descent__mutmut_27': x_gradient_descent__mutmut_27, 
    'x_gradient_descent__mutmut_28': x_gradient_descent__mutmut_28
}

def gradient_descent(*args, **kwargs):
    result = _mutmut_trampoline(x_gradient_descent__mutmut_orig, x_gradient_descent__mutmut_mutants, args, kwargs)
    return result 

gradient_descent.__signature__ = _mutmut_signature(x_gradient_descent__mutmut_orig)
x_gradient_descent__mutmut_orig.__name__ = 'x_gradient_descent'


def x_save_theta__mutmut_orig(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_1(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = None
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_2(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(None)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_3(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = None
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_4(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"XXtheta0XX": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_5(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"THETA0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_6(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(None), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_7(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "XXtheta1XX": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_8(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "THETA1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_9(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(None)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_10(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = None
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_11(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("XXmin_kmXX", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_12(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("MIN_KM", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_13(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("XXmax_kmXX", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_14(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("MAX_KM", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_15(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("XXmin_priceXX", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_16(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("MIN_PRICE", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_17(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("XXmax_priceXX", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_18(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("MAX_PRICE", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_19(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_20(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = None
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_21(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(None)
    data.update(bounds)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_22(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(None)
    theta_path.write_text(json.dumps(data))


def x_save_theta__mutmut_23(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(None)


def x_save_theta__mutmut_24(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    bounds: dict[str, float] = {}
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        if value is not None:
            bounds[key] = float(value)
    data.update(bounds)
    theta_path.write_text(json.dumps(None))

x_save_theta__mutmut_mutants : ClassVar[MutantDict] = {
'x_save_theta__mutmut_1': x_save_theta__mutmut_1, 
    'x_save_theta__mutmut_2': x_save_theta__mutmut_2, 
    'x_save_theta__mutmut_3': x_save_theta__mutmut_3, 
    'x_save_theta__mutmut_4': x_save_theta__mutmut_4, 
    'x_save_theta__mutmut_5': x_save_theta__mutmut_5, 
    'x_save_theta__mutmut_6': x_save_theta__mutmut_6, 
    'x_save_theta__mutmut_7': x_save_theta__mutmut_7, 
    'x_save_theta__mutmut_8': x_save_theta__mutmut_8, 
    'x_save_theta__mutmut_9': x_save_theta__mutmut_9, 
    'x_save_theta__mutmut_10': x_save_theta__mutmut_10, 
    'x_save_theta__mutmut_11': x_save_theta__mutmut_11, 
    'x_save_theta__mutmut_12': x_save_theta__mutmut_12, 
    'x_save_theta__mutmut_13': x_save_theta__mutmut_13, 
    'x_save_theta__mutmut_14': x_save_theta__mutmut_14, 
    'x_save_theta__mutmut_15': x_save_theta__mutmut_15, 
    'x_save_theta__mutmut_16': x_save_theta__mutmut_16, 
    'x_save_theta__mutmut_17': x_save_theta__mutmut_17, 
    'x_save_theta__mutmut_18': x_save_theta__mutmut_18, 
    'x_save_theta__mutmut_19': x_save_theta__mutmut_19, 
    'x_save_theta__mutmut_20': x_save_theta__mutmut_20, 
    'x_save_theta__mutmut_21': x_save_theta__mutmut_21, 
    'x_save_theta__mutmut_22': x_save_theta__mutmut_22, 
    'x_save_theta__mutmut_23': x_save_theta__mutmut_23, 
    'x_save_theta__mutmut_24': x_save_theta__mutmut_24
}

def save_theta(*args, **kwargs):
    result = _mutmut_trampoline(x_save_theta__mutmut_orig, x_save_theta__mutmut_mutants, args, kwargs)
    return result 

save_theta.__signature__ = _mutmut_signature(x_save_theta__mutmut_orig)
x_save_theta__mutmut_orig.__name__ = 'x_save_theta'


__all__ = ["read_data", "gradient_descent", "save_theta"]
