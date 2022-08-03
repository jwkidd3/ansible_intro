# Ansible course

Ansible is a configuration management software that lets you control and
configure nodes from another machine. What makes it different from other
management software is that Ansible uses (potentially existing) SSH
infrastructure, while others (Chef, Puppet, ...) need a specific PKI
infrastructure to be set up.

Ansible also emphasizes push mode, where configuration is pushed from a master
machine (a master machine is only a machine where you can SSH to nodes from) to
nodes, while most other CM typically do it the other way around (nodes pull
their config at times from a master machine).

This mode is really interesting since you do not need to have a 'publicly'
accessible 'master' to be able to configure remote nodes: it's the nodes
that need to be accessible (we'll see later that 'hidden' nodes can pull their
configuration too!), and most of the time they are.

This course has been tested with **Ansible 2.9**.

We're also assuming you have a keypair in your ~/.ssh directory.



## Complete explanations

### Installing Ansible

The reference is the [installation
guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

#### Using pip & virtualenv (higly recommended !)

The best way to install Ansible (by far) is to use `pip` and virtual
environments.

Then, install ansible via `pip`:

```bash
pip install ansible==2.7.1
```

(or use whatever version you want).


