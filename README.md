# ansible-temple

Terminal selector for an Ansible playbook catalogue. It reads a Git repository, lists the services across the full width of the screen, and runs `ansible-playbook` on this machine.

The repository follows this layout:

```text
manifest.json
playbooks/<id>/info.json
playbooks/<id>/main.yml
```

The reference catalogue is <https://github.com/elestranobaron/wp-package-installator-playbooks>. Another address is accepted when the repository has the same layout.

```bash
ansible-temple
ansible-temple https://github.com/example/catalogue
```

The last address is kept in `~/.config/ansible-temple/repository`. The checkout is kept in `~/.cache/ansible-temple/catalog`.

License: GPL-3.0-or-later.
