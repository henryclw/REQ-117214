# REQ-117214
BC Public Service REQ 117214

# temp logs

## python conda environment creation

```bash
conda create --name py312bcps python=3.12

# some windows
source activate py312bcps
# bash
conda activate py312bcps
```

## package management

```bash
pip install -r ./requirements.txt --upgrade
pip list --format=freeze > ./requirements.txt
```

## test

```bash
cd src
python -m unittest discover -s ./test -v
```