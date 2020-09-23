Ansible role for nginx
==================================

Installs nginx from source

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nginx/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nginx/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nginx/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nginx/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| name | desc | type | default | required |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-nginx
```

License
-------

[Apache License](LICENSE)
