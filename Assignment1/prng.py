import time
import random

if __name__ == "__main__":
    while True:
        time.sleep(3)
        with open("prng.txt", "r") as f:
            lines = f.read().splitlines(True)
        if lines and lines[0] == "run":
            with open("prng.txt", "w") as fout:
                lines[0] = str(random.randint(0, 1000))
                fout.writelines(lines[0:])



