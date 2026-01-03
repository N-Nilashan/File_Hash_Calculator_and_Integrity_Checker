import argparse
import hashlib

parser = argparse.ArgumentParser(description="Hash Checker")
parser.add_argument('-f', '--file',required=True,help="Enter the file name")
parser.add_argument('-s','--save',action='store_true',help="Save the hash code to Data Base")
parser.add_argument('-v','--verify',action='store_true',help="Verify the integrity of the file")
args = parser.parse_args()

if args.file is not None:
    with open(args.file, "rb") as file:
        data = file.read()
    hash_file = hashlib.sha256(data)
    hash_code = hash_file.hexdigest()
    print(hash_code)

if args.save:
    with open("hash_database.txt",'w') as db:
        db.write(hash_code)
    print("Hash Code successfully saved to the Data Base")

if args.verify:
    with open("hash_database.txt",'r') as db_data:
        readStoredHash = db_data.read()
    if (readStoredHash == hash_code):
        print("File integrity verified!")
    else:
        print("WARNING: File has been modified!")


