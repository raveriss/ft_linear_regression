"""Evaluation metrics for the linear regression project."""

from __future__ import annotations

import json
import math
from pathlib import Path

from linear_regression import estimatePrice
from train.train import read_data
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


def x_read_theta__mutmut_orig(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_1(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = None
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_2(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(None)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_3(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = None
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_4(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(None)
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_5(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(None) from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_6(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = None
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_7(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(None)
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_8(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["XXtheta0XX"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_9(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["THETA0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_10(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = None
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_11(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(None)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_12(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["XXtheta1XX"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_13(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["THETA1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def x_read_theta__mutmut_14(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(None) from exc
    return theta0, theta1

x_read_theta__mutmut_mutants : ClassVar[MutantDict] = {
'x_read_theta__mutmut_1': x_read_theta__mutmut_1, 
    'x_read_theta__mutmut_2': x_read_theta__mutmut_2, 
    'x_read_theta__mutmut_3': x_read_theta__mutmut_3, 
    'x_read_theta__mutmut_4': x_read_theta__mutmut_4, 
    'x_read_theta__mutmut_5': x_read_theta__mutmut_5, 
    'x_read_theta__mutmut_6': x_read_theta__mutmut_6, 
    'x_read_theta__mutmut_7': x_read_theta__mutmut_7, 
    'x_read_theta__mutmut_8': x_read_theta__mutmut_8, 
    'x_read_theta__mutmut_9': x_read_theta__mutmut_9, 
    'x_read_theta__mutmut_10': x_read_theta__mutmut_10, 
    'x_read_theta__mutmut_11': x_read_theta__mutmut_11, 
    'x_read_theta__mutmut_12': x_read_theta__mutmut_12, 
    'x_read_theta__mutmut_13': x_read_theta__mutmut_13, 
    'x_read_theta__mutmut_14': x_read_theta__mutmut_14
}

def read_theta(*args, **kwargs):
    result = _mutmut_trampoline(x_read_theta__mutmut_orig, x_read_theta__mutmut_mutants, args, kwargs)
    return result 

read_theta.__signature__ = _mutmut_signature(x_read_theta__mutmut_orig)
x_read_theta__mutmut_orig.__name__ = 'x_read_theta'


def x_evaluate__mutmut_orig(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_1(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = None
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_2(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(None)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_3(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = None
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_4(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(None)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_5(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = None
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_6(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = None
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_7(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(None, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_8(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, None, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_9(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, None) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_10(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_11(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_12(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, ) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_13(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = None
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_14(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = None
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_15(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(None)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_16(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) * m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_17(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum(None) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_18(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) * 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_19(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p + y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_20(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 3 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_21(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(None, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_22(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, None)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_23(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_24(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, )) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_25(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = None
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_26(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) * m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_27(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(None) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_28(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = None
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_29(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum(None)
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_30(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) * 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_31(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y + p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_32(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 3 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_33(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(None, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_34(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, None))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_35(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_36(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, ))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_37(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = None
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_38(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum(None)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_39(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) * 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_40(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y + y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_41(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 3 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_42(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = None
    return rmse, r2


def x_evaluate__mutmut_43(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 2.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_44(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot != 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_45(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 1.0 else 1 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_46(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 + ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_47(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 2 - ss_res / ss_tot
    return rmse, r2


def x_evaluate__mutmut_48(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res * ss_tot
    return rmse, r2

x_evaluate__mutmut_mutants : ClassVar[MutantDict] = {
'x_evaluate__mutmut_1': x_evaluate__mutmut_1, 
    'x_evaluate__mutmut_2': x_evaluate__mutmut_2, 
    'x_evaluate__mutmut_3': x_evaluate__mutmut_3, 
    'x_evaluate__mutmut_4': x_evaluate__mutmut_4, 
    'x_evaluate__mutmut_5': x_evaluate__mutmut_5, 
    'x_evaluate__mutmut_6': x_evaluate__mutmut_6, 
    'x_evaluate__mutmut_7': x_evaluate__mutmut_7, 
    'x_evaluate__mutmut_8': x_evaluate__mutmut_8, 
    'x_evaluate__mutmut_9': x_evaluate__mutmut_9, 
    'x_evaluate__mutmut_10': x_evaluate__mutmut_10, 
    'x_evaluate__mutmut_11': x_evaluate__mutmut_11, 
    'x_evaluate__mutmut_12': x_evaluate__mutmut_12, 
    'x_evaluate__mutmut_13': x_evaluate__mutmut_13, 
    'x_evaluate__mutmut_14': x_evaluate__mutmut_14, 
    'x_evaluate__mutmut_15': x_evaluate__mutmut_15, 
    'x_evaluate__mutmut_16': x_evaluate__mutmut_16, 
    'x_evaluate__mutmut_17': x_evaluate__mutmut_17, 
    'x_evaluate__mutmut_18': x_evaluate__mutmut_18, 
    'x_evaluate__mutmut_19': x_evaluate__mutmut_19, 
    'x_evaluate__mutmut_20': x_evaluate__mutmut_20, 
    'x_evaluate__mutmut_21': x_evaluate__mutmut_21, 
    'x_evaluate__mutmut_22': x_evaluate__mutmut_22, 
    'x_evaluate__mutmut_23': x_evaluate__mutmut_23, 
    'x_evaluate__mutmut_24': x_evaluate__mutmut_24, 
    'x_evaluate__mutmut_25': x_evaluate__mutmut_25, 
    'x_evaluate__mutmut_26': x_evaluate__mutmut_26, 
    'x_evaluate__mutmut_27': x_evaluate__mutmut_27, 
    'x_evaluate__mutmut_28': x_evaluate__mutmut_28, 
    'x_evaluate__mutmut_29': x_evaluate__mutmut_29, 
    'x_evaluate__mutmut_30': x_evaluate__mutmut_30, 
    'x_evaluate__mutmut_31': x_evaluate__mutmut_31, 
    'x_evaluate__mutmut_32': x_evaluate__mutmut_32, 
    'x_evaluate__mutmut_33': x_evaluate__mutmut_33, 
    'x_evaluate__mutmut_34': x_evaluate__mutmut_34, 
    'x_evaluate__mutmut_35': x_evaluate__mutmut_35, 
    'x_evaluate__mutmut_36': x_evaluate__mutmut_36, 
    'x_evaluate__mutmut_37': x_evaluate__mutmut_37, 
    'x_evaluate__mutmut_38': x_evaluate__mutmut_38, 
    'x_evaluate__mutmut_39': x_evaluate__mutmut_39, 
    'x_evaluate__mutmut_40': x_evaluate__mutmut_40, 
    'x_evaluate__mutmut_41': x_evaluate__mutmut_41, 
    'x_evaluate__mutmut_42': x_evaluate__mutmut_42, 
    'x_evaluate__mutmut_43': x_evaluate__mutmut_43, 
    'x_evaluate__mutmut_44': x_evaluate__mutmut_44, 
    'x_evaluate__mutmut_45': x_evaluate__mutmut_45, 
    'x_evaluate__mutmut_46': x_evaluate__mutmut_46, 
    'x_evaluate__mutmut_47': x_evaluate__mutmut_47, 
    'x_evaluate__mutmut_48': x_evaluate__mutmut_48
}

def evaluate(*args, **kwargs):
    result = _mutmut_trampoline(x_evaluate__mutmut_orig, x_evaluate__mutmut_mutants, args, kwargs)
    return result 

evaluate.__signature__ = _mutmut_signature(x_evaluate__mutmut_orig)
x_evaluate__mutmut_orig.__name__ = 'x_evaluate'


def x_main__mutmut_orig() -> None:
    rmse, r2 = evaluate("data.csv", "theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_1() -> None:
    rmse, r2 = None
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_2() -> None:
    rmse, r2 = evaluate(None, "theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_3() -> None:
    rmse, r2 = evaluate("data.csv", None)
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_4() -> None:
    rmse, r2 = evaluate("theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_5() -> None:
    rmse, r2 = evaluate("data.csv", )
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_6() -> None:
    rmse, r2 = evaluate("XXdata.csvXX", "theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_7() -> None:
    rmse, r2 = evaluate("DATA.CSV", "theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_8() -> None:
    rmse, r2 = evaluate("data.csv", "XXtheta.jsonXX")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_9() -> None:
    rmse, r2 = evaluate("data.csv", "THETA.JSON")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


def x_main__mutmut_10() -> None:
    rmse, r2 = evaluate("data.csv", "theta.json")
    print(None)
    print(f"R2: {r2}")


def x_main__mutmut_11() -> None:
    rmse, r2 = evaluate("data.csv", "theta.json")
    print(f"RMSE: {rmse}")
    print(None)

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
    'x_main__mutmut_11': x_main__mutmut_11
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


__all__ = ["read_theta", "evaluate", "main"]

if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
