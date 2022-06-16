import fire
import pandas as pd

import dblp


def main(file: str = 'query.txt'):
    with open(file, 'r') as f:
        queries = f.read().splitlines()
    results = dblp.search(queries)
    print(results)
    results.to_csv('output.csv', index=False)


if __name__ == '__main__':
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_columns', None)
    fire.Fire(main)
