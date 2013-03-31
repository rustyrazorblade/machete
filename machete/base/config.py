import os
import configobj

config = configobj.ConfigObj() # for interpreters

for f in [os.environ.get("MACHETE_CONFIG", ""), "machete.cfg", "/etc/machete.cfg"]:
    if os.path.isfile(f):
        config = configobj.ConfigObj(f)
        break
else:
    raise Exception("Config file not found")


