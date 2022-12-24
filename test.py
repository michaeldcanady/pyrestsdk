import pkg_resources



def get_requirements():
    with open("requirements.txt", "r+") as file1:
        # Reading form a file
        print(str(file1.read()).split("\n"))

get_requirements()