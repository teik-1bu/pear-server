# -*- coding: utf-8 -*-
import os

from flask_script import Manager
from PearServer import create_app

app = create_app()
manager = Manager(app)
project_root_path = os.path.join(os.path.dirname(app.root_path))


@manager.command
def run():
    """Run local server."""

    app.run(host='0.0.0.0', port=9998)


if __name__ == "__main__":
    manager.run()
