import os
import socket

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ipsec_service_running_and_enabled(host):
    ipsec = host.service("ipsec")
    assert ipsec.is_running
    assert ipsec.is_enabled


def test_ipsec_verify(host):
    with host.sudo():
        ipsec_verify = host.run("ipsec verify")
    assert ipsec_verify.rc == 0


def test_ipsec_connection_status(host):
    hostname = socket.gethostname()
    test_ip = '192.168.2.1' if hostname == 'test-gw-1' else '192.168.1.1'
    command = host.run('ping -c1 -W1 ' + test_ip)
    assert command.rc == 0
    assert '1 packets transmitted, 1 received' in command.stdout
