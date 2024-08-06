#!/usr/bin/python3

from local_lib.path import Path

if __name__ == "__main__":
    folder = Path("myfolder")
    folder.mkdir_p()
    file = folder / "myfile.txt"
    file.touch()
    file.write_text("Thanks for your time evaluating me :)\n")
    print(file.read_bytes().decode("utf-8"))

