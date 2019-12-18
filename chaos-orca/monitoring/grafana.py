import os

# Package import
import docker

# Local import
import config
from misc import common_helpers as common
#import monitoring.prometheus_targets as monitoring_targets

docker_client = docker.from_env()
dir_name = os.path.dirname(os.path.abspath(__file__))

grafana_name = '%s.grafana' % config.BASE_NAME

def start():
    '''Starts grafana container'''
    grafana = docker_client.containers.run(
        'grafana/grafana:latest',
        detach=True,
        name=grafana_name,
        ports={'3000': config.GRAFANA_PORT}, # <inside-port>:<outside-port>
        #publish= No need to publish ports, as it will later share a network with Prometheus.
        environment=['GF_SECURITY_ADMIN_PASSWORD='+config.GF_SECURITY_ADMIN_PASSWORD, 'GF_USERS_ALLOW_SIGN_UP='+config.GF_USERS_ALLOW_SIGN_UP],
        remove=True,
        volumes={
        'grafana_data': {'bind': '/var/lib/grafana', 'mode': 'rw'},
        dir_name+'/grafana/provisioning': {'bind':'/etc/grafana/provisioning/', 'mode': 'rw'}
        }
    )

    # Connect grafana to prometheus network.
    docker_client.networks.get(config.MONITORING_NETWORK_NAME).connect(grafana)

    grafana.reload()
    ip = common.getIpFromContainerAttachedNetwork(grafana, config.MONITORING_NETWORK_NAME)
#    monitoring_targets.add('%s:8080' % ip, 'grafana')
    print('Created grafana instance')


def getContainer():
    '''Returns the running container else None.'''
    try:
        return docker_client.containers.get(grafana_name)
    except Exception:
        return None

def stop():
    '''Stops grafana'''
    container = getContainer()
    if container is not None:
        container.stop()
#    monitoring_targets.remove('grafana')

    print('Stopped grafana')
