import time

def eraseData(txtFile):
    with open(txtFile, "r") as f:
        lines = f.read().splitlines(True)
    with open(txtFile, "w") as fout:
        fout.writelines(lines[1:])

if __name__ == "__main__":
    while True:
        userInput = input("Input 1 or 2: ")

        if userInput == "1":
            time.sleep(3)
            with open("prng.txt", "w") as prngOut:
                prngOut.write("run")

            time.sleep(3)

            with open("prng.txt", "r") as prngIn:
                rn = prngIn.readline()

            eraseData("image-service.txt")

            with open("image-service.txt", "w") as imgSrvOut:
                imgSrvOut.write(rn)

            time.sleep(10)

            with open("image-service.txt", "r") as imgSrvIn:
                print(imgSrvIn.readline())

        elif userInput == "2":
            print("exit")

        else:
            print("Unknown option")







