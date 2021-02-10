# ValheimBot

## Create developement environment (Raspian/Debian)
Clone repo
```
git clone https://github.com/NebulusRemixProject/ValheimBot.git
```
Install virtual environment
```
apt-get install virtualenv
virtualenv --python3 .
source ./bin/activate
```
Install requirements
```
pip install -r requirements.txt
```

## Run
```
echo CMD_PREFIX='!' > .env
echo TOKEN=<BOT_TOKEN> >> .env
pip install -r requirements.txt
python main.py
```



