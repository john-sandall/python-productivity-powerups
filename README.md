# Python Productivity Power-Ups

[![CI](https://github.com/john-sandall/python-productivity-powerups/actions/workflows/main.yaml/badge.svg)](https://github.com/john-sandall/python-productivity-powerups/actions/workflows/main.yaml)

This was created for the PyDataUK May Talks which you can watch in YouTube here: [https://www.youtube.com/watch?v=C1hqHk1SfrA](https://www.youtube.com/watch?v=C1hqHk1SfrA). If you would like to skip to this talk [please use this link](https://youtu.be/C1hqHk1SfrA?t=1851).


## Code
You can find the notebook from the presentation here: [Python Productivity Power-Ups](./notebooks/Python%20Productivity%20Power-Ups.ipynb)

The packages featured were:
1. tqdm: [https://pypi.org/project/tqdm/](https://pypi.org/project/tqdm/)
2. black: [https://pypi.org/project/black/](https://pypi.org/project/black/)
3. nb-black: [https://pypi.org/project/nb-black/](https://pypi.org/project/nb-black/)
4. isort: [https://github.com/timothycrosley/isort](https://github.com/timothycrosley/isort)
5. logaru: [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)
6. joblib: [https://joblib.readthedocs.io/en/latest/](https://joblib.readthedocs.io/en/latest/)


## Project cheatsheet

  - **pre-commit:** `pre-commit run --all-files`
  - **pytest:** `pytest` or `pytest -s`
  - **coverage:** `coverage run -m pytest` or `coverage html`
  - **poetry sync:** `poetry install --no-root --remove-untracked`
  - **updating requirements:** see [docs/updating_requirements.md](docs/updating_requirements.md)
- **create towncrier entry:** `towncrier create 123.added --edit`


## Initial project setup

1. See [docs/getting_started.md](docs/getting_started.md) or [docs/quickstart.md](docs/quickstart.md)
   for how to get up & running.
2. Check [docs/project_specific_setup.md](docs/project_specific_setup.md) for project specific setup.
3. See [docs/using_poetry.md](docs/using_poetry.md) for how to update Python requirements using
   [Poetry](https://python-poetry.org/).
4. See [docs/detect_secrets.md](docs/detect_secrets.md) for more on creating a `.secrets.baseline`
   file using [detect-secrets](https://github.com/Yelp/detect-secrets).
5. See [docs/using_towncrier.md](docs/using_towncrier.md) for how to update the `CHANGELOG.md`
   using [towncrier](https://github.com/twisted/towncrier).

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
