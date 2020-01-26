# Sample Word Count Example
import os

def extract(sc, inputSource):
  '''
    Usage:  Extract input into RDD
    Input:  Spark Context,
            Source File to be extracted
    Output: Extracted RDD
  '''
  print("Starting Extraction")
  inpRDD = sc.textFile(inputSource)
  return inpRDD
  print("Completed Extraction")

def transform(rdd):
  '''
    Usage:  Transforms input RDD
    Input:  Input RDD
    Output: Transformed RDD 
  '''
  print("Starting transformation")
  wordcounts = rdd.flatMap(lambda line: line.split()) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)
  print("Completed transformation")
  return wordcounts

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
  print("Running wordcount")

  # Collect Input
  arg = os.environ.get('PYSPARK_JOB_ARGS', None)
  jobArgs = dict()
  if arg :
    argsTuples = [arg_str.split('=') for arg_str in arg.split(' ')]
    jobArgs = {a[0]: a[1] for a in argsTuples}
  print("Arguments Passed: ")
  print(jobArgs)
  sourceFile = jobArgs['srcfile']

  # ETL
  extractedRDD = extract(sc, sourceFile)
  transformedRDD = transform(extractedRDD)
  load(transformedRDD)

  print("Completed wordcount")
