# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
bezdekIris_decimal = dataiku.Dataset("bezdekIris_decimal")
bezdekIris_decimal_df = bezdekIris_decimal.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

abc_df = bezdekIris_decimal_df # For this sample code, simply copy input to output


# Write recipe outputs
abc = dataiku.Dataset("abc")
abc.write_with_schema(abc_df)
