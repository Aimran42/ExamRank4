# ExamRank4
### Level1 :py_array_rotation_detector

Assignment <br>
<p>
Write a Python function that takes two lists (arrays) as parameters and determines if the second list is a rotation of the first list (left or right).

A rotation means that the elements are shifted circularly. For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

The function must return True if arr2 is a rotation of arr1, and False otherwise.
If the arrays have different lengths, they cannot be rotations of each other.
Two empty arrays are considered rotations of each other.    
</p>

<br>Function signature<br>
```python
def array_rotation_detector(arr1: list, arr2: list) -> bool:
```


<br>Examples<br>

<br>Input<br>
```array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])```
<br>Output<br>
True

<br>Input<br>
```array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])```
<br>Output<br>
True

<br>Input<br>
```array_rotation_detector([1, 2, 3], [3, 2, 1])```
<br>Output<br>
False

<br>Input<br>
```array_rotation_detector([1, 2], [1, 2, 3])```
<br>Output<br>
False


<br>Input<br>
```array_rotation_detector([], [])```
<br>Output<br>

True

### Level1 :py_constellation_mapper

Assignment <br>
<p>
Write a function that maps a constellation of stars onto a grid and returns the visual representation as a list of strings.

The function should:
- Take a list of star coordinates as tuples (row, col) and grid size as integer
- Return a list of strings representing the grid
- Stars are represented by '*' and empty spaces by '.'
- Grid coordinates start from (0, 0) at top-left
- Ignore coordinates outside the grid boundaries
- Handle duplicate coordinates (star appears only once)
</p>

<br>Function signature<br>
```python
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
```
<br>Examples<br>

<br>Input<br>
```constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)```
<br>Output<br>
['*..', '.*.', '..*']

<br>Input<br>
```constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)```
<br>Output<br>
['.*.', '***', '.*.']

<br>Input<br>
```constellation_mapper([], 2)```
<br>Output<br>
['..', '..']

<br>Input<br>
```constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)```
<br>Output<br>
['*.', '.*']

<br>Input<br>
```constellation_mapper([(0, 0), (5, 5)], 3)```
<br>Output<br>
['*..', '...', '...']

<br>Input<br>
```constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)```
<br>Output<br>
['...', '***', '...']
