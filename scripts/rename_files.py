#!/usr/bin/env python3
import os
import re

def rename_files_with_spaces(directory="blog"):
    """
    Rename all markdown files in the given directory, replacing spaces with underscores.
    """
    renamed_files = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.md') and ' ' in filename:
            old_path = os.path.join(directory, filename)
            # Replace spaces with underscores
            new_filename = filename.replace(' ', '_')
            new_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_path, new_path)
                renamed_files.append((filename, new_filename))
                print(f"✅ Renamed: {filename} → {new_filename}")
            except OSError as e:
                print(f"❌ Error renaming {filename}: {e}")
    
    if renamed_files:
        print(f"\n✅ Successfully renamed {len(renamed_files)} files")
    else:
        print("\nℹ️ No files needed renaming")

if __name__ == "__main__":
    rename_files_with_spaces() 