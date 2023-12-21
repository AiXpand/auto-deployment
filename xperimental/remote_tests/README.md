# Example of a remote-config playbook using a role

 1. Initialized with `ansible-galaxy init test-role`
 3. Added action plugin to `./test-role/action_plugins/`
 4. Added remote module tp `./test-role/library/`
 5. Finished playbook `./main.yml`
 6. Added Jinja inventory `./inventory.yml.j2` in `ansible.cfg`
 7. Added task for .env injection 