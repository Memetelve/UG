import pytest


from main import (
    calculate_blocks_per_row,
    calculate_margin,
    calculate_paddle_deflection_angle,
)

# create tests for the functions in main.py
def test_calculate_blocks_per_row():
    assert calculate_blocks_per_row(800, 20, 60) == 10
    assert calculate_blocks_per_row(800, 20, 40) == 13
    assert calculate_blocks_per_row(800, 00, 40) == 20


def test_calculate_margin():
    assert calculate_margin(10, 800, 20, 60) == 10
    assert calculate_margin(13, 800, 20, 40) == 20
    assert calculate_margin(20, 800, 00, 40) == 0


def test_calculate_paddle_deflection_angle():
    assert calculate_paddle_deflection_angle(20, 0, 100) == -1.5
    assert calculate_paddle_deflection_angle(0, 40, 100) == 0.0
    assert calculate_paddle_deflection_angle(0, 100, 100) == 1.5
