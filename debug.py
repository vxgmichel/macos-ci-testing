from packaging.tags import sys_tags as packaging_tags
from poetry.core._vendor.packaging.tags import sys_tags as poetry_tags

poetry_set = set(map(str, poetry_tags()))
packaging_set = set(map(str, packaging_tags()))
target_tag = "cp36-abi3-macosx_11_0_universal2"

print(f"Tags in poetry but not in packaging:")
for tag in poetry_set - packaging_set:
    print(f"- {tag}")
print()

print(f"Tags in packaging but not in poetry:")
for tag in packaging_set - poetry_set:
    print(f"- {tag}")
print()

print(f"Looking for {target_tag!r}:")
print(f"- in `sys_tags` provided by packaging: {target_tag in packaging_set}")
print(f"- in `sys_tags` provided by poetry: {target_tag in poetry_set}")
