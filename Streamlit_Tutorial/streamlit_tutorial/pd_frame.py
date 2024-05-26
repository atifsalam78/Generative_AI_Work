'''
# This is document title

This is _markdown_.
'''

import streamlit as st

import pandas as pd

df : pd.DataFrame = pd.DataFrame({"col1": [1,2,3], "col2": list("abc")})
df