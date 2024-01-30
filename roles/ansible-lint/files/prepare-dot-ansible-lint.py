import sys

import hiyapyco

conf = hiyapyco.load(
    ".ansible-lint",
    f"{sys.argv[1]}/roles/ansible-lint/files/defaults-dot-ansible-lint",
    method=hiyapyco.METHOD_MERGE,
    interpolate=True,
    failonmissingfiles=True,
)
with open(".ansible-lint", "w+") as fp:
    fp.write(hiyapyco.dump(conf, default_flow_style=True))
