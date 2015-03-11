from app import app
from flask_frozen import Freezer
import sys

if __name__ == "__main__":
    args = ["runserver", "build"]
    if len(sys.argv) > 1 and sys.argv[1] in args:
        if sys.argv[1] == "runserver":
            app.run()
        elif sys.argv[1] == "build":
            Freezer(app).freeze()
    else:
        usage = "Usage:\n\trunserver\n\tbuild"
        print(usage)
