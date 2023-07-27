import requests
import pandas as pd

from urllib.parse import urlencode
from importlib.resources import open_binary

BASE_URL = 'https://dblp.org/search/publ/api'


def _get_ccf_class(venue: str | None, catalog: pd.DataFrame) -> str | None:
    if venue is None:
        return
    if len(series := catalog.loc[catalog.get('abbr').str.lower() == venue.lower(), 'class']) > 0:
        return series.item()
    elif len(series := catalog.loc[catalog.get('url').str.contains(f'/{venue.lower()}/'), 'class']) > 0:
        return series.item()


def add_ccf_class(results: pd.DataFrame) -> pd.DataFrame:
    catalog = pd.read_csv(open_binary('dblp.data', 'ccf_catalog.csv'))
    results['ccf_class'] = results.get('venue').apply(_get_ccf_class, catalog=catalog)
    return results


def search(queries: list[str], **kwargs) -> pd.DataFrame:
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
    results = pd.DataFrame(results, **kwargs)
    return results
