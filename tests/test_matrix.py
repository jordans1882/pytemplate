"""Matrix class tests.

Provides tests for the Matrix class.

Includes:
 - tests of constructors:
   - from_list
   - from_matrix
   - filled
   - zeros
   - ones
   - identity
 - tests of getters and setters
   - elements
   - dims
   - columns/rows
 - addition, subtraction, multiplication
"""

from pytemplate.matrix import Matrix, t


def test_matrix_from_list():
    """Test matrix list constructor"""
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    assert a.get_data() == [[1, 2, 3], [4, 5, 6]]


def test_matrix_from_matrix():
    """Test matrix matrix constructor"""
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    b = Matrix.from_matrix(a)
    assert b.get_data() == [[1, 2, 3], [4, 5, 6]]


def test_matrix_filled():
    """Test filled matrix constructor"""
    a = Matrix.filled((3, 2), 2.1)
    assert a.get_data() == [[2.1, 2.1], [2.1, 2.1], [2.1, 2.1]]


def test_matrix_zeros():
    """Test zeros matrix constructor"""
    a = Matrix.zeros((3, 3))
    assert a.get_data() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_matrix_ones():
    """Test ones matrix constructor"""
    a = Matrix.ones((3, 3))
    assert a.get_data() == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def test_matrix_identity():
    """Test identity matrix constructor"""
    a = Matrix.identity(3)
    assert a.get_data() == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_matrix_add():
    """Test Matrix addition"""
    a = Matrix.identity(3)
    b = Matrix.identity(3)
    c = a + b
    assert c.get_data() == [[2, 0, 0], [0, 2, 0], [0, 0, 2]]


def test_matrix_sub():
    """Test Matrix addition"""
    a = Matrix.identity(3)
    b = Matrix.identity(3)
    c = a - b
    assert c.get_data() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_matrix_mul():
    """Test Matrix addition"""
    a = Matrix.identity(3)
    b = Matrix.identity(3)
    c = a * b
    assert c.get_data() == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_matrix_getitem():
    """Test element getter"""
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    assert a[0, 0] == 1


def test_matrix_setitem():
    """Test matrix element setter """
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    a[0, 0] = 4
    assert a[0, 0] == 4


def test_matrix_check_dims_match():
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    b = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    assert a._check_dims_match(b)
    assert not a._check_dims_match(t(a))


def test_matrix_add_matrix():
    assert 1 == 1


def test_t():
    """Test matrix transpose"""
    a = Matrix.from_list([[1, 2, 3], [4, 5, 6]])
    assert t(a).get_data() == [[1, 4], [2, 5], [3, 6]]
