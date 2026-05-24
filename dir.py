#!/usr/bin/env python3
# Use the functions in buildlist.py to read the directory from a single .d64 file and print the directory listing to the console.

from buildlist import read_d64_directory

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python dir.py <d64_file>")
        sys.exit(1)
    
    file_path, disk_name, directory_entries = read_d64_directory(sys.argv[1])
    print(f"\nDirectory listing for {file_path} (Disk Name: {disk_name}):")
    print(f"{'Type':<6} {'Size (Blocks)':<15} {'Filename'}")
    print("-" * 40)
    print(directory_entries)
