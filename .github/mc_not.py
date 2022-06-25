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
      "[0 1] value 0\n",
      "[1 1] value 0\n"
     ]
    }
   ],
   "source": [
    "#McCulloh Pitt model for AND model\n",
    "import numpy as np\n",
    "\n",
    "def McNot(x,w,t):\n",
    "    net = np.dot(x,w)\n",
    "    if net>t:\n",
    "        output = 1\n",
    "    else:\n",
    "        output = 0\n",
    "    return output\n",
    "\n",
    "x0 = np.array([0,1])\n",
    "x1 = np.array([1,1])\n",
    "w = np.array([1,-1])\n",
    "\n",
    "t = 0\n",
    "ans1 = McNot(x0,w,t)\n",
    "print (x0, \"value\", ans1)\n",
    "ans2 = McNot(x1,w,t)\n",
    "print (x1, \"value\", ans2)"
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
