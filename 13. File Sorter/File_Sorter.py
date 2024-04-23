import os
import shutil
import file_explorer


def create_folder(path: str, extension: str) -> str:
    """
    Creates a folder named after the extension
    If the folder exist before it will return its name otherwise it will make it.
    """

    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    """Sorts files in a given path"""
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)

    remove_empty_folders(source_path)
    file_explorer.ToplevelWindow()


def remove_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    fe = file_explorer.FileExplorer()
    fe.run()


if __name__ == '__main__':
    main()
