Role bacula_console
===================

[![Build Status](https://travis-ci.org/sedovandrew/ansible-role-bacula-console.svg?branch=master)](https://travis-ci.org/sedovandrew/ansible-role-bacula-console)

Installation and configuration Bacula Console

Role Variables
--------------

`bacula_console_version: 5.2.13` - version of Bacula Console

Connection to Bacula Director:

- `bacula_director_name: bacula-dir`
- `bacula_director_console_password: "@@DIR_PASSWORD@@"`
- `bacula_director_address: localhost`
- `bacula_director_port: 9101`

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: sedovandrew.bacula_console
           become: true
           bacula_director_console_password: "bacula console password"

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
