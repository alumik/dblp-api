import dblp
import pandas as pd

with open('query.txt', 'r') as f:
    queries = f.read().splitlines()

results = dblp.search(queries, verbose=1)
print(results)
pd.DataFrame(results).to_csv('output.csv', index=False)
