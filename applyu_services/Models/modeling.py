from conn import url
from sqlacodegen_v2 import generate_models

# update models from database
generate_models(
        url,"declarative",None,"/home/ted/Desktop/Applyu-Server/applyu_services/Models/data_mods.py")
