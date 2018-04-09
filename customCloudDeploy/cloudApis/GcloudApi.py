
"""
This class connects to google cloud via http
and fire the respective queries

"""
class GcloudApi():
    """Cloud api methods defined here"""
    def __init__(self, arg):
        # super(GcloudApi, self).__init__()
        api_config = arg['api_config']
        self.api_config = api_config

    def get_cloud_api_config(self):
        return self.arg

    def create_vm_template(self, vm_config):
        pass

    def get_all_vm_template():
        pass

    def create_vm_instance_group(self, vm_config):
        pass

    def create_vm_instance(self, vm_config):
        pass

    def create_firewall_rule(self, firewall_config):
        pass

