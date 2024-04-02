def custom_open(file_path, mode):
    try:
        file = open(file_path, mode, encoding="utf-8")
        return file
    except UnicodeDecodeError:
        print(f"Failed to decode file '{file_path}' with UTF-8. Falling back to GBK.")

    file = open(file_path, mode, encoding="gbk")

    return file
