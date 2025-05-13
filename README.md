# DBLP API

![version-0.3.0](https://img.shields.io/badge/version-0.3.0-blue)
![python->=3.9](https://img.shields.io/badge/python->=3.9-blue?logo=python&logoColor=white)
![GitHub License](https://img.shields.io/github/license/alumik/dblp-api)

A helper package to get information of scholarly articles from [DBLP](https://dblp.uni-trier.de/) using its public API.

## Usage

### General Search

```python
import dblp

queries: list[str] = ...

results: list[dict] = dblp.search(queries)
```

### Add China Computer Federation (CCF) Classification

```python
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
    "authors": [
      "Alban Siffer",
      "Pierre-Alain Fouque",
      "Alexandre Termier",
      "Christine Largouët"
    ],
    "title": "Anomaly Detection in Streams with Extreme Value Theory.",
    "venue": "KDD",
    "pages": "1067-1075",
    "year": "2017",
    "type": "Conference and Workshop Papers",
    "access": "closed",
    "key": "conf/kdd/SifferFTL17",
    "doi": "10.1145/3097983.3098144",
    "ee": "https://doi.org/10.1145/3097983.3098144",
    "url": "https://dblp.org/rec/conf/kdd/SifferFTL17"
  },
  {
    "authors": [
      "Xiaoyan Duan",
      "Ningjiang Chen",
      "Yongsheng Xie"
    ],
    "title": "Intelligent Detection of Large-Scale KPI Streams Anomaly Based on Transfer Learning.",
    "venue": "Big Data",
    "pages": "366-379",
    "year": "2019",
    "type": "Conference and Workshop Papers",
    "access": "closed",
    "key": "conf/bdccf/DuanCX19",
    "doi": "10.1007/978-981-15-1899-7_26",
    "ee": "https://doi.org/10.1007/978-981-15-1899-7_26",
    "url": "https://dblp.org/rec/conf/bdccf/DuanCX19"
  },
  {
    "authors": [
      "Haowen Xu",
      "Wenxiao Chen",
      "Nengwen Zhao",
      "Zeyan Li",
      "Jiahao Bu",
      "Zhihan Li",
      "Ying Liu 0024",
      "Youjian Zhao",
      "Dan Pei",
      "Yang Feng",
      "Jie Chen",
      "Zhaogang Wang",
      "Honglin Qiao"
    ],
    "title": "Unsupervised Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications.",
    "venue": "WWW",
    "pages": "187-196",
    "year": "2018",
    "type": "Conference and Workshop Papers",
    "access": "closed",
    "key": "conf/www/XuCZLBLLZPFCWQ18",
    "doi": "10.1145/3178876.3185996",
    "ee": "https://doi.org/10.1145/3178876.3185996",
    "url": "https://dblp.org/rec/conf/www/XuCZLBLLZPFCWQ18"
  },
  {
    "authors": [
      "Zeyan Li",
      "Wenxiao Chen",
      "Dan Pei"
    ],
    "title": "Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder.",
    "venue": "IPCCC",
    "pages": "1-9",
    "year": "2018",
    "type": "Conference and Workshop Papers",
    "access": "closed",
    "key": "conf/ipccc/LiCP18",
    "doi": "10.1109/PCCC.2018.8710885",
    "ee": "https://doi.org/10.1109/PCCC.2018.8710885",
    "url": "https://dblp.org/rec/conf/ipccc/LiCP18"
  },
  {
    "authors": [
      "Shantanu Sharma 0001",
      "Anton Burtsev",
      "Sharad Mehrotra"
    ],
    "title": "Advances in Cryptography and Secure Hardware for Data Outsourcing.",
    "venue": "ICDE",
    "pages": "1798-1801",
    "year": "2020",
    "type": "Conference and Workshop Papers",
    "access": "closed",
    "key": "conf/icde/0001BM20",
    "doi": "10.1109/ICDE48307.2020.00173",
    "ee": "https://doi.org/10.1109/ICDE48307.2020.00173",
    "url": "https://dblp.org/rec/conf/icde/0001BM20"
  }
]
```
