from app import app
from flask_frozen import Freezer
import sys
import subprocess
import os
from datetime import datetime


BASEDIR = os.path.abspath(os.path.dirname(__file__))
PAGESDIR = os.path.join(BASEDIR, "app", "pages")


DEFAULT_EDITOR_PATH = "D:\\Program Files\\Notepad++\\notepad++.exe"


def build():
    Freezer(app).freeze()


def deploy():
    cmds = "winscp.com " + \
        "/command " + \
        "\"option batch abort\" " + \
        "\"open ftp://ftp194319:Cz650520@sk510.webcname.net\" " + \
        "\"synchronize " + \
        "remote d:\\projects\\web\\blog\\app\\build /web\" " + \
        "exit"
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)
    p.wait()
    if p.returncode == 0:
        print("Success!")
    else:
        print("Failed! Try again.")


def new(filename):
    def markdownmeta():
        meta_title = "title:\n"
        meta_published = "published: {0}\n".format(datetime.today())
        meta_tags = "tags:\n"
        return meta_title + meta_published + meta_tags

    filepath = os.path.join(PAGESDIR, filename)
    if os.path.isfile(filepath):
        return print("File already exists.")
    f = open(filepath, "w")
    f.write(markdownmeta())
    f.close()
    cmd = [DEFAULT_EDITOR_PATH, filepath]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     universal_newlines=True)


if __name__ == "__main__":
    args = ["runserver", "build", "test", "deploy", "new", "bad"]
    """
    bad: build and deploy
    """
    if len(sys.argv) > 1 and sys.argv[1] in args:
        if sys.argv[1] == "runserver":
            app.run()
        elif sys.argv[1] == "build":
            build()
        elif sys.argv[1] == "test":
            p = subprocess.Popen("dir", stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True, shell=True)
            p.wait()
            print(p.returncode)
            print(p.stdout.read())
        elif sys.argv[1] == "deploy":
            deploy()
        elif sys.argv[1] == "bad":
            print("building...")
            build()
            print("deploying...")
            deploy()
        elif sys.argv[1] and sys.argv[2]:
            new(sys.argv[2])
    else:
        usage = "Usage:\n\trunserver\n\tbuild"
        print(usage)
