from pathlib import Path

import pandas as pd
import numpy as np
import pytest

from ipumspy import readers

def test_my_stuff():
    my_string = readers.test()
    assert my_string == "test"