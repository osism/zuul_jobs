# shellcheck

Find all shell scripts in a repository and run `shellcheck` against this shell scripts.
Define rules that should skipped in the defaults like this:

```yaml
---
# defaults file for shellcheck
zuul_work_dir: "{{ zuul.project.src_dir }}"
exclude_rules: -e SC1091,SC2034,SC1090
```
