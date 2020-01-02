from click import group, option, argument, echo, style, File
from pyfiglet import Figlet
from yaml import dump


@group()
def converter():
    """ Driver converter """

    figlet = Figlet(font='isometric3')
    echo(figlet.renderText('ASMDC'))

    echo('\n' 'Assembly Driver Converter (ASMDC)')
    echo('Apache Licence 2.0 2019 Philipp Baszuk' '\n')


@converter.command()
@option('--no-header', is_flag=True, default=False, help='Disable output file header')
@argument('driver_file', type=File('r'))
@argument('output_file', type=File('w'))
def convert_file(no_header, driver_file, output_file):
    """ Convert driver file from cpu to yaml format """

    def echo_colored(text, color=None, *args, **kwargs):
        echo(style(text.format(*args, **kwargs), fg=color))

    lines = driver_file.readlines()

    if len(lines) == 0:
        echo_colored('Input file is not valid cpu driver', 'red')
        return

    output = {
        'constants': {},
        'addresses': {}
    }

    section = None

    for number, line in enumerate(lines, start=1):
        comment_index = line.find(';')
        if comment_index != -1:
            line = line[:comment_index]

        line = line.strip().lower()

        if line.find('=') != -1:
            name, value = list(map(lambda val: val.strip(), line.split('=')))

            if name in output['constants']:
                echo_colored(f'Error: constant {name} already defined at line {number}', 'red')
            else:
                output['constants'][name] = int(value) if value.isnumeric() else value
                echo_colored(f'Constant {name} = {value}', 'magenta')

        elif len(line.split(' ')) == 2:
            address, name = line.split(' ')

            if section is None:
                echo_colored(f'Error: address declaration ({name}) before section at line {number}', 'red')
            elif name in output['addresses'][section]:
                echo_colored(f'Error: address redeclaration ({name}) at line {number}', 'red')
            else:
                output['addresses'][section][name] = int(address) if address.isnumeric() else address
                echo_colored(f'Address {name} -> {address}', 'yellow')

        elif len(line) >= 1:
            section = line

            if section not in output['addresses']:
                output['addresses'][section] = {}

            echo_colored(f'Section {section}', 'blue')

        elif line != '':
            echo_colored(f'Error: invalid line {number}', 'red')

    if not no_header:
        output_file.write('# Assembly Driver File \n')

    output_file.write(dump(output, sort_keys=False))
    output_file.close()

    echo('\n' 'File has been converted')


if __name__ == '__main__':
    converter()
