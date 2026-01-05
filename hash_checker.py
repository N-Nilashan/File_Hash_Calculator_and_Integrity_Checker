import argparse
import hashlib
import json

from colorama import init, Fore, Back, Style
init(autoreset=True)

# Create argument parser
parser = argparse.ArgumentParser(description="Hash Checker")

# Argument for file input (required)
parser.add_argument('-f', '--file', required=True, help="Enter the file name")

# Flag to save hash to database
parser.add_argument('-s', '--save', action='store_true', help="Save the hash code to Data Base")

# Flag to verify file integrity
parser.add_argument('-v', '--verify', action='store_true', help="Verify the integrity of the file")

# Parse command-line arguments
args = parser.parse_args()


# If --save flag is used, attempt to save the file's hash
if args.save:
    with open(args.file, "rb") as file:
        fileData = file.read()

        # Generate SHA-256 hash of the file
        hash_file = hashlib.sha256(fileData)
        hash_code = hash_file.hexdigest()



    try:
        with open("hash_database.json", "r") as db:
            content = db.read().strip()
            if content:
                data = json.loads(content)
            else:
                data = []
    except FileNotFoundError:
        data = []  # empty database if file doesn't exist

    # Boolean flag to track if the file is already in the database
    file_exists = any(item["filename"] == args.file for item in data)

    if not file_exists:
        data.append({"filename": args.file,"hash": hash_code})
        with open("hash_database.json",'w') as db:
            json.dump(data,db,indent=4)
        print(Fore.GREEN + "Hash Code has been saved to the Data Base!")
        # Print the generated hash
        print(hash_code)
    else:
        print(Fore.RED + f"{args.file} has already been saved!")

# Verify file integrity if --verify flag is used
if args.verify:

    with open(args.file, "rb") as file:
        fileData = file.read()

        # Generate SHA-256 hash of the file
        hash_file = hashlib.sha256(fileData)
        hash_code = hash_file.hexdigest()

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
