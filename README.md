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

# Todo

## ContainerManager
* define models
  * Container
    * name

* create a generic app (or module ?) to centralize:
  * container initialization commands (create_superuser, etc)


## HostManager
* find interesting usages
