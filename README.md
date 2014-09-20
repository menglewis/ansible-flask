ansible-flask
=======================

This is a simple ansible configuration for running a Flask application. This can also be used for any Python WSGI application, but this case uses a simple Flask app as an example.


Requirements
------

To run locally through Vagrant, you need the following installed:

* Virtualbox
* Vagrant
* Ansible

If you are provisioning a server, you only need Ansible installed on your control machine.


Getting Started
------

To start the VM, go to the ansible directory and use vagrant up.

    $ cd ansible
    $ vagrant up
    
If you ever make changes to the ansible configuration and want to update your VM, use vagrant provision

    $ vagrant provision
    


