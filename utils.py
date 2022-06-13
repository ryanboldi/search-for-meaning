import unittest

def clipNum(num, low, high):
    if num > high:
        return high
    elif num < low:
        return low
    else:
        return num
    
def getColor(l):
    return tuple(map(lambda x: clipNum(int(x), 0, 255), l))
    
# UNIT TESTING
class UtilsTest(unittest.TestCase):
    def testClipNum(self):
        self.assertEqual(0, clipNum(-1, 0, 10)) #low
        self.assertEqual(10, clipNum(11, 0, 10)) #high
        self.assertEqual(5, clipNum(5, 0, 10)) #in
    
    def testGetColor(self):
        self.assertTupleEqual(getColor([0, 0, 0]), (0, 0, 0))
        self.assertTupleEqual(getColor([-1, -1, -1]), (0, 0, 0))
        self.assertTupleEqual(getColor([0.1, 0.1, 0.1]), (0, 0, 0))
        self.assertTupleEqual(getColor([300, 300, 300]), (255, 255, 255))


unittest.main()