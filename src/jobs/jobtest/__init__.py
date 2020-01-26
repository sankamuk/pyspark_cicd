# Sample Test Job
import os

def extract(sc):
  '''
    Usage:  Extract input into RDD
    Input:  Spark Context,
            Source File to be extracted
    Output: Extracted RDD
  '''
  print("Starting Extraction")
  inpRDD = sc.parallelize(range(10))
  return inpRDD
  print("Completed Extraction")

def transform(rdd):
  '''
    Usage:  Transforms input RDD
    Input:  Input RDD
    Output: Transformed RDD 
  '''
  print("Starting transformation")
  evennumbers = rdd.filter(lambda x: x % 2 == 0)
  print("Completed transformation")
  return evennumbers

def load(rdd):
  '''
    Usage:  Load analysis into destination
    Input:  Transformed RDD
    Output: None
  '''
  print("Starting Load")
  resultset = rdd.collect()
  print(resultset)
  print("Completed Load")

# Main 
def analyze(spark):

  sc = spark.sparkContext
  print("Running jobtest")

  # Collect Input
  arg = os.environ.get('PYSPARK_JOB_ARGS', None)
  jobArgs = dict()
  if arg :
    argsTuples = [arg_str.split('=') for arg_str in arg.split(' ')]
    jobArgs = {a[0]: a[1] for a in argsTuples}
  print("Arguments Passed: ")
  print(jobArgs)

  # ETL
  extractedRDD = extract(sc)
  transformedRDD = transform(extractedRDD)
  load(transformedRDD)

  print("Completed jobtest")


