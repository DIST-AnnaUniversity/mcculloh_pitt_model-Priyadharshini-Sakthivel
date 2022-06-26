{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor(8, shape=(), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "#Simple operation to illustrate constant and variable\n",
    "import tensorflow as tf\n",
    "x = tf.constant(2)\n",
    "y = tf.Variable(x+4)\n",
    "#type(x)\n",
    "#print(x)\n",
    "total=x+y\n",
    "#type(total)\n",
    "print(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 5 7]\n",
      "Dimension  1\n",
      "Shape  (3,)\n",
      "[[2 5 7]\n",
      " [3 6 8]]\n",
      "Dimension  2\n",
      "Shape  (2, 3)\n",
      "[[[ 1  3  5  6]\n",
      "  [ 2  4  6  7]\n",
      "  [ 1  2  3  4]]\n",
      "\n",
      " [[ 4  3  2  1]\n",
      "  [ 7  9 11 12]\n",
      "  [ 8 10 12  9]]]\n",
      "Dimension  3\n",
      "Shape  (2, 3, 4)\n"
     ]
    }
   ],
   "source": [
    "#tensor demo\n",
    "#1D\n",
    "import numpy as np\n",
    "x = np.array([2,5,7])\n",
    "print(x)\n",
    "print(\"Dimension \", x.ndim)\n",
    "print(\"Shape \", x.shape)\n",
    "\n",
    "y = np.array([[2,5,7],[3,6,8]])\n",
    "print(y)\n",
    "print(\"Dimension \", y.ndim)\n",
    "print(\"Shape \", y.shape)\n",
    "\n",
    "z = np.array([[[1,3,5,6],[2,4,6,7],[1,2,3,4]],[[4,3,2,1],[7,9,11,12],[8,10,12,9]]])\n",
    "print(z)\n",
    "print(\"Dimension \", z.ndim)\n",
    "print(\"Shape \", z.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[4 6]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "tensor_a = tf.constant([[1,2]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[3, 4]], dtype = tf.int32)\n",
    "tensor_add = tf.add(tensor_a, tensor_b)\n",
    "print(tensor_add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[ 6 23]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "tensor_a = tf.constant([[9,27]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[3, 4]], dtype = tf.int32)\n",
    "tensor_subtract = tf.subtract(tensor_a, tensor_b)\n",
    "print(tensor_subtract)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[48 35]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "tensor_a = tf.constant([[8,7]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[6, 5]], dtype = tf.int32)\n",
    "tensor_multiply = tf.multiply(tensor_a, tensor_b)\n",
    "print(tensor_multiply)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
