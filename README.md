#Warning: Use this repo at your own risk

#click_the_text_below_to_deploy

[Click Here To F**K on Heroku](https://heroku.com/deploy)


#### Simple Guide
Simply clone the repository and run the main file:
```sh
git clone https://github.com/muhammedfurkan/uniborg.git
cd uniborg
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python3 -m stdborg YourSessionName
```
 
An example `config.py` file could be:
 
**Not All of the variables are mandatory**
 
__The UniBorg should work by setting only these variables__
 
```python3
from sample_config import Config
 
class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```
 
## internals
 
The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/muhammedfurkan/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements, the `_core` plugin, and the `_inline_bot` plugin.
 
 
 
- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.
- Please report any issues to the support group: [support group](https://t.me/joinchat/AHAujEjG4FBO-TH-NrVVbg)
 

 
## learning
 
Check out the already-mentioned [plugins](https://github.com/SpEcHiDe/muhammedfurkan/tree/master/stdplugins) directory, or some third-party [plugins](https://telegram.dog/UniBorg) to learn how to write your own, and consider reading [Telethon's documentation](http://telethon.readthedocs.io/).
 
