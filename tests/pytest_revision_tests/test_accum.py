import pytest
from stuff.accum import Accumulator

@pytest.mark.accumulator
def test_initial_count_is_zero(accum):
    # Act-Assert
    assert accum.count == 0

@pytest.mark.accumulator
def test_add_only(accum):
    #Act
    accum.add()
    #Assert
    assert accum.count == 1

@pytest.mark.accumulator
def test_add_two(accum):
    accum.add(2)
    assert accum.count == 2

@pytest.mark.accumulator
def test_add_one_two_times(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_set_count_direclty(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute 'count'") as e:
        accum.count = 10
    #with pytest.raises(AttributeError) as e:
    #    accum.count = 10
    #assert "can't set attribute 'count'" in str(e.value)