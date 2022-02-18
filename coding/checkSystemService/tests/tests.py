import testinfra
from unittest import TestCase

class SomeChecks(TestCase):

    def test_passwd_file(self):
        passwd = self.host.file("/etc/passwd")
        assert passwd.contains("root")
        assert passwd.user == "root"
        assert passwd.group == "root"
        assert passwd.mode == 0o644

    def test_python_pkg(self):
        hostPackage = self.host.package("python3")
        assert hostPackage.is_installed

    def test_ssh_running(self):
        service = self.host.service("ssh")
        running = service.is_running
        assert running
