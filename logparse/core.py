from parser import Parser
import os.path
import argparse
  
def main():
    # Defining cmdline argument parser
    argparser = argparse.ArgumentParser(description="Parse log files")
    argparser.add_argument('path', help='Path')                
    args = argparser.parse_args()
    
    # Check if log file exists and init our parser
    if os.path.isfile(args.path):
        try:
            # Init
            parser = Parser(args.path)
            # Start processsing
            parser.processLog()
            # Dump the data out
            parser.printOut()
        except:
            print("Failure on parser - unknown error")
    else:
        print("Log file does not exist")