def test_6376(testdir):
    testdir.copy_example("issue_6376.py")
    testdir.runpytest("issue_6376.py")
