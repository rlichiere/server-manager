# server-manager
Host and docker containers manager


# Release Notes
## 0.0.1
* created initial files
* created main structure:
  * main app: servermanager
  * app containermanager
  * app hostmanager
* defined models
  * Application
    * name
    * label
    * git_repository_url
  * Environment
    * name
    * label
* added home view
* added front app
  * added Readme view
  * improved Applications view
* improved urls repartition

# Todo

## ContainerManager
* define models
  * Configuration
    * projects_root
  * Container
    * name

* create a generic app (or module ?) to centralize:
  * container initialization commands (create_superuser, etc)

* manage database switch
  * sqlite / mysql
  * switchable with a configurable option

* manage a configuration root

## Implement Applications actions

### User
* Up
* Down
* Update
* Promote

### Maintenance
* Pull
* Build
* Start
* Stop
* Remove

## Implement Application's Containers actions

### User
* Up
* Down
* Update
* Promote

### Maintenance
* Pull
* Build
* Start
* Stop
* Remove

## HostManager
* find interesting usages
  * list containers
    * docker ps
    * docker ps -a
  * list images
    * docker images
    * docker images -a
    