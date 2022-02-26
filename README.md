# Reproduction repo for a `pip-tools` bug

Issue: TODO

## Companion repositories:

- https://github.com/RedRoserade/pip-tools-repro-repo-b
- https://github.com/RedRoserade/pip-tools-repro-repo-c

## Testing this

1. Create a Virtual Environment (this has been tested on Python 3.10, but 3.8 shows the same issue)
2. Use the scripts `compile-XYZ.sh` to compile the associated `requirements-XYZ.txt` files
3. Investigate the output

## Notes

Repository `B` has two relevant branches that serve as variants:

- `test/pep-440-url`: https://github.com/RedRoserade/pip-tools-repro-repo-b/tree/test/pep-440-url
- `test/remove-c-dep`: https://github.com/RedRoserade/pip-tools-repro-repo-b/tree/test/remove-c-dep

They are referenced (commented out) in [requirements.in](./requirements.in).

Also, for `pip-tools<6.5`, `pip<22` is installed to prevent incompatibilities.
