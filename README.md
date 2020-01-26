
# PySpark CICD Project

A sample PySpark project ready for production deployment. This can help you develop your favorite PySpark Application with your enterprise CICD pipeline.

## Overview

Today setting up an CICD enabled PySpark project is not always a simple task. Because of inherent deficulty in Testing Spark and enabling CICD for an Python project most of todays PySpark project avoid walking in this path. But for todays modern enterprise productionalising a non CICD enabled project is an antipattern. This is the problem this work tries to resolve.

***Features***:

- Spark and Spark SQL batch module development supported project.
- Multi Module PySpark Application, reduces the number of project created and groups module under an application.
- Unit Test support.
- Test Result and Coverage Report support.
- Setup tools to push project to PIP repository. Help you to use PySpark module in any application.
- Two Jenkins Pipeline (Declarative) for Build (SNAPSHOT) and Release.
- Oozie based job deployment support. Shell Action script and Workflow xml provided.
- Airflow based job deployment support. SparkSubmit Operator Dag submitted.

***Limitation***:
- Does not Streaming Job.


## Contents



## Build

Below are the requirement to build and release.

### Prerequesite

Note before you create Jenkins Jobs for your Build and Release of this project you should setup your Jenkins Build host with below requiements.

- Install Python3

```
$ sudo apt-get install python3
```

- Install Python Pip

```
$ sudo apt-get install python3-pip
```

- Install Python Virtual Environment support

```
$ sudo apt-get install python3-venv
```

- Setup Pip Repository definition file

Below setup consider you have running Pip Repository at *http://192.168.0.44:8880* with user *admin* and password *admin*.
If you want to quickly setup an dedicated Pip Repository for this project follow LINK.

```
$ cat > ~/.pypirc <<EOF
[distutils]
index-servers =
  pypi
  local

[pypi]
username:
password: 

[local]
repository: http://192.168.0.44:8880
username: admin
password: admin
EOF
```

- Setup Remote Git Repository Credential

User [LINK|https://jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials] to setup your credential with name ***Github***.

> Above commands are for Debian host, checkout in Internet for your platform specific commands.

### Build

Daily SCM Polled Snapshot build Jenkins Pipeline job can be scheduled by creating a Jenkins Pipeline with GIT SCM with Decrative script ***JenkinsfileBuild***. 


### Release

Release Jenkins Pipeline job can be scheduled by creating a Jenkins Pipeline with GIT SCM with Decrative script ***JenkinsfileRelease***. 


## Usage 

Below are the way to use the project:

### Manual Testing


```

# Environment Setup
export SPARK_HOME=[Location of Spark Home]
export PROJECT_HOME=[Location of Project]
export PYTHONPATH="${SPARK_HOME}/python/:${SPARK_HOME}/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH"
cd $PROJECT_HOME/test

# Initiate Testing
pytest --disable-pytest-warnings

```

### Manual Execution


```

# Environment Setup
export SPARK_HOME=[Location of Spark Home]
export PROJECT_HOME=[Location of Project]
cd $PROJECT_HOME/src

# To execute module Wordcount
${SPARK_HOME}/bin/spark-submit app.py --job aggregate --job-args srcfile=${PROJECT_HOME}/sampledata

# To execute module Aggregate
${SPARK_HOME}/bin/spark-submit app.py --job wordcount --job-args srctype=json srcfile=${PROJECT_HOME}/sampledata

```

### Oozie Job Deployment



### Airflow Job Deployment



## Acknowledgements and Further Reading
