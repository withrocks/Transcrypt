# This is an ad-hoc test that will not be added to the pull request (separate branch)

# Run with transcrypt -b -m -e 6 -n test_enumerate.py, include in a page, then run `test_enumerate.enumerate_string()`
# within the page. It should fail with `shortest.map is not a function`.
#
# Merge the patch with git merge 326-zip-iterable. The it should write:
"""0 a
1 b
2 c"""


def enumerate_string():
    # Without the patch, this fails with an error of
    for ix, c in enumerate("abc"):
        print(ix, c)

