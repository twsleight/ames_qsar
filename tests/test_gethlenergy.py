import pytest
import os

from ames_qsar.gethlenergy import gethlenergy

filename = 'coumarin_gas.out'

def test_gethlenergy():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    hl = gethlenergy(dir_path, filename)

    assert hl == [-0.29586, -0.04159]
