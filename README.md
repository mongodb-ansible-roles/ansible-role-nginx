Ansible role for nginx
==================================

Installs nginx from source

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nginx/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nginx/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nginx/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nginx/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `nginx_version` | Version of nginx to install | string | `1.18.0` | true |

Dependencies
------------

You must have C build tools installed, for example: `build-essential` on Debian based systems
You must also install `libpcre3-dev` and `zlib1g-dev` to build properly

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-nginx
      vars:
        nginx_version: 1.18.0
```

RHEL 7
------

This role is required for `rhel70` because installing `nginx` via `yum` will update OpenSSL to 1.0.2 and the server project requires version 1.0.1. By installing from source, OpenSSL's version is preserved.

License
-------

[Apache License](LICENSE)
