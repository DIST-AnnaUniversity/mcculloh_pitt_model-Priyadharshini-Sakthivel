
    "#McCulloh Pitt model for AND model\n",
    "import numpy as np\n",
    "\n",
    "def McOr(x,w,t):\n",
    "    net = np.dot(x,w)\n",
    "    if net>t:\n",
    "        output = 1\n",
    "    else:\n",
    "        output = 0\n",
    "    return output\n",
    "\n",
    "x0 = np.array([0,0,1])\n",
    "x1 = np.array([0,1,1])\n",
    "x2 = np.array([1,0,1])\n",
    "x3 = np.array([1,1,1])\n",
    "w = np.array([5,5,-4])\n",
    "\n",
    "t = 0\n",
    "ans1 = McOr(x0,w,t)\n",
    "print (x0, \"value\", ans1)\n",
    "ans2 = McOr(x1,w,t)\n",
    "print (x1, \"value\", ans2)\n",
    "ans3 = McOr(x2,w,t)\n",
    "print (x2, \"value\", ans3)\n",
    "ans4 = McOr(x3,w,t)\n",
    "print (x3, \"value\", ans4)"
 
