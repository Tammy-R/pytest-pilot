#import pytest lib da bi mogli da koristimo pytest.raises za asertaciju error msgs
import pytest

# assert exception messages
#-------------------------------------------------
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)