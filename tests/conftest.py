"""
This module contains shared fixtures.
"""

import pytest
#import selenium.webdriver
from stuff.accum import Accumulator


# @pytest.fixture
# def browser():
#     b = selenium.webdriver.Chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()

@pytest.fixture
def accum():
    # Arrange
    accum = Accumulator()
    yield accum