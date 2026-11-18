## Q-> What is the difference between a Python list and a NumPy array?

### A-> The fundamental difference between a Python list and a NumPy array comes down to performance and data types. Python lists are general-purpose, flexible containers, while NumPy arrays are highly optimized for numerical and scientific computing.

#### Data Types -> Python List -> Heterogeneous: Can hold mixed data types
#### Data Types -> NumPy Array -> Homogeneous: Elements must be of the same type

#### Data Types -> Python List -> Lower: Stores a collection of pointers to objects scattered in memory, adding overhead.
#### Data Types -> NumPy Array -> Higher: Stores data in contiguous blocks of memory, minimizing overhead.

#### Data Types -> Python List -> Slower: Mathematical operations require looping through each element individually.
#### Data Types -> NumPy Array -> Much Faster: Uses vectorized operations implemented in C, skipping Python loops entirely.

#### Data Types -> Python List -> Dynamic: Easily grows or shrinks by appending or removing items.
#### Data Types -> NumPy Array -> Fixed: Size is defined at creation; changing size generally requires creating a new array.

#### Data Types -> Python List -> Math Operations -> Requires list comprehensions or explicit for loops.
#### Data Types -> NumPy Array -> Math Operations -> Supports direct arithmetic.

## Q-> What does shape mean?
### A-> In NumPy, shape is an attribute of an array that returns a tuple representing the dimensions of that array. It tells you exactly how many elements exist along each axis (like rows and columns).

#### Why it matters for large datasets:
#### Knowing the shape is critical when doing mathematical operations on multiple arrays. For NumPy to multiply or add two arrays together efficiently, their shapes must either match exactly or be compatible through a process called "broadcasting."

## What is the difference between indexing and slicing?
### A-> Indexing is used to access a single, specific element from a list or array, while slicing is used to extract a range or subset of elements.

## Q-> What is broadcasting?
### A-> Broadcasting: NumPy automatically "stretches" smaller arrays to match larger ones so you can do math on them without loops.

## Q-> What is a dot product?
### A-> Dot Product: A single number that measures how much two vectors overlap or "point" in the same direction.

## Q-> What is cosine similarity?
### A-> Cosine Similarity: A metric that measures how similar two vectors are based on the angle between them, completely ignoring their overall size or magnitude.
### The Math: It takes the dot product of the two vectors and divides it by the product of their lengths (magnitudes).Cosine Similarity = (A · B) / (||A|| * ||B||)

## Q-> Why might NumPy be faster than Python loops for numerical work?
### A-> 