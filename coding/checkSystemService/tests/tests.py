import sys
sys.path.append('.')
from defs import constants as c

class TestCases(object):

    '''
    Host constant can be a remote host.
    tests:
     check app structure folder and their files
     check installed python packages
    '''

    def test_project_dir(self):
        assert c.host.file("/app").is_directory

    def test_main_exist(self):
        assert c.host.file("main.py").is_file

    def test_requirements_exist(self):
        assert c.host.file("requirements.txt").exist

    def test_dockerfile_exist(self):
        assert c.host.file("Dockerfile").is_file

    def test_check_pip(s):
        assert c.host.package("pip").is_installed

    def test_python_pkg(s):
        assert c.host.package("python3").is_installed

    def test_python_link_pkg(s):
        assert c.host.package("python").is_installed
