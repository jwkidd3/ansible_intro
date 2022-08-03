# Ansible course: setup

To make the course self-contained, a Vagrant file is provided. Vagrant makes
it easy to bootstrap barebones virtual machines with VirtualBox.

### Cautionary tale about NetworkManager

On some systems, NetworkManager will take over `vboxnet` interfaces and mess
everything up. If you're in this case, you should prevent NetworkManager from
trying to autoconfigure `vboxnet` interfaces. Just edit
`/etc/NetworkManager/NetworkManager.conf` (or whatever the NetworkManager
config is on your system) and add in section `[keyfile]`:

    unmanaged-devices=mac:MAC_OF_VBOXNET0_IF;mac:MAC_OF_VBOXNET1_IF;...

Then destroy Vagrant machines, restart NetworkManager and try again.

## Adding your SSH keys on the virtual machines

To follow this course, you'll need to have your keys in VMs root's
`authorized_keys`. While this is not absolutely necessary (Ansible can use
sudo, password authentication, etc...), it will make things way easier.

Ansible is perfect for this and we will use it for the job. However I won't
explain what's happening for now. Just trust me.

```bash
ansible-playbook -i step-00/hosts step-00/setup.yml
```

If you get "Connections timed out" errors, please check the firewall
settings of your machine.

If you get errors like:

```none
fatal: [192.168.33.10]: UNREACHABLE! => {"changed": false, "msg": "host key mismatch for 192.168.33.10", "unreachable": true}
```

then you probably already have SSH host keys for those IPs in your
`~/.ssh/known_hosts`. You can remove them with `ssh-keygen -R
<IP_ADDRESS>`.

Otherwise, juste type `yes` when prompted to access ssh host keys if
requested.

To polish things up, it's better to have an ssh-agent running, and add your
keys to it (`ssh-add`).

**NOTE:** We are assuming that you're using Ansible version v2.5+ on your local
machine. If not you should upgrade ansible to v2.5+ before using this
repository (or run under virtualenv).

To check your ansible version use the command `ansible --version`. The output
should be similar to the above:

```none
ansible 2.10.5
  ...
  python version = 3.8.5 (default, Jul 28 2020, 12:59:40) [GCC 9.3.0]
```
