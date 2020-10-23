import pytest
import os

from ames_qsar.gethlenergy import gethlenergy

filename = 'coumarin_gas.out'

def test_gethlenergy():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    [h, l] = gethlenergy(dir_path, filename)
    print(h,l)
    assert(h == -0.29586 and l == -0.04159)
