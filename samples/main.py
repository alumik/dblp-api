import fire
import json
import pathlib

import dblp


def main(path: str, with_ccf_class: bool = False):
    queries = pathlib.Path(path).read_text().splitlines()
    results = dblp.search(queries)
    if with_ccf_class:
        results = dblp.add_ccf_class(results)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    fire.Fire(main)
