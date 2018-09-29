import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bacula_console_is_installed(host):
    host.package("bacula-console").is_installed


def test_bacula_console_config_file(host):
    f = host.file('/etc/bacula/bconsole.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
