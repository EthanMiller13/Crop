import os


def remove_all():
    for file in os.listdir("images/user"):
        os.remove(f"images/user/{file}")
        print(file, "was removed from images/user")


remove_all()
