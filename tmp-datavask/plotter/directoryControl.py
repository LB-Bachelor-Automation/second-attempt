from os import chdir
from subprocess import check_output
from matplotlib import rcParams

def directoryControl():
    git_root = check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
    chdir(git_root)

    rcParams["savefig.directory"] = "/figures"
    rcParams["savefig.format"] = "eps"

    
