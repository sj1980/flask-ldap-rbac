# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from ldap_rbac import RBACManager
from ldap_rbac.resources.ext.tinydb import TinyLogger, TinyResources
import settings
from tinydb import TinyDB
import bills

app = Flask(__name__)
app.config.from_object(settings)
logger = TinyLogger(db=TinyDB(settings.LOGGER_SOURCE))
resources = TinyResources(db=TinyDB(settings.RESOURCE_SOURCE), logger=logger)
app.resources = resources
manager = RBACManager(app, apis=[bills.api])
cors = CORS(app=app)


if __name__ == '__main__':
    app.run(debug=True)
