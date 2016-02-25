# WOUDC Automated Quality Assessment library

Python package for automatically quality assessing WOUDC data based on defined rules.

## Installation

### Requirements

woudc-extcsv requires Python 2.7.

### Dependencies

None.

### Installing the Package

```bash
# via distutils
pip install -r requirements.txt
python setup.py install
```

## Usage

### Command line interface
```bash
usage: woudc-qa.py [-h] --file FILE

Execute Qa.

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Path to extended CSV file to be quality assessed.

## Examples
```python
from woudc_qa import qa
file_s = open(<path to your extended CSV file.>).read()
qa_results = qa(file_s)
```


## Development

For development environments, install
in a Python [virtualenv](http://virtualenv.org):

```bash
virtualenv foo
cd foo
. bin/activate
# fork master
http://gitlab.ssc.etg.gc.ca/woudc/woudc-qa
# clone your fork to create a branch
git clone https://gitlab.ssc.etg.gc.ca/{your Gitlab username}/woudc-qa.git
cd woudc-qa
# install dev packages
pip install -r requirements.txt
python setup.py install
# create upstream remote
git remote add upstream https://gitlab.ssc.etg.gc.ca/woudc/woudc-qa.git
git pull upstream master
git branch my-cool-feature
git checkout my-cool-feature
# start dev
git commit -m 'implement cool feature'
# push to your fork
git push origin my-cool-feature
# issue Pull Request on GitHub
git checkout master
# cleanup/update once your branch is merged on GitHub
# remove branch
git branch -D my-cool-feature
# update your fork
git pull upstream master
git push origin master
```

### Running Tests

```bash
# via distutils
python setup.py test
# manually
python run_tests.py
# report test coverage
coverage run --source woudc_qa setup.py test
coverage report -m
```

### Code Conventions

woudc_qa code conventions are as per
[PEP8](https://www.python.org/dev/peps/pep-0008).

```bash
# code should always pass the following
find -type f -name "*.py" | xargs flake8
```

## Issues

All bugs, enhancements and issues are managed on
[GitHub](http://gitlab.ssc.etg.gc.ca/woudc/woudc-qa/issues).

## History

## Contact

* [Thinesh Sornalingam](http://geds20-sage20.ssc-spc.gc.ca/en/GEDS20/?pgid=015&dn=CN%3Dthinesh.sornalingam%40canada.ca%2COU%3DDAT-GES%2COU%3DMON-STR%2COU%3DMON-DIR%2COU%3DMSCB-DGSMC%2COU%3DDMO-CSM%2COU%3DEC-EC%2CO%3DGC%2CC%3DCA)
