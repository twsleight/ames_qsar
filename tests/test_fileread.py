import pytest
import os
import shutil

#import the function to be tested
from ames_qsar.out_fileread import out_fileread

def test_fileread(tmpdir):
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    #copy the files into a temporary directory
    shutil.copytree(dir_path, tmpdir, ignore = shutil.ignore_patterns('*.py'), dirs_exist_ok=True)

    assert set(out_fileread(tmpdir)) == set(['coumarin_gas.out','coumarin_neg.out','coumarin_pos.out' ])
