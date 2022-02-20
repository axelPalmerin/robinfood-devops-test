import sys
sys.path.append('.')
from defs import constants as c

class TestCases(object):

    '''
    tests:
     check app structure folder and their files
     check python package is installed
    '''

    def test_project_dir(self):
        assert c.host.file("/app").is_directory

    def test_main_exist(self):
        assert c.host.file("main.py").exist

    def test_requirements_exist(self):
        assert c.host.file("requirements.py").exist

    def test_dockerfile_exist(self):
        assert c.host.file("Dockerfile").exist

    def test_check_pip(s):
        assert c.host.package("py3-pip").is_installed

    def test_python_pkg(s):
        assert c.host.package("python3").is_installed

    def test_python_link_pkg(s):
        assert c.host.package("python").is_installed
