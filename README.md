# mq-playground <!-- omit in toc -->

## prerequisites

- [Rancher Desktop](https://github.com/rancher-sandbox/rancher-desktop): `1.8.1`
- Kubernetes: `v1.26.3`
- kubectl `v1.26.0`
- Helm: `v3.11.2`
- [pdm](https://github.com/pdm-project/pdm): `2.4.8`

## setup

tl;dr: `bash scripts/up.sh`

### namespace

```sh
kubectl create namespace mq --dry-run=client -o yaml | kubectl apply -f -
```

### rabbitmq

follow the [bitnami rabbitmq chart](https://github.com/bitnami/charts/tree/master/bitnami/rabbitmq) to install rabbitmq

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

```sh
helm upgrade --install mq-rabbitmq bitnami/rabbitmq -n mq -f rabbitmq/values.yaml
```

verify the rabbitmq is running

```sh
kubectl port-forward --namespace mq svc/mq-rabbitmq 15672:15672
```

then visit `http://localhost:15672/` with credential

```sh
username: admin
password: admin
```

port forward to localhost

```sh
kubectl port-forward --namespace mq svc/mq-rabbitmq 5672:5672
```

### redis

follow the [bitnami redis chart](https://github.com/bitnami/charts/tree/master/bitnami/redis) to install redis

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

```sh
helm upgrade --install mq-redis bitnami/redis -n mq -f redis/values.yaml
```

verify the installation

```sh
kubectl exec -it svc/mq-redis-master -n mq -- redis-cli -h mq-redis-master -a admin_password scan 0
```

port forward to localhost

```sh
kubectl port-forward --namespace mq svc/mq-redis-master 6379:6379
```

## playground

### python celery

publish messages

```sh
cd py
pdm install
pdm run python producer.py
```

start the celery workers

```sh
pdm run celery -A proj worker -l INFO
```

## cleanup

tl;dr: `bash scripts/down.sh`

```sh
helm uninstall mq-redis -n mq
helm uninstall mq-rabbitmq -n mq
kubectl delete pvc --all -n mq
kubectl delete namespace mq
```

## references
