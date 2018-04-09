
from customCloudDeploy.cloudApis import GcloudApi;
from customCloudDeploy.healthChecks import HealthChecks

#respective cloud config
cloud_config = {}
gcloudApi = new GcloudApi(cloud_config)
healthChecks = new HealthChecks()
# steps to deploy a app/service

#functions defs

# returns the application config
def get_app_config():
    return {}

#checks if the application template exists or not
def check_if_template_exists():
    return True

# creates the vm template
def create_vm_template():
    gcloudApi.create_vm_template()
    return True

# creats the vm instance group
def create_vm_group(template):
    gcloudApi.create_vm_instance_group(template)
    return True

# save the vm instance group ip's to internal database
def save_ip_to_db(vm_ip_list):
    return True

# builds the app with all its dependencies
def build_app_package():
    return True

# deploys app to vm instance group
def deploy_app_to_vm_group():
    return True

# setup health checks for the respective application
def setup_health_checks():
    return True

# add application to load balancer config
def add_app_to_load_balancer():
    return True

# remove application from load balancer config
def remove_app_from_load_balancer():
    return True

# kill the respective vm machine group
def kill_vm_group():
    return True
# executes the kill script of the respective application to do any clean if possible
def kill_app():
    return True



# starts the health checks for the respective application
'''
health checks can be of two types
1. vm machine health checks
2. application specific health checks
'''
def start_health_checks():
    config = {}
    healthChecks.start_health_checks()
    health_check_status = healthChecks.get_health_check_status()
    if (health_check_status.vm_machine && health_check_status.app)
        #all good keep monitoring
    else
        remove_app_from_load_balancer()
        kill_app()
        kill_vm_group()
        #reuse the build package
        config.build_app_package = False
        config.redeploy_app = True
        start_app_deploy(config)
        add_app_to_load_balancer()

def start_app_deploy(config):
    if config.template_exists
        # no need to create vm instance template for application
    create_vm_template()
    config.vm_ip_list = create_vm_group(app_config.template)
    save_ip_to_db(config.vm_ip_list)
    if config.build_app_package
        build_app_package()
    deploy_app_to_vm_group()
    if !config.redeploy_app:
        setup_health_checks(config)
        start_health_checks(config)



#flow of the program
deployement_config = {}
app_config = get_app_config()

deployement_config.template_exists = check_if_template_exists(app_config.template)
deployement_config.build_app_package = True
deployement_config.redeploy_app = False
start_app_deploy(deployement_config)



'''
components of custom cloud deploy
application configuration database (3 servers master slave configuration)
application deployment server (1 server)
application build/package server (1 server)
health check servers (3 servers monitor each other with master slave configuration)
log server (1 server)
internal load balancer server (1 server)
'''