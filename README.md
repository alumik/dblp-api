# DBLP API

[![license-MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/AlumiK/dblp-api/blob/main/LICENSE)

A helper package to get information of scholarly articles from [DBLP](https://dblp.uni-trier.de/) using its public API.

## Usage

```python
import dblp

queries = [...]

# verbose > 0: Print out search results for each query.
results = dblp.search(queries, verbose=1)
```

## Examples

### Get Search Results

```python
import dblp

queries = [
    'Anomaly Detection in Streams with Extreme Value Theory',
    'Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning',
    'Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications',
    'Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder',
    'Advances in Cryptography and Secure Hardware for Data Outsourcing',
]

results = dblp.search(queries)
```

The results will be:

```python
[
    {
        'Query': 'Anomaly Detection in Streams with Extreme Value Theory',
        'Title': 'Anomaly Detection in Streams with Extreme Value Theory.',
        'Year': '2017',
        'Venue': 'KDD',
        'CCF Class': 'A',
        'DOI': '10.1145/3097983.3098144',
        'URL': 'https://doi.org/10.1145/3097983.3098144',
        'BibTeX': 'https://dblp.org/rec/conf/kdd/SifferFTL17?view=bibtex'
    },
    {
        'Query': 'Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning',
        'Title': 'N/A',
        'Year': 'N/A',
        'Venue': 'N/A',
        'CCF Class': 'N/A',
        'DOI': 'N/A',
        'URL': 'N/A',
        'BibTeX': 'N/A'
    },
    {
        'Query': 'Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications',
        'Title': 'Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications.',
        'Year': '2018',
        'Venue': 'WWW',
        'CCF Class': 'A',
        'DOI': '10.1145/3178876.3185996',
        'URL': 'https://doi.org/10.1145/3178876.3185996',
        'BibTeX': 'https://dblp.org/rec/conf/www/XuCZLBLLZPFCWQ18?view=bibtex'
    },
    {
        'Query': 'Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder',
        'Title': 'Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder.',
        'Year': '2018',
        'Venue': 'IPCCC',
        'CCF Class': 'C',
        'DOI': '10.1109/PCCC.2018.8710885',
        'URL': 'https://doi.org/10.1109/PCCC.2018.8710885',
        'BibTeX': 'https://dblp.org/rec/conf/ipccc/LiCP18?view=bibtex'
    },
    {
        'Query': 'Advances in Cryptography and Secure Hardware for Data Outsourcing',
        'Title': 'Advances in Cryptography and Secure Hardware for Data Outsourcing.',
        'Year': '2020',
        'Venue': 'ICDE',
        'CCF Class': 'A',
        'DOI': '10.1109/ICDE48307.2020.00173',
        'URL': 'https://doi.org/10.1109/ICDE48307.2020.00173',
        'BibTeX': 'https://dblp.org/rec/conf/icde/0001BM20?view=bibtex'
    },
]
```

### Output in CSV Format

The sample code can be found at `sample/main.py`.

| Query | Title | Year | Venue | CCF Class | DOI | URL | BibTeX |
| - | - | - | - | - | - | - | - |
| Anomaly Detection in Streams with Extreme Value Theory | Anomaly Detection in Streams with Extreme Value Theory. | 2017 | KDD | A | 10.1145/3097983.3098144 | https://doi.org/10.1145/3097983.3098144 | https://dblp.org/rec/conf/kdd/SifferFTL17?view=bibtex |
| Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications | Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications. | 2018 | WWW | A | 10.1145/3178876.3185996 | https://doi.org/10.1145/3178876.3185996 | https://dblp.org/rec/conf/www/XuCZLBLLZPFCWQ18?view=bibtex |
| Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder | Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder. | 2018 | IPCCC | C | 10.1109/PCCC.2018.8710885 | https://doi.org/10.1109/PCCC.2018.8710885 | https://dblp.org/rec/conf/ipccc/LiCP18?view=bibtex |
| Advances in Cryptography and Secure Hardware for Data Outsourcing | Advances in Cryptography and Secure Hardware for Data Outsourcing. | 2020 | ICDE | A | 10.1109/ICDE48307.2020.00173 | https://doi.org/10.1109/ICDE48307.2020.00173 | https://dblp.org/rec/conf/icde/0001BM20?view=bibtex |
