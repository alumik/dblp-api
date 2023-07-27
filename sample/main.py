import fire
import pandas as pd

import dblp


def main(input: str, with_ccf_class: bool = False):
    with open(input, 'r') as f:
        queries = f.read().splitlines()
    results = dblp.search(queries)
    if with_ccf_class:
        results = dblp.add_ccf_class(results)
    print(results)
    results.to_csv('output.csv', index=False)


if __name__ == '__main__':
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_columns', None)
    fire.Fire(main)
