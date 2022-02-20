import sys
sys.path.append('.')
from defs import constants as c

class TestCases(object):

    def test_passwd_file(self, caplog):
        passwd = c.host.file("/etc/passwd")
        assert passwd.contains("root")
        assert passwd.user == "root"
        assert passwd.group == "root"
        assert passwd.mode == 0o644

    def test_python_pkg(s):
        hostPackage = c.host.package("python3")
        assert hostPackage.is_installed

    def test_ssh_running(s):
        service = c.host.service("docker")
        running = service.is_running
        assert running
