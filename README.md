# DBLP API

![version-0.2.1](https://img.shields.io/badge/version-0.2.1-blue)
![python->=3.10](https://img.shields.io/badge/python->=3.10-blue?logo=python&logoColor=white)
![license-MIT](https://img.shields.io/badge/license-MIT-green)

A helper package to get information of scholarly articles from [DBLP](https://dblp.uni-trier.de/) using its public API.

## Usage

```python
import dblp

queries: list[str] = ...

results: list[dict] = dblp.search(queries)
results_with_ccf_class: list[dict] = dblp.add_ccf_class(results)
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

```json
[
  {
    "query": "Anomaly Detection in Streams with Extreme Value Theory",
    "title": "Anomaly Detection in Streams with Extreme Value Theory.",
    "year": "2017",
    "venue": "KDD",
    "doi": "10.1145/3097983.3098144",
    "url": "https://doi.org/10.1145/3097983.3098144",
    "bibtex": "https://dblp.org/rec/conf/kdd/SifferFTL17?view=bibtex"
  },
  {
    "query": "Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning",
    "title": "Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning.",
    "year": "2019",
    "venue": "Big Data",
    "doi": "10.1007/978-981-15-1899-7_26",
    "url": "https://doi.org/10.1007/978-981-15-1899-7_26",
    "bibtex": "https://dblp.org/rec/conf/bdccf/DuanCX19?view=bibtex"
  },
  {
    "query": "Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications",
    "title": "Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications.",
    "year": "2018",
    "venue": "WWW",
    "doi": "10.1145/3178876.3185996",
    "url": "https://doi.org/10.1145/3178876.3185996",
    "bibtex": "https://dblp.org/rec/conf/www/XuCZLBLLZPFCWQ18?view=bibtex"
  },
  {
    "query": "Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder",
    "title": "Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder.",
    "year": "2018",
    "venue": "IPCCC",
    "doi": "10.1109/PCCC.2018.8710885",
    "url": "https://doi.org/10.1109/PCCC.2018.8710885",
    "bibtex": "https://dblp.org/rec/conf/ipccc/LiCP18?view=bibtex"
  },
  {
    "query": "Advances in Cryptography and Secure Hardware for Data Outsourcing",
    "title": "Advances in Cryptography and Secure Hardware for Data Outsourcing.",
    "year": "2020",
    "venue": "ICDE",
    "doi": "10.1109/ICDE48307.2020.00173",
    "url": "https://doi.org/10.1109/ICDE48307.2020.00173",
    "bibtex": "https://dblp.org/rec/conf/icde/0001BM20?view=bibtex"
  }
]
```
