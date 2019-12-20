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

## Install

Build and install using the following command:

 ```
 $ sudo pip3 install -I --editable .
 ```

## Execute

1. Rename `file_sd_config.json.sample` to `file_sd_config.json`
2. Run the orc application. `python main.py <commands>`

## Commands

 * `fault` - Adds a syscall fault to a container.
 * `flist` - List all container that can be attacked.
 * `list` -  List all containers relevant to chaosorca currently running
 * `metric` - Extract different kind of csv formatted metrics from Prometheus.
 * `monit` - Attach monitoring to container.
 * `prom` - Handles launching/restarting Prometheus and launch of cAdvisor.

Each command has subcommands cabable of doing different things.

## Fault options

A perturbation is defined as a tuple `(s, e, d)` which describes how to perturb the container. Here

 * `s` is the system call,
 * `e` the error code and
 * `d` the delay to use.

Together with this perturbation there is a fourth parameter available which is the duration of the perturbation, by default set to 120 seconds.

In total the default duration of an experiment is therefore 6 minutes long. The selected time was used as to keep have enough time to compare metrics while enabling the ability to run many experiments within a reasonable time frame.

Together the parameters forms a large amount of available perturbations as there exists more than 300 available system calls and more than 100 different possible error codes.

This results in the necessity of picking a subset of these to use for the experiment runs.





Common system calls [Linux Syscall Reference](https://syscalls.kernelgrok.com/):

 * `open`, `write`, `writev`, `read`, `readv`, `sendfile`, `sendfile64`, `poll`, `select`

Common errors [All possible error codes](http://man7.org/linux/man-pages/man3/errno.3.html):

  * None, `EACCES`, `EPERM`, `ENOENT`, `EIO`, `EINTR`, `ENOSYS`

Common delays:

  * None, `1000`, `5000`

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
