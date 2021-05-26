print("validating configurations.......")

import json
from pathlib import Path

class Config_Parser:
    def __init__(self, user_file):
        self.user = {}
        self.app = {}
        self._parse(user_file)

    def _parse(self,user_file):
        basepath = Path(user_file)
        files = [entry for entry in basepath.iterdir() if entry.is_file()]
        for file in files:
            with open(str(file)) as f:
                jsn = json.load(f)
            if(file.name == "user.json"):
                self.user = jsn
            if(file.name == "app.json"):
                self.app = jsn

    def validate():
        print("To be written soon.....")

config = Config_Parser('config/')