from click import command, option, argument, echo, style, File
from pyfiglet import Figlet

from app.core import Compiler

compiler = Compiler()


@command()
@option('--version', is_flag=True, help='Print compiler version')
def info(version):
    """ Display compiler information """

    figlet = Figlet(font='isometric3')
    echo(style(figlet.renderText('ASMC'), fg='red'))

    echo('Assembly-Compiler (ASMC)')
    echo('Apache Licence 2.0 2019 Philipp Baszuk')

    if version:
        echo('Version {}'.format(compiler.version))


@command()
@option('--no-pretty-print', is_flag=True, help='Disable pretty printing')
@argument('source', type=File('r'))
@argument('binary', type=File('w'), required=False)
@argument('listing', type=File('w'), required=False)
def compile_file(source, binary, listing):
    """ Compile file """
    pass


if __name__ == '__main__':
    info()
    compile_file()
