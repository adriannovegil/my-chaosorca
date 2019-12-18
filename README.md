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

Build and install using the following command:

 ```
 $ sudo pip3 install --editable .
 ```

## Execute

1. Rename `file_sd_config.json.sample` to `file_sd_config.json`
2. Run the orc application. `python main.py <commands>`

## Commands

 * prom - Handles launching/restarting Prometheus and launch of cAdvisor.
 * monit - Attach monitoring to container.
 * fault - Adds a syscall fault to a container.
 * metric - Extract different kind of csv formatted metrics from Prometheus.

Each command has subcommands cabable of doing different things.

## Basic example

Following, you can see the necessary commands to execute a basic example using Nginx.

First, execute the `hello_world` container using the following command:

```
$ docker run -p 32768:80 -d --name=hello_world nginxdemos/hello
```

Start monitoring database and `cadvisor`.

```
$ chaosorca prom start
```

Attach the monitoring to the `hello_world` container

```
$ chaosorca monit start --name hello_world
```

View containers list

```
$ docker container ls
```

Open the app in chrome

```
$ xdg-open http://localhost:32768
```

Now, we can start the perturbation time :-P

```
$ chaosorca fault premade --name hello_world --cmd open:error=EACCES
```

Open the app again in chrome.

```
$ xdg-open http://localhost:32768
```

Stop perturbation.

```
$ chaosorca fault stop --all
```

Detach the monitoring

```
$ chaosorca monit stop --name hello_world
```

View containers.

```
$ docker container ls
```
