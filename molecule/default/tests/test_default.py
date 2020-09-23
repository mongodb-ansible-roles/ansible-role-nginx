import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx(host):
    cmd = host.run("/usr/local/nginx/sbin/nginx -v 2>&1 | awk '{print $3}'")
    assert cmd.stdout == "nginx/1.18.0\n"
