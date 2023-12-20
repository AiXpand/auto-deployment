#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import subprocess
import sys

def get_hostname():
  try:
    hostname = subprocess.check_output('hostname', shell=True).decode().strip()
    return hostname
  except Exception as e:
    return str(e)

def main():
  module = AnsibleModule(
    argument_spec={}
  )


  hostname = get_hostname()
  result = dict(
    changed=False,
    # ansible_facts is the reserved key, can be other but not really recommended
    ansible_facts=dict( 
      remote_hostname=hostname,
      remote_python=sys.version,
      remote_os=sys.platform,

    )
  )
  module.exit_json(**result)

if __name__ == '__main__':
  main()
