import os
import click

from utilities.utility import get_folder_path
from utilities.readFile import read_file
from utilities.yaml_lib import write_yaml
from utilities.textParsing import check_language, tokenization, lemmatize, simple_parse, count_words


@click.command()
@click.help_option('-h', '--help')
@click.version_option('2.0', '-v', '--version', message='%(prog)s v%(version)s')
@click.option('--filename', default=None, help='Insert the name of the file you want to analyze')
@click.option('--folder', default=None, help='Insert the folder name where your file are')
@click.option('--advance', default=False, help='Specify if you want to use the advance linguistic features')
@click.option('--stemming', default=True, help='If you want to stem the text')
def main(filename, folder, advance, stemming):
    """
    Main function for the program
    :return: Boolean (true or false)
    """
    click.echo('\n --- Welcome to count words in a file!! --- \n')
    try:
        # Define the file name
        if filename is None or filename == '':
            filename = 'sonnet.txt'

        # Define the file path
        if folder is None or folder == '':

            input_path = get_folder_path('./')
        else:
            input_path = get_folder_path(os.path.join('./', folder))

        input_file_path = os.path.join(input_path, filename)

        # Read the file
        text = read_file(input_file_path)

        # Parse the text
        text = simple_parse(text)

        if advance or advance is 'True':

            print("\nRunning advance parsing...")

            # Check the language of the text
            language = check_language(text)

            # Tokenization
            text = tokenization(text, language, stemming=stemming)

            # Lemmatization
            text = lemmatize(text, language)

        # Count the words
        counter = count_words(text)
        print(f'\nResult: {counter}')

        # Export to yaml file the result
        write_yaml(input_path, 'ContaParoleResult.yml', counter)

        return True
    except Exception as message:
        print(f"Impossibile to start the program: {message}")
        return False


if __name__ == '__main__':
    main()
