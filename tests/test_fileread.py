import pytest
import os

from ames_qsar.out_fileread import out_fileread

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
def test_fileread():
    #these are the test files that should be found
    assert set(out_fileread(THIS_DIR)) == set(['coumarin_gas.out'\
        ,'coumarin_neg.out','coumarin_pos.out' ])
