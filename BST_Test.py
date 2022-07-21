import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    
    def setUp(self):
        self.__a = Binary_Search_Tree()
        
    def test_empty_tree(self):
        self.assertEqual('[ ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ ]', str(post))
        self.assertEqual(0, self.__a.get_height())
        self.assertEqual([], self.__a.to_list())
    
    def test_insert_one_node(self):
        self.__a.insert_element(20)
        self.assertEqual('[ 20 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 20 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 20 ]', str(post))
        self.assertEqual(1, self.__a.get_height())
        self.assertEqual([20], self.__a.to_list())
        
    def test_insert_three_nodes_left_left(self):
        self.__a.insert_element(5)
        self.__a.insert_element(3)
        self.__a.insert_element(1)
        self.assertEqual('[ 1, 3, 5 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 3, 1, 5 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 1, 5, 3 ]', str(post))
        self.assertEqual(2, self.__a.get_height())
        self.assertEqual([1,3,5], self.__a.to_list())
        
    def test_insert_four_nodes_left_left(self):
        self.__a.insert_element(5)
        self.__a.insert_element(3)
        self.__a.insert_element(1)
        self.__a.insert_element(4)
        self.assertEqual('[ 1, 3, 4, 5 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 3, 1, 5, 4 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 1, 4, 5, 3 ]', str(post))
        self.assertEqual(3, self.__a.get_height())
        self.assertEqual([1,3,4,5], self.__a.to_list())
        
    def test_insert_three_nodes_left_right(self):
        self.__a.insert_element(5)
        self.__a.insert_element(3)
        self.__a.insert_element(4)
        self.assertEqual('[ 3, 4, 5 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 4, 3, 5 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 3, 5, 4 ]', str(post))
        self.assertEqual(2, self.__a.get_height())
        self.assertEqual([3,4,5], self.__a.to_list())
        
    def test_insert_three_nodes_right_right(self):
        self.__a.insert_element(5)
        self.__a.insert_element(7)
        self.__a.insert_element(9)
        self.assertEqual('[ 5, 7, 9 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 7, 5, 9 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 5, 9, 7 ]', str(post))
        self.assertEqual(2, self.__a.get_height())
        self.assertEqual([5,7,9], self.__a.to_list())
        
    def test_insert_four_nodes_right_right(self):
        self.__a.insert_element(5)
        self.__a.insert_element(7)
        self.__a.insert_element(9)
        self.__a.insert_element(6)
        self.assertEqual('[ 5, 6, 7, 9 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 7, 5, 6, 9 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 6, 5, 9, 7 ]', str(post))
        self.assertEqual(3, self.__a.get_height())
        self.assertEqual([5,6,7,9], self.__a.to_list())
        
    def test_insert_three_nodes_right_left(self):
        self.__a.insert_element(5)
        self.__a.insert_element(7)
        self.__a.insert_element(6)
        self.assertEqual('[ 5, 6, 7 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 6, 5, 7 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 5, 7, 6 ]', str(post))
        self.assertEqual(2, self.__a.get_height())
        self.assertEqual([5,6,7], self.__a.to_list())
        
    def test_insert_with_floater(self):
        self.__a.insert_element(3)
        self.__a.insert_element(0)
        self.__a.insert_element(5)
        self.__a.insert_element(-1)
        self.__a.insert_element(1)
        self.__a.insert_element(-2)
        self.assertEqual('[ -2, -1, 0, 1, 3, 5 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 0, -1, -2, 3, 1, 5 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ -2, -1, 1, 5, 3, 0 ]', str(post))
        self.assertEqual(3, self.__a.get_height())
        self.assertEqual([-2,-1,0,1,3,5], self.__a.to_list())
        
    def test_insert_ten_nodes(self):
        self.__a.insert_element(14)
        self.__a.insert_element(6)
        self.__a.insert_element(8)
        self.__a.insert_element(22)
        self.__a.insert_element(17)
        self.__a.insert_element(15)
        self.__a.insert_element(16)
        self.__a.insert_element(20)
        self.__a.insert_element(18)
        self.__a.insert_element(19)
        self.assertEqual('[ 6, 8, 14, 15, 16, 17, 18, 19, 20, 22 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 17, 14, 8, 6, 15, 16, 20, 18, 19, 22 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 6, 8, 16, 15, 14, 19, 18, 22, 20, 17 ]', str(post))
        self.assertEqual(4, self.__a.get_height())
        self.assertEqual([6,8,14,15,16,17,18,19,20,22], self.__a.to_list())
        
    def test_insert_20_nodes_remove_1(self):
        self.__a.insert_element(85)
        self.__a.insert_element(31)
        self.__a.insert_element(126)
        self.__a.insert_element(22)
        self.__a.insert_element(46)
        self.__a.insert_element(92)
        self.__a.insert_element(286)
        self.__a.insert_element(28)
        self.__a.insert_element(35)
        self.__a.insert_element(50)
        self.__a.insert_element(87)
        self.__a.insert_element(107)
        self.__a.insert_element(212)
        self.__a.insert_element(307)
        self.__a.insert_element(51)
        self.__a.insert_element(89)
        self.__a.insert_element(98)
        self.__a.insert_element(112)
        self.__a.insert_element(309)
        self.__a.insert_element(115)
        self.__a.remove_element(31)
        self.assertEqual('[ 22, 28, 35, 46, 50, 51, 85, 87, 89, 92, 98, 107, 112, 115, 126, 212, 286, 307, 309 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 92, 85, 35, 22, 28, 50, 46, 51, 87, 89, 126, 107, 98, 112, 115, 286, 212, 307, 309 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 28, 22, 46, 51, 50, 35, 89, 87, 85, 98, 115, 112, 107, 212, 309, 307, 286, 126, 92 ]', str(post))
        self.assertEqual(5, self.__a.get_height())
        self.assertEqual([22, 28, 35, 46, 50, 51, 85, 87, 89, 92, 98, 107, 112, 115, 126, 212, 286, 307, 309], self.__a.to_list())
        
    def test_insert_15_nodes_remove_4(self):
        self.__a.insert_element(38)
        self.__a.insert_element(17)
        self.__a.insert_element(93)
        self.__a.insert_element(8)
        self.__a.insert_element(27)
        self.__a.insert_element(73)
        self.__a.insert_element(139)
        self.__a.insert_element(3)
        self.__a.insert_element(12)
        self.__a.insert_element(21)
        self.__a.insert_element(85)
        self.__a.insert_element(112)
        self.__a.insert_element(140)
        self.__a.insert_element(15)
        self.__a.insert_element(124)
        self.__a.remove_element(38)
        self.__a.remove_element(8)
        self.__a.remove_element(17)
        self.__a.remove_element(21)
        self.assertEqual('[ 3, 12, 15, 27, 73, 85, 93, 112, 124, 139, 140 ]', str(self.__a))
        pre = self.__a.pre_order()
        self.assertEqual('[ 73, 12, 3, 27, 15, 112, 93, 85, 139, 124, 140 ]', str(pre))
        post = self.__a.post_order()
        self.assertEqual('[ 3, 15, 27, 12, 85, 93, 124, 140, 139, 112, 73 ]', str(post))
        self.assertEqual(4, self.__a.get_height())
        self.assertEqual([3, 12, 15, 27, 73, 85, 93, 112, 124, 139, 140], self.__a.to_list())
        
    def test_insert_duplicate_value(self):
        with self.assertRaises(ValueError):
            self.__a.insert_element(20)
            self.__a.insert_element(10)
            self.__a.insert_element(30)    
            self.__a.insert_element(5)
            self.__a.insert_element(11)
            self.__a.insert_element(12)
            self.__a.insert_element(25)
            self.__a.insert_element(10)
            
    def test_remove_on_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__a.remove_element(20)   
            
    def test_remove_value_not_in_tree(self):
        with self.assertRaises(ValueError):
            self.__a.insert_element(20)
            self.__a.insert_element(10)
            self.__a.insert_element(30)    
            self.__a.insert_element(5)
            self.__a.insert_element(11)
            self.__a.insert_element(12)
            self.__a.insert_element(25)
            self.__a.remove_element(300)
            
        
if __name__ == '__main__':
  unittest.main()
        
    