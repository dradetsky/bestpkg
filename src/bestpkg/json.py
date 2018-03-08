try:
    import simplejson as json
except (ImportError, ModuleNotFoundError):
    import json

for key in dir(json):
    globals()[key] = getattr(json, key)
