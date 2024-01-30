import sys

import hiyapyco

conf = hiyapyco.load(
    ".ansible-lint",
    sys.argv[1],
    method=hiyapyco.METHOD_MERGE,
    interpolate=True,
    failonmissingfiles=True,
)
with open(".ansible-lint", "w+") as fp:
    fp.write(hiyapyco.dump(conf, default_flow_style=True))
