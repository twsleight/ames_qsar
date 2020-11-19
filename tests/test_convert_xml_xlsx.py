import pytest
import os

from ames_qsar.read_ccris_data import convert_xml_xlsx

def test_convert_xml_xlsx():
    parent = os.path.join(os.path.abspath(__file__), os.pardir)
    #retrieve the ccris.xml file from the data folder

    filename = os.path.abspath(os.path.join(parent,'..', 'tests', 'test_CCRIS_data.xml'))

    df = convert_xml_xlsx(filename)

    assert len(df) == 75
