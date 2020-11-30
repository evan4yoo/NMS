import configparser
#import database

class SetConfig():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.dbhost = config.get("mysql", "host")
        self.dbuser = config.get("mysql", "username")
        self.dbpasswd = config.get("mysql", "password")
        self.dbname = "hosts"


setfig = SetConfig()