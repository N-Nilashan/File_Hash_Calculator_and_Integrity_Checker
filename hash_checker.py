import argparse
import hashlib
import json
from datetime import datetime

from colorama import init, Fore, Back, Style


# Initialize colorama for colored console output
init(autoreset=True)

# Function to calculate SHA-256 hash of a file
def get_file_hash(filename):
    try:
        with open(filename, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{filename}' not found")
        exit(1)

# Set up command-line argument parser
parser = argparse.ArgumentParser(description="Hash Checker")
parser.add_argument('-f', '--file', required=True, help="Enter the file name")  # File to hash/check
parser.add_argument('-s', '--save', action='store_true', help="Save the hash code to Data Base")  # Save hash
parser.add_argument('-v', '--verify', action='store_true', help="Verify the integrity of the file")  # Verify hash

# Parse the arguments
args = parser.parse_args()

# If user wants to save the hash
if args.save:
    hash_code = get_file_hash(args.file)  # Compute the hash
    timestamp = datetime.utcnow().isoformat() + 'Z'

    try:
        # Try to read existing database
        with open("hash_database.json", "r") as db:
            content = db.read().strip()
            data = json.loads(content) if content else []  # Load JSON or start with empty list
    except FileNotFoundError:
        data = []  # If database doesn't exist, start empty

    # Check if file already exists in database
    file_exists = any(item["filename"] == args.file for item in data)



    if not file_exists:
        # Append new file hash to database
        data.append({
            "filename": args.file, "hash": hash_code, "timestamp": timestamp
        })
        with open("hash_database.json", 'w') as db:
            json.dump(data, db, indent=4)
        print(Fore.GREEN + "Hash Code has been saved to the Data Base!")
        print(hash_code)
    else:
        # File already in database
        print(Fore.RED + f"{args.file} has already been saved!")

# If user wants to verify file integrity
if args.verify:
    hash_code = get_file_hash(args.file)  # Compute current hash
    
    try:
        # Load database
        with open("hash_database.json", "r") as db:
            content = db.read().strip()
            data = json.loads(content) if content else []  # Load JSON or empty list
    except FileNotFoundError:
        print(Fore.RED + "The database file you are looking for is not found")
        exit(1)

    # Check file hash against saved hash
    for item in data:
        if item["filename"] == args.file:
            if item["hash"] == hash_code:
                print(Fore.GREEN + f"File integrity verified! Saved at {item['timestamp']}")
            else:
                print(Fore.RED + "WARNING: File has been modified!")
            break
    else:
        # File not in database
        print(Fore.RED + "Error: File not found in database. Save it first with --save")
