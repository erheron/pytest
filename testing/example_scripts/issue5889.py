import os

import pytest

os.mkdir("/tmp/issue5889/")
os.mkdir("/tmp/issue5889/empty_dir")
os.mkdir("/tmp/issue5889/test_dir")
f = open("/tmp/issue5889/test_dir/test_file.py")

f.write("def test_bug():\n" "    assert True")
f.close()

pytest.main(
    [
        "-v",
        "-o",
        "testpaths=/tmp/issue5889/test_dir",
        "--rootdir=/tmp/empty_dir",
        "-k",
        "not empty_dir",
    ]
)
# outcome now: 0 tests run, 1 collected, 1 deselected, it's a bug!
# desired outcome: 1 collected, 1 run, OK
