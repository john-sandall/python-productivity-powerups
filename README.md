# Python Productivity Power-Ups

## Code
You can find the notebook from the presentation here: [Python Productivity Power-Ups](./notebooks/Python%20Productivity%20Power-Ups.ipynb)

The packages featured were:
1. tqdm: [https://pypi.org/project/tqdm/](https://pypi.org/project/tqdm/)
2. black: [https://pypi.org/project/black/](https://pypi.org/project/black/)
3. nb-black: [https://pypi.org/project/nb-black/](https://pypi.org/project/nb-black/)
4. isort: [https://github.com/timothycrosley/isort](https://github.com/timothycrosley/isort)
5. logaru: [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)
6. joblib: [https://joblib.readthedocs.io/en/latest/](https://joblib.readthedocs.io/en/latest/)

## Load the environment using pip-tools
```
# Activate environment
workon python-productivity-powerups

# Update packages from requirements.txt
pip-sync
 
# Install new package & update requirements.txt
pip install new-package-name
pip freeze  # to check version number

# copy paste package & version to requirements.in
pip-compile requirements.in
pip-sync
```

## Setup
```
# Install virtualenv
pip install virtualenv


# Install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
pip install virtualenvwrapper
# Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs by adding following to .zshrc
zshconfig
#    # "Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs"
#    export WORKON_HOME=$HOME/.virtualenvs
#    export PROJECT_HOME=$HOME/code
#    source /usr/local/bin/virtualenvwrapper.sh
source ~/.zshrc
source /usr/local/bin/virtualenvwrapper.sh
# Now let's make a virtualenv
mkvirtualenv venv
workon venv
# Commands `workon venv`, `deactivate`, `lsvirtualenv` and `rmvirtualenv` are useful
# WARNING: When you brew install formulae that provide Python bindings, you should not be in an active virtual environment.
# (https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md)
deactivate


# Create virtualenv & install packasges
mkvirtualenv numberphile
pip install python-productivity-powerups
pip-sync
python -m ipykernel install --user --name python-productivity-powerups --display-name "Python (python-productivity-powerups)"
```

---

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
