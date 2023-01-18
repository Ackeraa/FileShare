import argparse
import os

def generate_unique_name():
    return os.urandom(7).hex()

def save(filename, name1, name2):
    with open(filename, 'a') as f:
        f.write(name1 + ': ' + name2 + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="the name of the folder")
    args = parser.parse_args()

    # get the name of the folder
    folder_name = args.name

    # generate a unique name
    while unique_name := generate_unique_name():
        if not os.path.exists(unique_name):
            break

    # create a folder with the unique name
    os.makedirs(os.path.join("share", unique_name))

    # save unique name: folder name to a file
    save(os.path.join("share", "match.txt"), unique_name, folder_name)
