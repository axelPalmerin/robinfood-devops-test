import sys
sys.path.append('.')
from defs import constants as c

class TestCases(object):

    def test_project_dir(self):
        assert c.host.file("/app").is_directory

    def test_check_pip(s):
        assert c.host.package("pip").is_installed

    def test_check_pip_tools(s):
        assert c.host.package("pip-tools").is_installed

    def test_python_pkg(s):
        assert c.host.package("python3").is_installed

    def test_ssh_running(s):
        assert c.host.service("docker").is_running

    def test_docker(self):
        c.host.docker.version()
