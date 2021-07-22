import sys
sys.path.append('..')

import dblp
import fire
import pandas as pd

def main(file: str = 'query.txt'):
    with open(file, 'r') as f:
        queries = f.read().splitlines()
    results = dblp.search(queries, verbose=1)
    print(results)
    pd.DataFrame(results).to_csv('output.csv', index=False)

if __name__ == '__main__':
    fire.Fire(main)
