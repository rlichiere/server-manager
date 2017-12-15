# server-manager
Host and docker containers manager


# Release Notes

## 0.0.1

### server-manager
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

### Infra
* use only 1 mysql & 1 phpmyadmin container
  * check/modify all docker-compose.yml :
    * use same mysql port everywhere
    * add env.name for each database name
* manage servermanager like django-chess app
  * split to dev/preprod/prod folders
  * adapt each docker-compose.yml

## 0.0.2

### ServerManager
* added core app
  * manages environment configuration
  * manages static configuration
  * manages dynamic configuration
* manage database switch sqlite/mysql
* improved config so as 
  * it is initialized by environment variables
  * then it is updated from core/config/config.yml 
  * then it is updated from core/config/config_private.yml 
* manage allowed_hosts in config
* manage secret_key in config
* added core.utils

### Dockerfile
* added ENV
  * DB_TYPE: sqlite/mysql
  * DEBUG: True/False


# Todo

## ServerManager
* improve core app
  * improve dynamic configuration
  * improve core utils

## ContainerManager
  * sqlite / mysql
  * switchable with a configurable option

* define models
  * Configuration
    * projects_root
  * Container
    * name

* create a generic app (or module ?) to centralize:
  * container initialization commands (create_superuser, etc)

* manage a configuration root

## Infra
* manage complete backup in zip

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
    