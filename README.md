# ansible-temple

Sélecteur de playbooks Ansible. Le programme lit un dépôt catalogue, affiche les services sur toute la largeur du terminal, et lance `ansible-playbook` sur cette machine.

Le dépôt suit ce contrat :

```text
manifest.json
playbooks/<id>/info.json
playbooks/<id>/main.yml
```

Le catalogue de référence est <https://github.com/elestranobaron/wp-package-installator-playbooks>. Une autre adresse est acceptée si le dépôt a la même forme.

```bash
ansible-temple
ansible-temple https://github.com/exemple/catalogue
```

La dernière adresse est gardée dans `~/.config/ansible-temple/repository`. La copie du dépôt est dans `~/.cache/ansible-temple/catalog`.

Licence : GPL-3.0-or-later.
