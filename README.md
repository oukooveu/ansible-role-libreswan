Ansible role: Libreswan
=========

Install Libreswan IPsec server for RedHat/CentOS.

Requirements
------------

None.

Role Variables
--------------

```
ipsec_connections:
  test:
    local_gateway_ip: '172.16.100.17'
    remote_gateway_ip: '172.16.100.33'
    psk: 'test123'
    options:
      leftsubnets: '192.168.17.0/24,192.168.220.0/24'
      rightsubnet: '192.168.18.0/24'
      authby: 'secret'
      auto: 'start'
      type: 'tunnel'
      ikelifetime: '8h'
      keylife: '1h'
      ike: 'aes128-sha1;modp1024'
      phase2alg: 'aes128-sha1;modp1024'
      keyingtries: '%forever'
      keyexchange: 'ike'
      dpddelay: '10'
      dpdtimeout: '30'
      dpdaction: 'restart_by_peer'
```

Dependencies
------------

None.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - libreswan
```

License
-------

Apache 2.0

Author Information
------------------

Daniil Kupchenko, kupchenko@gmail.com
