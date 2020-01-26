# Sample Aggregation Job
import os

def extract(spark, sourceType, inputSource):
  '''
    Usage:  Extract input into RDD
    Input:  Spark Session,
            Source File to be extracted
    Output: Extracted RDD
  '''
  print("Starting Extraction")
  if sourceType == 'json':
    inpRDD = spark.read.json(inputSource)    
  return inpRDD
  print("Completed Extraction")

def transform(spark, rdd):
  '''
    Usage:  Transforms input RDD
    Input:  Spark Session,
            Input RDD
    Output: Transformed RDD 
  '''
  print("Starting transformation")
  rdd.createOrReplaceTempView('temptable')
  spark.sql('select * from temptable').show()
  aggDataFrame = spark.sql('select avg(age) from temptable')
  print("Completed transformation")
  return aggDataFrame

def load(rdd):
  '''
    Usage:  Load analysis into destination
    Input:  Transformed RDD
    Output: None
  '''
  print("Starting Load")
  rdd.show()
  print("Completed Load")

# Main 
def analyze(spark):

  print("Running aggregate")

  # Collect Input
  arg = os.environ.get('PYSPARK_JOB_ARGS', None)
  jobArgs = dict()
  if arg :
    argsTuples = [arg_str.split('=') for arg_str in arg.split(' ')]
    jobArgs = {a[0]: a[1] for a in argsTuples}
  print("Arguments Passed: ")
  print(jobArgs)
  sourceType = jobArgs['srctype']
  sourceFile = jobArgs['srcfile']

  # ETL
  extractedRDD = extract(spark, sourceType, sourceFile)
  transformedRDD = transform(spark, extractedRDD)
  load(transformedRDD)

  print("Completed aggregate")
