try:
    import re2 as re
except (ImportError, ModuleNotFoundError):
    import re

for key in dir(re):
    globals()[key] = getattr(re, key)
