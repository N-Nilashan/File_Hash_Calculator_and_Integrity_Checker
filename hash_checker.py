import argparse
import hashlib
import json

from colorama import init, Fore, Back, Style
init(autoreset=True)

def get_file_hash(filename):
    with open(filename,'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

parser = argparse.ArgumentParser(description="Hash Checker")

parser.add_argument('-f', '--file', required=True, help="Enter the file name")

parser.add_argument('-s', '--save', action='store_true', help="Save the hash code to Data Base")

parser.add_argument('-v', '--verify', action='store_true', help="Verify the integrity of the file")

args = parser.parse_args()


if args.save:
    hash_code = get_file_hash(args.file)
    


    try:
        with open("hash_database.json", "r") as db:
            content = db.read().strip()
            if content:
                data = json.loads(content)
            else:
                data = []
    except FileNotFoundError:
        data = []  # empty database if file doesn't exist

    file_exists = any(item["filename"] == args.file for item in data)

    if not file_exists:
        data.append({"filename": args.file,"hash": hash_code})
        with open("hash_database.json",'w') as db:
            json.dump(data,db,indent=4)
        print(Fore.GREEN + "Hash Code has been saved to the Data Base!")
        print(hash_code)
    else:
        print(Fore.RED + f"{args.file} has already been saved!")

if args.verify:

    hash_code = get_file_hash(args.file)

    try:
        with open("hash_database.json", "r") as db:
            content = db.read().strip()
            if content:
                data = json.loads(content)
            else:
                data = []
    except FileNotFoundError:
        print(Fore.RED + "The database file you are looking for is not found")
        exit(1)


    for item in data:
        if item["filename"] == args.file:
            if item["hash"] == hash_code:
                 print(Fore.GREEN + "File integrity verified!")
            else:
                print(Fore.RED + "WARNING: File has been modified!")
            break
    else:
        print(Fore.RED  + "Error: File not found in database. Save it first with --save")
