import time
import os

if __name__ == "__main__":
    img_files = []

    for root, dirs, files in os.walk("./images"):
        for file in files:
            img_files.append(os.path.abspath(os.path.join(root, file)))
    while True:
        time.sleep(10)
        with open("image-service.txt", "r") as f:
            lines = f.read().splitlines(True)
        if lines and lines[0].isdigit():
            with open("image-service.txt", "w") as fout:
                lines[0] = img_files[int(lines[0]) % len(img_files)]
                fout.writelines(lines)

