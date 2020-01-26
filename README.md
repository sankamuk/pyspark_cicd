
# PySpark CICD Project

A sample PySpark project ready for production deployment. This can help you develop your favorite PySpark Application with your enterprise CICD pipeline.

## Contents


## Overview


## Build


## Usage 

```
PROJECT_HOME=$(pwd)
${SPARK_HOME}/bin/spark-submit app.py --job stream --job-args srctype=csv srcschema=names:string srcpath=${PROJECT_HOME}/sampledata
```

## Acknowledgements and Further Reading
