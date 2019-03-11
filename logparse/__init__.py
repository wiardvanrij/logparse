import apache_log_parser
import os
import shutil

def parseFile(filePath):
    reader = ReadFile(filePath)
    reader.print_data()  

def config(type, value):
    from ConfigParser import ConfigParser

    user_config_dir = os.path.expanduser("~") + "/.config/logparse"
    user_config = user_config_dir + "/config.ini"

    if not os.path.isdir(user_config_dir):
        os.makedirs(user_config_dir)

    if not os.path.isfile(user_config):    
        shutil.copyfile('logparse/config.ini', user_config)

    config = ConfigParser()
    config.read(user_config)

    # try catch this + return
    return config.get(type, value, True)

class ReadFile:
    import apache_log_parser


    def __init__(self, path):
        self.path = path
        self.regex = config('log', 'regex')
        self.remote_hosts = {}

    def print_data(self):
        
        import collections

        line_parser = apache_log_parser.make_parser(self.regex)
        with open(self.path, 'r') as f:
            for line in f:
                # Try catch this..
                data = line_parser(line)
                if data['remote_host'] not in self.remote_hosts:
                    self.remote_hosts[data['remote_host']] = 1
                else:
                    self.remote_hosts[data['remote_host']] += 1

        remoteHostCollection = collections.Counter(self.remote_hosts)

        for remoteHost, count in remoteHostCollection.most_common(10):
            print remoteHost , ":" , count
