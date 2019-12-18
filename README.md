# ChaosOrca

Proyecto basado en el repo de ChaosOrca

ChaosOrca is an original chaos engineering system for Docker. Its key design principle is to work with untouched Dockers images. All the monitoring and pertirbations are done from the Docker host. It uses different capabilities of the Linux Kernel and the Docker architecture.

## Prepare the Docker images

Lo primero que tenemos que hacer es preparar las imágenes que vamos a necesitar para el experimento.

 1. bpftrace. Esta es la primera de las imágenes que hemos de construir.
 2. ftrace
 3. netm
 4. perf
 5. sysc
 6. sysm
 7. prometheus

## Install

 ```
 $ sudo pip install --editable .
 ```

## Execute

1. Rename `file_sd_config.json.sample` to `file_sd_config.json`
2. Run the orc application. `python main.py <commands>`

## Commands

prom - Handles launching/restarting Prometheus and launch of cAdvisor.
monit - Attach monitoring to container.
fault - Adds a syscall fault to a container.
metric - Extract different kind of csv formatted metrics from Prometheus.

Each command has subcommands cabable of doing different things.
