import os
import shutil


def file_transferring(file_list, from_dir, to_dir):
    """
    Transfer/Moving (not copy) file that list in file_name from from_dir to to_dir
    :param to_dir: string
    :param from_dir: string
    :type file_list: list of string
    :return TRUE or FALSE
    """
    if not os.path.isdir(to_dir) or not os.path.isdir(from_dir):
        print("Path is invalid")
        return False

    for file_name in file_list:
        if not os.path.exists(os.path.join(from_dir, file_name)):
            print(f'{file_name} not exist')
        else:
            file_path = os.path.join(from_dir, file_name)
            to_path = os.path.join(to_dir, file_name)
            shutil.move(file_path, to_path)

    return True


def file_transferring_all(from_dir, to_dir):
    """
    Transfer/Moving (not copy) all file from from_dir to to_dir
    :param to_dir: string
    :param from_dir: string
    :return TRUE or FALSE
    """
    if not os.path.isdir(to_dir) or not os.path.isdir(from_dir):
        print("Path is invalid")
        return False

    if os.listdir(from_dir).__len__() == 0:
        print("Have no files to transfer")
        return False

    for file_name in os.listdir(from_dir):
        file_path = os.path.join(from_dir, file_name)
        to_path = os.path.join(to_dir, file_name)
        shutil.move(file_path, to_path)

    return True
