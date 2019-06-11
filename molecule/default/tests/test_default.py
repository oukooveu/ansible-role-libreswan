import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ipsec_service_running_and_enabled(host):
    ipsec = host.service("ipsec")
    assert ipsec.is_running
    assert ipsec.is_enabled

def test_ipsec_connection_status(host):
    command = host.command('ping -c1 -W1 192.168.2.1')
    assert '1 packets transmitted, 1 received, 0% packet loss' in command.stdout
    assert command.rc == 0
