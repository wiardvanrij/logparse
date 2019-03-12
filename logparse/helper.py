import os
import shutil

def readConfig(type, value):
    from ConfigParser import ConfigParser

    user_config_dir = os.path.expanduser("~") + "/.config/logparse"
    user_config = user_config_dir + "/config.ini"
    try:
        if not os.path.isdir(user_config_dir):
            os.makedirs(user_config_dir)
        if not os.path.isfile(user_config):    
            shutil.copyfile('logparse/config.ini', user_config)
    except:
        print("Failed to create config dir or file")
        exit(1)        

    try:
        config = ConfigParser()
        config.read(user_config)
    except:
        print("Failed to read config, please check permissions")
        exit(1)

    try:
        configData = config.get(type, value, True)
    except:
        print("Failed to retreive config item: ", type)
        exit(1)

    return configData 