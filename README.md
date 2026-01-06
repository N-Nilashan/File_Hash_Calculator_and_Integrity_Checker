Hash Checker (SHA-256)

A simple Python CLI tool to generate, store, and verify SHA-256 file hashes.
Use it to detect file tampering or unauthorized changes. No fluff.

Features

Generate SHA-256 hash of any file

Save hashes to a local JSON database

Verify file integrity against saved hash
Colored terminal output for clarity

Requirements

Python 3.x

colorama

Install dependency:

pip install colorama

Usage
Save a file hash
python hash_checker.py -f example.txt --save

Verify file integrity
python hash_checker.py -f example.txt --verify

How It Works

Hashes are stored in hash_database.json

Each entry contains:

filename

SHA-256 hash

If the hash changes → file was modified

Notes

Always save a file before verifying it

Deleting hash_database.json resets everything

This tool is meant for basic integrity checking, not enterprise forensics

License

Free to use. Modify it. Break it. Improve it.