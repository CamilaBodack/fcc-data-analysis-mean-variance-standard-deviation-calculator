# Mean-Variance-Standard Deviation Calculator

[FCC Data Analysis Challenge N. 1](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

---

[From FCC](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator):

```

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:


{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

Development
Write your code in mean_var_std.py. For development, you can use main.py to test your code.

Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience.

```

## Running locale

- Environment (virtual env recommended) running Python 3.
- Inside virtual env install the requirements 
  - ```sh
       pip install -r requirements.txt
    ```
- Running / testing 
  - ```sh
       python main.py
    ```
## Help ⛑

1. TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
   - ERROR: test_calculate (test_module.UnitTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "./test_module.py", line 10, in test_calculate
    self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")
    File "/usr/lib/python3.10/unittest/case.py", line 876, in assertAlmostEqual
    diff = abs(first - second)
    TypeError: unsupported operand type(s) for -: 'dict' and 'dict'

  - Solutions
    - All numpy arrays need to be converted using tolist() 
    - Check the returned dictionary if exists any key with '_' like:
       ```py 

            This will cause an error:
       
            return {
                'mean': [mean_rows, mean_cols, mean_all_axis],
                'variance': [variance_rows, variance_cols, variance_all_axis],
            👉  'standard_deviation': [std_rows, std_cols, std_all_axis],
                'max': [max_rows, max_cols, max_all_axis],
                'min': [min_rows, min_cols, min_all_axis],
                'sum': [sum_rows, sum_cols, sum_all_axis]
            }

            This will work:

            return {
                'mean': [mean_rows, mean_cols, mean_all_axis],
                'variance': [variance_rows, variance_cols, variance_all_axis],
            👉  'standard deviation': [std_rows, std_cols, std_all_axis],
                'max': [max_rows, max_cols, max_all_axis],
                'min': [min_rows, min_cols, min_all_axis],
                'sum': [sum_rows, sum_cols, sum_all_axis]
            }

        ```









