import requests
import pandas as pd

from typing import *
from urllib.parse import urlencode
from importlib.resources import open_binary


def _ccf_class(venue: Optional[str]) -> Optional[str]:
    if venue is None:
        return
    ccf = pd.read_csv(open_binary('dblp.data', 'ccf_catalog.csv'))
    if len(series := ccf.loc[ccf.get('abbr').str.lower() == venue.lower(), 'class']) > 0:
        return series.item()
    elif len(series := ccf.loc[ccf.get('url').str.contains(f'/{venue.lower()}/'), 'class']) > 0:
        return series.item()


def search(queries: Sequence[str],
           verbose: int = 0,
           plain: bool = False,
           formatter: Optional[Callable[Dict[str, Any], str]] = None,
           **kwargs) -> Union[Sequence[Dict[str, Any]], pd.DataFrame]:
    url = 'https://dblp.org/search/publ/api'
    results = []
    for query in queries:
        entry = {
            'query': query,
            'title': None,
            'year': None,
            'venue': None,
            'ccf_class': None,
            'doi': None,
            'url': None,
            'bibtex': None,
        }
        options = {
            'q': query,
            'format': 'json',
            'h': 1
        }
        r = requests.get(f'{url}?{urlencode(options)}').json()
        hit = r.get('result').get('hits').get('hit')
        if hit is not None:
            info = hit[0].get('info')
            entry['title'] = info.get('title')
            entry['year'] = info.get('year')
            entry['venue'] = info.get('venue')
            entry['ccf_class'] = _ccf_class(entry.get('venue'))
            entry['doi'] = info.get('doi')
            entry['url'] = info.get('ee')
            entry['bibtex'] = f'{info.get("url")}?view=bibtex'
        results.append(entry)
        if verbose > 0:
            if formatter is not None:
                print(formatter(entry))
            else:
                print(entry)
    if not plain:
        results = pd.DataFrame(results, **kwargs)
    return results
