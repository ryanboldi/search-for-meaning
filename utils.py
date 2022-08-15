import unittest
import numpy as np

def clipNum(num, low, high):
    if num > high:
        return high
    elif num < low:
        return low
    else:
        return num

def sigmoid(x):
   return 1/(1+np.exp(-x))
    
def getColor(l):
    v = clipNum(255*l, 0, 255)
    return (v, v, v)
    
# UNIT TESTING
class UtilsTest(unittest.TestCase):
    def testClipNum(self):
        self.assertEqual(0, clipNum(-1, 0, 10)) #low
        self.assertEqual(10, clipNum(11, 0, 10)) #high
        self.assertEqual(5, clipNum(5, 0, 10)) #in
    
    def testGetColor(self):
        self.assertEqual(getColor(0), 0)
        self.assertEqual(getColor(-1), 0)
        self.assertEqual(getColor(0.1), (0.1*255))
        self.assertEqual(getColor(1), 255)


# modified from https://numbersmithy.com/2d-and-3d-convolutions-using-numpy/
def conv3D2(var, kernel, pad=0):
    '''3D convolution by sub-matrix summing.
    Args:
        var (ndarray): 2d or 3d array to convolve along the first 2 dimensions.
        kernel (ndarray): 2d or 3d kernel to convolve. If <var> is 3d and <kernel>
            is 2d, create a dummy dimension to be the 3rd dimension in kernel.
    Keyword Args:
        stride (int): stride along the 1st 2 dimensions. Default to 1.
        pad (int): number of columns/rows to pad at edges.
    Returns:
        result (ndarray): convolution result.
    '''
    ny, nx = var.shape[:2]
    ky, kx = kernel.shape[:2]
    result = 0
    if pad > 0:
        var_pad = np.pad(var, ((1,1), (1, 1), (0, 0)), mode="wrap")
    else:
        var_pad = var
    for ii in range(ky*kx):
        yi, xi = divmod(ii, kx)
        slabii = var_pad[yi:2*pad+ny-ky+yi+1:1,
                         xi:2*pad+nx-kx+xi+1:1, ...]*kernel[yi, xi]
        result += slabii
    return result/9