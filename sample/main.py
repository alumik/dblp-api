import fire
import json

import dblp


def main(input: str, with_ccf_class: bool = False):
    with open(input, 'r') as f:
        queries = f.read().splitlines()
    results = dblp.search(queries)
    if with_ccf_class:
        results = dblp.add_ccf_class(results)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    fire.Fire(main)
