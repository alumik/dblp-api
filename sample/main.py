import json
import fire

import dblp


def main(file: str = 'query.txt'):
    with open(file, 'r') as f:
        queries = f.read().splitlines()
    results = dblp.search(queries, verbose=1, formatter=lambda x: json.dumps(x, indent=2))
    print(results)
    results.to_csv('output.csv', index=False)


if __name__ == '__main__':
    fire.Fire(main)
