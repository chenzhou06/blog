from app import app
from flask_frozen import Freezer
import sys
import subprocess

if __name__ == "__main__":
    args = ["runserver", "build", "test", "deploy"]
    if len(sys.argv) > 1 and sys.argv[1] in args:
        if sys.argv[1] == "runserver":
            app.run()
        elif sys.argv[1] == "build":
            Freezer(app).freeze()
        elif sys.argv[1] == "test":
            p = subprocess.Popen("dir", stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True, shell=True)
            p.wait()
            print(p.returncode)
            print(p.stdout.read())
        elif sys.argv[1] == "deploy":
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
            print("Returncode: ".format(p.returncode))
    else:
        usage = "Usage:\n\trunserver\n\tbuild"
        print(usage)
