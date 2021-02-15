import chardet


def read_file(file_path=None):
    """
    Read an input text file and return the text string
    :return:
    """
    try:
        # Get the encoding info's
        textraw = open(file_path, 'rb').read()
        encoder = chardet.detect(textraw)

        # Read the file
        file = open(file_path, 'r', encoding=encoder.get('encoding'))
        text = file.read()
        file.close()
        return text

    except Exception as message:
        print(f"Impossible to read from file: {message}")
        return None
