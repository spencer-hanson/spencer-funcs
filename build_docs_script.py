import os
import subprocess


def main():
    os.chdir("docs")

    subprocess.run(["make", "clean"])
    # subprocess.run(["make.bat", "clean"])

    print("Generating API docs..")
    subprocess.run(["sphinx-apidoc", "-o", "source",  "../spencer_funcs", "-f"])

    print("Generating HTML docs..")

    subprocess.run(["sphinx-build",  "-b", "html", "source", "build"])

    print("Making HTML docs..")
    # TODO Might need a different command on Linux/Mac, try uncommenting below line and commenting
    #  out the 'make.bat' line

    subprocess.run(["make", "html"])
    # subprocess.run(["make.bat", "html"])

    print("Done!")


if __name__ == "__main__":
    main()
