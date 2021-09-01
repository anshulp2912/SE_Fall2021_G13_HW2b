import os

print(os.getpwd())

def test_add():
    assert add(2, 3) == 5 , 'TEST_PASS'
    assert add('xyz','abc') != 'xyzabc' , "TEST_FAIL:Please enter numeric values only"
    
def test_subtract():
  assert subtract(10,4) == 6 , "TEST_PASS"
  
def test_multiply():
  assert multiply(10,6) == 60 , "TEST_PASS"
  assert multiply("abc",2) != "abcabc" , "TEST_FAIL:Please enter numeric values only"

def test_divide():
  assert divide(10,5) == 2 , "TEST_PASS"
