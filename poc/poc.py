import os


def get_folder_size(folder):
    total_size = 0  # 遍历文件夹中的所有文件和子文件夹
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def main(folder_path):
    folder_sizes = {}
    # 获取文件夹中所有文件夹的大小
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folder_sizes[item] = get_folder_size(item_path)
    for folder, size in folder_sizes.items():
        print(f"{folder}: {size / (1024 * 1024):.2f} MB")  # 以 MB 为单位显示


if __name__ == "__main__":
    folderpath = r"C:\Users\TS-Runner\AppData"
    main(folderpath)
