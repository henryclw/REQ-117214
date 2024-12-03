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

## unit test

```bash
cd src
python -m unittest discover -s ./test -v
```

## running the server

```bash
cd src
python main.py
```

## running the mock script to test

```bash
cd src/structure
python mock_web_app.py
```

## References

The sources that I referred to when during the development stage:

- MQTT
  - <https://pypi.org/project/paho-mqtt/>
  - <https://github.com/eclipse-paho/paho.mqtt.python>
- GitHub CI/CD
  - <https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python>

## Possible improvement

Although the basic project goals have been met, there is still a lot of room for improvement:
- Return more errors
- Changing host ip, port to use environment variables
- Deploy as a docker image
- Log the time for calc
- Use something like grafana to monitor
- 
