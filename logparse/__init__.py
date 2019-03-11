import apache_log_parser
from os.path import expanduser


def testing():
    line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
    log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
    return(log_line_data)

def parseFile(filePath):
    reader = ReadFile(filePath)
    reader.print_data()

def config():
    from ConfigParser import ConfigParser
    home = expanduser("~")
    config = ConfigParser()
    config.read(home + 'logparse.ini')
    regex = config.get('log', 'regex')
    print(regex)  

class ReadFile:
    import apache_log_parser

    def __init__(self, path):
        self.path = path

    def print_data(self):
        line_parser = apache_log_parser.make_parser("%h - -")
        with open(self.path, 'r') as f:
            for line in f:
                print(line_parser(line))  
        config()      


#17.58.97.174 - - [10/Mar/2019:07:32:44 +0100] "GET /tag/bash/ HTTP/1.1" 500 3821 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)"                   