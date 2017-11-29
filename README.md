# python_vector

```python
vector_a = Vector((x, y, z))
vector_b = Vector((x, y, z))

# Operations with scalar
1+vector_a => Vector((x+1, y+1, z+1))
5*vector_a => Vector((5*x, 5*y, 5*z))
vector_a/2 => Vector((x/2, y/2, z/2))

# Addition
vector_a + vector_b
vector_a - vector_b

# Scalar product
vector_a * vector_b

# Vectorial product
vector_a ^ vector_b

# Random vector
Vector.rand()

# Iterator
for coord in vector_a:
  print(coord)
  # x
  # y
  # z
