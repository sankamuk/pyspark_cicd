#!/usr/bin/python
import argparse
import importlib
import time
import os
import sys
import pyspark
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession

if os.path.exists('pyspark_jobs_sample-1.0.0-py3-none-any.whl'):
  sys.path.insert(0, 'pyspark_jobs_sample-1.0.0-py3-none-any.whl')
else:
  sys.path.insert(0, './jobs')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='PySpark Job')
  parser.add_argument('--job', type=str, required=True, dest='job_name', help="The name of the job module.")
  parser.add_argument('--job-args', nargs='*', help="Extra arguments to send to the PySpark Job.")
  args = parser.parse_args()
  print("Called with arguments: %s" % args)

  environment = {
    'PYSPARK_JOB_ARGS': ' '.join(args.job_args) if args.job_args else ''
  }

  print('\n Job - %s \n Environment - %s\n' % (args.job_name, environment))

  os.environ.update(environment)
  sc = pyspark.SparkContext(appName=args.job_name, environment=environment)
  spark = SparkSession(sc)
  job_module = importlib.import_module('jobs.%s' % args.job_name)

  start = time.time()
  job_module.analyze(spark)
  end = time.time()

  print("\n Job - %s , Total Time - %s seconds" % (args.job_name, end-start))
