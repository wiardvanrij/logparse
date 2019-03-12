from helper import readConfig
import apache_log_parser
import collections
from terminaltables import AsciiTable

class Parser:

    # Init the class with its path. Define the regex for the parser and init the dicts
    def __init__(self, path):
        self.path = path
        self.regex = readConfig('log', 'regex')
        self.dataList = { "remote_host" : {} , "status" : {}, "request_method" : {}, "request_header_user_agent" : {}, "request_url_path" : {} }

    def processLog(self):
        # define the regex
        line_parser = apache_log_parser.make_parser(self.regex)

        with open(self.path, 'r') as f:
            for line in f:    
                # Try to parse each line            
                try:
                    data = line_parser(line)
                except apache_log_parser.LineDoesntMatchException:
                    print("Bad regex / log file - Could not match regex with logfile")
                    break
                except:
                    print("Unknown error when trying to match regex with logfile")
                    break

                # All good, process the data per line
                self.__processData(data)

    def __processData(self, data):
        # We loop over the dataList and count the data
        for key,value in self.dataList.items():
            if data[key] not in self.dataList[key]:
                self.dataList[key][data[key]] = 1
            else:
                self.dataList[key][data[key]] += 1
                
    def printOut(self):
        # Again we loop over to get the most common(n) values and print this in a table
        for key,value in self.dataList.items():
            collection = collections.Counter(self.dataList[key]).most_common(10)
            
            tableData = AsciiTable(collection)
            tableData.inner_heading_row_border = False
            tableData.title = key
            print(tableData.table)
      