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
    if not os.path.isdir(from_dir):
        print(f"{from_dir} is invalid path")
        return False

    if not os.path.isdir(to_dir):
        print(f"{to_dir} is invalid path")
        return False

    num_file = len(file_list)
    for idx, file_name in enumerate(file_list):
        print(f'\r {idx}/{num_file}: {file_name} is tranferring')
        if not os.path.exists(os.path.join(from_dir, file_name)):
            print(f'\r {file_name} not exist')
        else:
            file_path = os.path.join(from_dir, file_name)
            to_path = os.path.join(to_dir, file_name)
            shutil.copy(file_path, to_path)

    return True


def file_transferring_all(from_dir, to_dir):
    """
    Transfer/Moving (not copy) all file from from_dir to to_dir
    :param to_dir: string
    :param from_dir: string
    :return TRUE or FALSE
    """
    if not os.path.isdir(from_dir):
        print(f"{from_dir} is invalid path")
        return False

    if not os.path.isdir(to_dir):
        print(f"{to_dir} is invalid path")
        return False

    if os.listdir(from_dir).__len__() == 0:
        print("Have no files to transfer")
        return False

    list_file = os.listdir(from_dir)
    num_file = len(list_file)
    for idx, file_name in enumerate(list_file):
        print(f'\r {idx}/{num_file}: {file_name} is tranferring')
        file_path = os.path.join(from_dir, file_name)
        to_path = os.path.join(to_dir, file_name)
        shutil.move(file_path, to_path)

    print()
    return True
