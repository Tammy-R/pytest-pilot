import pytest
from stuff.accum import Accumulator

# Ovo je file u kome ce se cuvati fixtures za razlicite module

# Fixtures
@pytest.fixture
def accum():
  return Accumulator()