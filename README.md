# Hash Checker (SHA-256)

A simple Python CLI tool to generate, save, and verify SHA-256 hashes of files. Useful for detecting file modifications or ensuring integrity of important files.

Features:
- Generate SHA-256 hash for any file
- Save hashes to a local JSON database with timestamps
- Verify file integrity against saved hashes
- Colored console output for clarity
- Handles missing files gracefully

Requirements:
- Python 3.x
- colorama library

Install the dependency using pip:
pip install colorama

Usage:

1. Save a file hash:
python hash_checker.py -f example.txt --save
- Computes the SHA-256 hash of example.txt
- Saves it to hash_database.json with a UTC timestamp

2. Verify file integrity:
python hash_checker.py -f example.txt --verify
- Computes the current SHA-256 hash of the file
- Compares it against the saved hash in hash_database.json
- Displays whether the file is intact or has been modified
- Shows the timestamp of when the hash was saved

JSON Database Format:

[
    {
        "filename": "example.txt",
        "hash": "abc123...",
        "timestamp": "2026-01-06T22:45:30+00:00"
    }
]

- filename – the name of the file
- hash – SHA-256 hash of the file
- timestamp – UTC datetime when the hash was saved

Notes:
- This tool is meant for basic integrity checking, not enterprise forensics

License:
Free to use, modify, and distribute.
