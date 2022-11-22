import pytest
import os,sys

from functions import multiply_num


testdata = [([2,3] ,[6])]
@pytest.mark.parametrize("sample_input , expected_output" , testdata)

def test_multiply_num(sample_input , expected_output):
  print("Sample Input - " , sample_input)
  result = multiply_num(sample_input[0] , sample_input[1])
  print("Function Output - ", result)
  print("Expected Output - ", expected_output)
  assert result == expected_output[0]
