{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 11   1   7]\n",
      " [  8   0   2]\n",
      " [  3   2 -11]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "A = np.array([[2, 4,2], [5, -6,-4], [-2,5,-7]])\n",
    "B = np.array([[9, -3,5], [3, 6,6], [5,-3,-4]])\n",
    "C = A + B      # element wise addition\n",
    "print(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ -7   7  -3]\n",
      " [  2 -12 -10]\n",
      " [ -7   8  -3]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "A = np.array([[2, 4,2], [5, -6,-4], [-2,5,-7]])\n",
    "B = np.array([[9, -3,5], [3, 6,6], [5,-3,-4]])\n",
    "C = A - B      # element wise addition\n",
    "print(C)"
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
      "[[ 18 -12  10]\n",
      " [ 15 -36 -24]\n",
      " [-10 -15  28]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "A = np.array([[2, 4,2], [5, -6,-4], [-2,5,-7]])\n",
    "B = np.array([[9, -3,5], [3, 6,6], [5,-3,-4]])\n",
    "C = A *B      # element wise addition\n",
    "print(C)"
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
