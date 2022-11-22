import pytest
import os,sys

from functions import add_num


testdata = [([1,2] ,[3])]
@pytest.mark.parameterize("sample_input , expected_output" , testdata)

def test_add_num(sample_input , expected_output):
  print("Sample Input - " , sample_input)
  result = add_num(sample_input[0] , sample_input[1])
  print("Function Output - ", result)
  print("Expected Output - ", expected_output)
  assert result == expected_output[0]
