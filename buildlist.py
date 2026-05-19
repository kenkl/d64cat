#!/usr/bin/env python3
# walk the directory tree and get directory listings for the .d64 images in the current directory and subdirectories, and write them to... a file? a database? a spreadsheet? TBD.

import struct, sys

def get_sector_offset(track, sector):
    """Calculates the byte offset in a .d64 file for a given track and sector."""
    # Sector counts per track for a standard 35-track D64
    if 1 <= track <= 17:
        offset = (track - 1) * 21 + sector
    elif 18 <= track <= 24:
        offset = 17 * 21 + (track - 18) * 19 + sector
    elif 25 <= track <= 30:
        offset = 17 * 21 + 7 * 19 + (track - 25) * 18 + sector
    elif 31 <= track <= 35:
        offset = 17 * 21 + 7 * 19 + 6 * 18 + (track - 31) * 17 + sector
    else:
        return None
    return offset * 256

def petscii_to_ascii(data):
    """Converts Commodore PETSCII strings to readable ASCII."""
    return "".join([chr(b) if 32 <= b <= 126 else "." for b in data]).strip()

def read_d64_directory(file_path):
    with open(file_path, "rb") as f:
        # 1. Get Disk Name (Track 18, Sector 0, Offset 144)
        f.seek(get_sector_offset(18, 0) + 144)
        disk_name = petscii_to_ascii(f.read(16))
        print(f"--- DISK NAME: {disk_name} ---")
        print(f"{'Type':<6} {'Size (Blocks)':<15} {'Filename'}")
        print("-" * 40)

        # 2. Iterate through Directory Sectors (Track 18, Sectors 1-18)
        current_track, current_sector = 18, 1
        
        while current_track != 0:
            f.seek(get_sector_offset(current_track, current_sector))
            sector_data = f.read(256)
            
            # The first two bytes point to the next track/sector of the directory
            next_track = sector_data[0]
            next_sector = sector_data[1]

            # Each sector contains 8 entries of 32 bytes each
            for i in range(0, 256, 32):
                entry = sector_data[i:i+32]
                file_type_raw = entry[2]
                
                # If file type is 0, the entry is empty/deleted
                if file_type_raw == 0:
                    continue

                # Parse file metadata
                # Types: 0=DEL, 1=SEQ, 2=PRG, 3=USR, 4=REL
                types = ["DEL", "SEQ", "PRG", "USR", "REL"]
                file_type = types[file_type_raw & 0x07]
                filename = petscii_to_ascii(entry[5:21])
                blocks = struct.unpack("<H", entry[30:32])[0]

                print(f"{file_type:<6} {blocks:<15} {filename}")

            current_track, current_sector = next_track, next_sector

def get_all_d64_files():
    """Walks the current directory and subdirectories to find all .d64 files."""
    import os
    d64_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(".d64"):
                d64_files.append(os.path.join(root, file))
    return d64_files

# Usage
# read_d64_directory("your_game_disk.d64")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python buildlist.py <d64_file>")
        sys.exit(1)
    read_d64_directory(sys.argv[1])