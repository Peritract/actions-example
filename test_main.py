"""Tests for the functions in main.py."""

import pytest

from main import get_sarcastic_text


def test_rejects_non_string_input():
    """Checks that the function rejects invalid arguments."""

    with pytest.raises(TypeError) as ex:
        get_sarcastic_text(34)

    assert ex.value.args[0] == "Argument must be a string."


def test_returns_expected_values():
    """Checks that the function works as expected."""
    assert get_sarcastic_text("hello") == "hElLo"
    assert get_sarcastic_text("big horse") == "bIg hOrSe"
