import json
import sys
from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

  TRANSFERS_FILES = False

  def run(self, tmp=None, task_vars=None):
    super(ActionModule, self).run(tmp, task_vars)

    result = super(ActionModule, self).run(tmp, task_vars)

    # Custom action logic
    args = self._task.args
    remote_data = args.get('remote_data', None)
    if remote_data is None:
      result['failed'] = True
      result['msg'] = 'remote_data is required'
    else:
      # dct_remote_data = json.loads(remote_data)
      REMOTE_KEY = "ansible_facts"
      dct_remote_data = remote_data # data is received via {{ remote_data }} in task
      dct_remote_results = dct_remote_data.get(REMOTE_KEY, {})
      result['changed'] = False
      result['processed_stuff'] = dct_remote_results    
      print('remote_data processed: \n{}'.format(json.dumps(dct_remote_data, indent=2)))
      result['msg'] = 'remote_data processed: {}'.format(dct_remote_results)
      result['remote_host'] = dct_remote_results.get('remote_hostname', "unknown")

    return result
