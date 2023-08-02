import requests
import pandas as pd

from urllib.parse import urlencode
from importlib.resources import open_binary

BASE_URL = 'https://dblp.org/search/publ/api'


def add_ccf_class(results: list[dict]) -> list[dict]:
    def get_ccf_class(venue: str | None, catalog: pd.DataFrame) -> str | None:
        if venue is None:
            return
        if len(series := catalog.loc[catalog.get('abbr').str.lower() == venue.lower(), 'class']) > 0:
            return series.item()
        elif len(series := catalog.loc[catalog.get('url').str.contains(f'/{venue.lower()}/'), 'class']) > 0:
            return series.item()

    catalog = pd.read_csv(open_binary('dblp.data', 'ccf_catalog.csv'))
    for result in results:
        result['ccf_class'] = get_ccf_class(result.get('venue'), catalog=catalog)
    return results


def search(queries: list[str]) -> list[dict]:
    results = []
    for query in queries:
        entry = {
            'query': query,
            'title': None,
            'year': None,
            'venue': None,
            'doi': None,
            'url': None,
            'bibtex': None,
        }
        options = {
            'q': query,
            'format': 'json',
            'h': 1
        }
        r = requests.get(f'{BASE_URL}?{urlencode(options)}').json()
        hit = r.get('result').get('hits').get('hit')
        if hit is not None:
            info = hit[0].get('info')
            entry['title'] = info.get('title')
            entry['year'] = info.get('year')
            entry['venue'] = info.get('venue')
            entry['doi'] = info.get('doi')
            entry['url'] = info.get('ee')
            entry['bibtex'] = f'{info.get("url")}?view=bibtex'
        results.append(entry)
    return results
