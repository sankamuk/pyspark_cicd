import pytest
import sys
sys.path.append('../src')

import jobs.wordcount
import jobs.jobtest
import jobs.aggregate

pytestmark = pytest.mark.usefixtures("spark_context", "spark_session")

# Function to test Word Count
def test_wordcount(spark_context):
  test_input = [
    ' hello spark ',
    ' hello again spark spark'
  ]

  input_rdd = spark_context.parallelize(test_input, 1)
  resultsrdd = jobs.wordcount.transform(input_rdd)
  results = {word: count for word, count in resultsrdd.collect()}
  expected_results = {'hello':2, 'spark':3, 'again':1}
  assert results == expected_results   

# Function to test Job Test
def test_jobtest(spark_context):
  test_input = [ 1, 2, 3, 7 ]

  input_rdd = spark_context.parallelize(test_input, 1)
  resultsrdd = jobs.jobtest.transform(input_rdd)
  results = resultsrdd.count()
  expected_results = 1
  assert results == expected_results

# Function to test Aggregate Job
def test_aggregate(spark_context, spark_session):
  test_input_RDD = spark_context.parallelize([('user3', 33), ('user2', 32),('user1', 31)])
  test_input_DF = spark_session.createDataFrame(test_input_RDD, ['name', 'age'])

  resultsrdd = jobs.aggregate.transform(spark_session, test_input_DF)
  results = resultsrdd.collect()[0][0]
  expected_results = 32
  assert results == expected_results
