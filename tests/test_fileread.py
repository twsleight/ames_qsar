#adde the current working directory to the PATH
import sys,os
sys.path.append(os.getcwd())

import pytest
import os
from ames_qsar.out_fileread import out_fileread

def test_fileread():
    #these are the test files that should be found
    assert set(out_fileread(os.getcwd()+ '/tests')) == set(['coumarin_gas.out'\
        ,'coumarin_neg.out','coumarin_pos.out' ])
