import json

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)

        result = super(ActionModule, self).run(tmp, task_vars)

        # Custom action logic
        args = self._task.args
        str_msg = args.get('key1', 'Nothing yet') 
        str_msg += ': ' + self.__class__.__name__
        result['msg'] = str_msg        
        result['changed'] = False
        dct_show = {
          k: v for k, v in task_vars.items() 
          if type(v) in [str, int, float, bool, list, dict]
        }
        str_dump = "\n".join(["{} ({}): {}".format(k, type(v), v) for k,v in dct_show.items()])
        str_dump = json.dumps(dct_show, indent=2)
        self._display.display("{}\nParams {}:\n{}".format(
          result['msg'],
          list(task_vars.keys()),
          str_dump
        ))

        return result
