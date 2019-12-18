import os
import time

# Package imports
import click

# Local imports
from perturbations import commands as p_cmd
from monitoring import commands as c_cmd
from metrics import commands as m_cmd
from misc import container_api
from misc import click_autocompletion as cauto

@click.group()
def main():
    '''ChaosOrca - Tool made by JSimo'''
    pass

#
# Application commands
#
@main.command()
def list():
    '''List all containers relevant to chaosorca currently running'''
    print([c.name for c in container_api.list()])

@main.command()
def flist():
    '''List all container that can be attacked'''
    print([c.name for c in container_api.filteredList()])

@main.command()
def clist():
    '''Return all containers with chaos in them'''
    print([c.name for c in container_api.getChaosContainers()])

main.add_command(p_cmd.fault) # Fault injection commands.
main.add_command(c_cmd.prom) # Prometheus start/stop/more.
main.add_command(c_cmd.monit) # Monitoring start/stop/more.
main.add_command(m_cmd.metric) # Metrics export from Prometheus.

if __name__ == '__main__':
    main()
