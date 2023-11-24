import argparse
from rich import print as rprint
from lib import utils

def run_solver():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="AOC main file <YEAR> <DayX>")
    parser.add_argument('-t', '--tokenfile', default = "./token.txt" )
    parser.add_argument('-i', '--input',default = "example.txt")
    parser.add_argument('-f', '--filetype', default="example")
    parser.add_argument('-y', '--year')
    parser.add_argument('-d', '--day')

    args = parser.parse_args()

    if (args.tokenfile == ""):
        rprint("token not present - get token and update file")
    
    if (args.input == ""):
        rprint("input file not entered")
    
    if (args.filetype == ""):
        rprint("file type not entered")
    
    else:
        ## check to see if either the example file or input file is there
        ## if not call up the site to pull down the correct file. 
        token = utils.load_token(args.tokenfile)
        print(token[0])
        out = utils.check_and_load_file(args.filetype,token[0],args.input,args.year,args.day)
        print(out)
        ##all is ready, add code to run_solver and execute
        run_solver()