class Test_Rootdir:
    def test_basic(self, testdir):
        dir_with_ini = testdir.mkdir("dir_with_ini")
        testdir.makefile(".ini", pytest="[pytest]\naddopts=-rs\n")
        dir_with_ini.mkdir("dir1")
        dir_with_ini.mkdir("dir1/dir11")
        tfile = testdir.makepyfile(
            """
            def test_one():
                assert True
        """
        )
        config = testdir.parseconfigure("--rootdir=dir_with_ini/dir1")
        assert config.rootdir.purebasename == "dir1"
        reprec = testdir.inline_run(tfile, "--rootdir=dir_with_ini/dir1")
        passed, skipped, failed = reprec.listoutcomes()
        assert len(skipped) == 0
        assert len(passed) == 1
        assert len(failed) == 0
