Memory Mapping is a technique used by an operating system to connect virtual memory addresses used by programs to physical memory locations in RAM (or sometimes disk-backed storage). It lets programs access data as though it were in normal memory while the OS handles the translation behind the scenes.

Simple Explanation

Think of memory mapping like this:

Your program says: "I need data at address 1000."
The OS checks its memory map and says:
"Virtual address 1000 actually points to physical RAM location 5000."
Main Uses of Memory Mapping
1. Virtual Memory Management
Converts virtual addresses to physical addresses.
Allows each program to think it has its own large memory space.
2. Memory-Mapped Files
A file on disk can be mapped into memory.
The program can read/write the file like a normal array in RAM instead of using repeated file I/O calls.
3. Hardware Communication (Memory-Mapped I/O)
Some hardware devices are controlled through specific memory addresses.
Writing to that address sends commands to the device.
Example