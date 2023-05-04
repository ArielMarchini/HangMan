def copy_file_content(source_path: str, destination_path: str):
    """
    Copy the contents of one file to another file.

    Parameters:
    source_path (str): The path to the source file.
    destination_path (str): The path to the destination file.

    Returns:
    None
    """
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            destination_file.write(source_file.read())
