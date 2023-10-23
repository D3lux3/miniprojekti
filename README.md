# miniprojekti

Install dependencies

```
$ poetry install
```

Run development server:

```
$ poetry run invoke start
```

Crawl normal youtube searches:

```
$ poetry run invoke crawler
```

Crawl youtube searches with most viewed setting:

```
$ poetry run invoke crawlmost
```

Runs wrangler in Jupyter notebook:

```
$ poetry run invoke wrangler
```
