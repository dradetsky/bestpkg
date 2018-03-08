bestpkg: more stupid module tricks
==================================

building on the idea in `best-re`, a library of package import
fallbacks

example:

```
# tries simplejson, falls back to stdlib json
from bestpkg.json import json
# tries pyre2/re3/whatever, falls back to stdlib re
from bestpkg.re import re
```

not that i plan to use this in real code or particularly think anyone
else will; mostly just a working example/aide memoire.
