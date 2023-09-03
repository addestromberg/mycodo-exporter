# Prometheus Exporter for Mycodo

Searches for all input and output devices and publishes input measurements and output states to server.

Metrics can be found at ```http://127.0.0.1:8000/metrics``` (Default)

You can change the port from config file.

an ```.env``` is needed with the variable set to you API key. Remove the ```.example``` from filename and paste your generated API key.

Can in theory be run from any server but is only tested on local network.

Read more about (prometheus)[https://prometheus.io/] and how to setup ie a (grafana agent)[https://grafana.com/docs/agent/latest/]