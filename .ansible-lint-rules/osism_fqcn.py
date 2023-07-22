"""Rule definition for usage of fully qualified collection names for FQCN."""

import os
import sys
from typing import Any, Dict, Optional, Union
import yaml

from ansiblelint.file_utils import Lintable
from ansiblelint.rules import AnsibleLintRule


class OsismFQCNRule(AnsibleLintRule):
    """Use FQCN for all actions."""

    id = "osism-fqcn"
    severity = "MEDIUM"
    description = "Check whether the long version is used in the playbook"
    tags = ["formatting"]

    def matchtask(
        self, task: Dict[str, Any], file: Optional[Lintable] = None
    ) -> Union[bool, str]:

        with open(
            f"{os.getcwd()}/.ansible-lint-rules/osism_fqcn_list.yaml", "r"
        ) as fp:
            try:
                data = yaml.safe_load(fp)
            except yaml.YAMLError as e:
                print(e)
                sys.exit(1)

        for category in data:
            if (
                task["action"]["__ansible_module_original__"]
                in data[category]
            ):
                return False

        return True
