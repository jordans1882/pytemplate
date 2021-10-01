"""
matrix
======

The matrix module. Contains the matrix class.

Implements:
  - Printing
  - Addition
  - Subtraction
  - Multiplication
"""
from __future__ import annotations


# TODO: rewrite docs with numpy style

class Matrix():
    """Matrix Class """
    def __init__(self, data: list):
        self._data = data
        self._m = len(data)
        self._n = len(data[0])

    @classmethod
    def from_list(cls, lst: list):
        """Constructor from list"""
        data = lst
        return cls(data)

    @classmethod
    def from_matrix(cls, matrix: Matrix):
        """Constructor from matrix"""
        data = matrix.get_data()
        return cls(data)

    @classmethod
    def filled(cls, dims: tuple, value: float):
        """Constructor from dims and float"""
        data = [[value for x in range(dims[1])] for y in range(dims[0])]
        return cls(data)

    @classmethod
    def zeros(cls, dims: tuple):
        """Constructor from matrix"""
        data = [[0 for n in range(dims[1])] for m in range(dims[0])]
        return cls(data)

    @classmethod
    def ones(cls, dims: tuple):
        """Constructor from matrix"""
        data = [[1 for n in range(dims[1])] for m in range(dims[0])]
        return cls(data)

    @classmethod
    def identity(cls, dim: tuple):
        """Constructor from matrix"""
        data = []
        for i in range(dim):
            tmp = []
            for j in range(dim):
                if (i == j):
                    tmp += [1]
                else:
                    tmp += [0]
            data += [tmp]
        return cls(data)

    def __getitem__(self, idx: tuple):
        return self._data[idx[0]][idx[1]]

    def __setitem__(self, idx: tuple, value: float):
        self._data[idx[0]][idx[1]] = value

    def __add__(self, b: Matrix):
        return self._add_matrix(b)

    # TODO: truncate for large matrices
    def __repr__(self):
        """Print Matrix object"""
        return str(self._data).replace("],", "]\n")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self._multiply_matrix(other)
        if isinstance(other, Vector):
            return self._multiply_vector(other)

    def __sub__(self, b: Matrix):
        return self._subtract_matrix(b)

    def _check_dims_match(self, other):
        return self.get_dims() == other.get_dims()

    def _add_matrix(self, b: Matrix):
        if not self._check_dims_match(b):
            raise ValueError("Error: Matrix dimensions do not match for matrix addition\n"
                             f"First matrix has dims {self.get_dims()} and second has {b.get_dims()}")
        c = Matrix.zeros((self._m, self._n))
        for i in range(self._m):
            for j in range(self._n):
                c[i, j] = self.__getitem__((i, j)) + b[i, j]
        return c

    def _subtract_matrix(self, b: Matrix):
        if not self._check_dims_match(b):
            raise ValueError("Error: Matrix dimensions do not match for matrix addition\n "
                             f"First matrix has dims {self.get_dims()} and second has {b.get_dims()}")
        c = Matrix.zeros((self._m, self._n))
        for i in range(self._m):
            for j in range(self._n):
                c[i, j] = self.__getitem__((i, j)) - b[i, j]
        return c

    def get_data(self):
        """Get matrix dimensions as a dictionary"""
        return self._data

    def get_dims(self):
        """Get matrix dimensions as a dictionary"""
        return (self._m, self._n)

    def get_row(self, row_idx):
        """Get matrix dimensions as a dictionary"""
        return self._data[row_idx]

    def get_column(self, col_idx):
        """Get matrix dimensions as a dictionary"""
        return [row[col_idx] for row in self._data]

    # TODO: change set_dims to a resize() method
    # def set_dims(self, dims: tuple):
    #     """Set matrix dimensions as a dictionary"""
    #     self._m = dims[0]
    #     self._n = dims[1]

    def _multiply_matrix(self, bmat: Matrix):
        self._mult_dim_check(bmat)
        outdims = (self._m, bmat.get_dims()[1])
        result = Matrix.zeros(outdims)
        for i in range(self._m):
            for j in range(bmat.get_dims()[1]):
                for k in range(bmat.get_dims()[0]):
                    result[i, j] += self.__getitem__((i, k)) * bmat.__getitem__((k, j))
        return result

    def _multiply_vector(self, bvec: Vector):
        return 87

    # TODO: implement matrix multiplication dim checker
    def _mult_dim_check(self, bmat: Matrix):
        pass

    def transpose(self):
        """Transpose self"""
        return self.from_list(list(map(list, zip(*self._data))))


def t(a: Matrix):
    """transpose a matrix"""
    return a.transpose()


def inv(a: Matrix):
    """Return the matrix inverse"""
    return a.inverse()

# a = Matrix.from_list([[1,2,3],[4,5,6]])
# a - t(a)


class Vector():
    """Documentation for Vector"""
    def __init__(self):
        super(Vector, self).__init__()
