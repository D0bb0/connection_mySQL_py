import configparser
import os
from pathlib import Path

class saveConfig:
    def __init__(self,usr_color,db_name='',db_pass='',db_nemebd=''):
        self.usr_color = usr_color
        self.db_name = db_name
        self.db_pass = db_pass
        self.db_namedb = db_nemebd
        self.config = configparser.ConfigParser()
        self.filename = "connection.ini"
        path = Path(__file__)
        ROOT_DIR = path.parent.absolute()
        self.fullFilename = os.path.join(ROOT_DIR, self.filename)

    def saveFile(self):
        self.config.read(self.fullFilename)

        try:
            self.config.add_section("SETTINGS")
        except configparser.DuplicateSectionError:
            pass

        self.config.set("SETTINGS", "DB_NAME", self.db_name)
        self.config.set("SETTINGS", "DB_PASS", self.db_pass)
        self.config.set("SETTINGS", "BD_NAMEBD", self.db_namedb)
        self.config.set("SETTINGS", "USR_COLOR", self.usr_color)

        with open(self.fullFilename, "w") as config_file:
            self.config.write(config_file)

        
    def readFile(self):
        res = {}
        res["credential"] = {}
        res["status"] = False

        self.config.read(self.fullFilename)
        keys = [
            "DB_NAME",
            "DB_PASS",
            "BD_NAMEBD",
            "USR_COLOR"
        ]
        for key in keys:
            try:
                value = self.config.get("SETTINGS", key)
                res["credential"][key] = value
                res["status"] = True
                    
                
            except configparser.NoSectionError:
                pass
                
        return res