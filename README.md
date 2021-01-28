
## Docker Example 3

### Building Image:
docker build -t jabil/docker-example-3 .

### Running Container:
docker run --name docker-example-3 jabil/docker-example-3
docker run --name docker-example-3 -p 8888:8888 jabil/docker-example-3
docker run --name docker-example-3 -p 8888:8888 -d jabil/docker-example-3

### Useful Commands:
* docker rm [container-name|container-id]
  Remove one or more containers
* rm $(docker ps -a -q)
  Remove all containers: docker 
* docker stop [container-name|container-id]
  Stop one or more running containers
* docker stop $(docker ps -a -q)
  Stop all containers:
* docker kill [container-name|container-id]
  Kill one or more running containers
* docker kill $(docker ps -a -q)
  Kill all containers: 
* docker start [container-name|container-id]
  Start one or more stopped containers
* docker logs [container-name|container-id]
  Fetch the logs of a container: 
* docker exec -it [container-name|container-id] bash
  Run a command in a running container: 

# AIOtests
