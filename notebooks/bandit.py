"""Bandit examples.

bandit notebooks/bandit.py
"""

import pickle

import pandas as pd
import requests
import sqlalchemy

# Bad: hard coded passwords
EMAIL_PASSWORD = "secret"

# Bad: potential SQL injection
identifier = "123"
query = "SELECT * FROM foo WHERE id = '%s'" % identifier

# Bad: No timeout when using requests
requests.get("https://gmail.com")

# Bad: Pickle can be insecure
# https://github.com/PyCQA/bandit/pull/710
df = pd.DataFrame({"col_A": [1, 2]})
pick = pickle.dumps(df)
print(pd.read_pickle(pick))
