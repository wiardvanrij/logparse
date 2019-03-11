from . import parseFile

def main():
    import os  
    import argparse

    parser = argparse.ArgumentParser(description="Parse log files")

    parser.add_argument('path',
                    help='Path')                

    args = parser.parse_args()

    # Todo - add args for ini file

    if os.path.isfile(args.path):
        parseFile(args.path)
    else:
        print("File does not exist")

      