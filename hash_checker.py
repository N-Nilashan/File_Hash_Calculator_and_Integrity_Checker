import argparse
import hashlib

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

try:
    # Open the file in binary mode and read data
    if args.file is not None:
        with open(args.file, "rb") as file:
            data = file.read()

        # Generate SHA-256 hash of the file
        hash_file = hashlib.sha256(data)
        hash_code = hash_file.hexdigest()

        # Print the generated hash
        print(hash_code)

# Handle missing file error
except FileNotFoundError:
    print(f"✗ Error: File '{args.file}' not found")
    exit(1)

# If --save flag is used, attempt to save the file's hash
if args.save:
    # Boolean flag to track if the file is already in the database
    file_exists = False

    # Open the hash database in read mode to check for existing entries
    with open("hash_database.txt", 'r') as db:
        for line in db:
            # Split each line into filename and stored hash
            stored_file, stored_hash = line.strip().split('=')

            # Check if the current file is already in the database
            if args.file == stored_file:
                file_exists = True  # Mark as found
                break  # Stop checking further lines

        # If the file was found, notify the user
        if file_exists:
            print(f"{args.file} has already been saved!")
        else:
            # If not found, open the database in append mode and save the new hash
            with open("hash_database.txt", 'a') as writer:
                writer.write(f"{args.file}={hash_code}\n")  # Append the file and hash

# Verify file integrity if --verify flag is used
if args.verify:
    try:
        # Open hash database
        with open("hash_database.txt", 'r') as db_data:
            for line in db_data:
                # Split stored filename and hash
                stored_file, stored_hash = line.strip().split('=')

                # Match file name
                if stored_file == args.file:
                    # Compare hashes
                    if stored_hash == hash_code:
                        print("File integrity verified!")
                    else:
                        print("WARNING: File has been modified!")
                    break
            else:
                # File not found in database
                print("Error: File not found in database. Save it first with --save")

    # Handle missing database file
    except FileNotFoundError:
        print("The database file you are looking for is not found")
