import requests
import pandas as pd

from urllib.parse import urlencode
from importlib.resources import open_binary

BASE_URL = 'https://dblp.org/search/publ/api'


def add_ccf_class(results: list[dict]) -> list[dict]:
    def get_ccf_class(venue: str | None, catalog: pd.DataFrame) -> str | None:
        if venue is None:
            return None
        if len(series := catalog.loc[catalog.get('abbr').str.lower() == venue.lower(), 'class']) > 0:
            return series.item()
        if len(series := catalog.loc[catalog.get('url').str.contains(f'/{venue.lower()}/'), 'class']) > 0:
            return series.item()
        return None

    catalog = pd.read_csv(open_binary('dblp.data', 'ccf_catalog.csv'))
    for result in results:
        result['ccf_class'] = get_ccf_class(result.get('venue'), catalog=catalog)
    return results


def search(queries: list[str]) -> list[dict | None]:
    results = []
    for query in queries:
        options = {
            'q': query,
            'format': 'json',
            'h': 1,
        }
        r = requests.get(f'{BASE_URL}?{urlencode(options)}').json()
        hit = r['result']['hits'].get('hit')
        if hit is not None:
            info = hit[0].get('info')
            info['authors'] = [author['text'] for author in info['authors']['author']]
            results.append(info)
        else:
            results.append(None)
    return results
