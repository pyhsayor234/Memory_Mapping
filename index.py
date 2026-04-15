import mmap

# Create/Open a file
with open("example.txt", "r+b") as file:
    
    # Map the file into memory
    mapped_file = mmap.mmap(file.fileno(), 0)

    # Read content from memory
    print("Original Content:")
    print(mapped_file.read().decode())

    # Move pointer to beginning
    mapped_file.seek(0)

    # Modify content directly in memory
    mapped_file.write(b"HELLO")

    # Close mapping
    mapped_file.close()