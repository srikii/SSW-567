'''Buggy triangles assignment to classify triangles given the length of the 3 sides and write automated test cases
    to test the correctness
    author: srikanth'''

import unittest      #importing unittest module

def  classify_triangle(a, b, c):

   if (a>=b+c) or (b>=c+a) or (c>=a+b): 
      return("that is not a triangle!")

   elif (a==b==c): 
      return("It's Equilateral" )

   elif (a==b) or (a==c) or (b==c): 
      return("It's Isosceles")   

   elif (a**2==b**2+c**2) or (b**2==c**2+a**2) or (c**2==b**2+a**2):
      return("It's Right angled")

   elif (a!=b!=c):
      return("It's a scalene")


class Triangle_tests(unittest.TestCase):

      def test_not_triangle(self):
         self.assertEqual(classify_triangle(5,5,25),"that is not a triangle!")
         self.assertEqual(classify_triangle(3,4,23),"that is not a triangle!")
         self.assertNotEqual(classify_triangle(5,5,5),"that is not a triangle!")
      
      def test_equilateral_traingle(self):
         self.assertEqual(classify_triangle(5,5,5),"It's Equilateral")
         self.assertEqual(classify_triangle(6,6,6),"It's Equilateral")
         self.assertNotEqual(classify_triangle(4,5,5),"It's Equilateral")

      def test_isosceles_triangle(self):
         self.assertEqual(classify_triangle(5,6,5),"It's Isosceles")
         self.assertEqual(classify_triangle(2,3,3),"It's Isosceles")
         self.assertNotEqual(classify_triangle(5,5,25),"It's Isosceles")
      
      def test_right_triangle(self):
         self.assertEqual(classify_triangle(3,4,5),"It's Right angled")
         self.assertEqual(classify_triangle(9,40,41),"It's Right angled")
         self.assertNotEqual(classify_triangle(4,4,5),"It's Right angled")

      def test_scalene_triangle(self):
         self.assertEqual(classify_triangle(6,4,5),"It's a scalene")
         self.assertEqual(classify_triangle(10,12,11),"It's a scalene")
         self.assertNotEqual(classify_triangle(3,4,10),"It's a scalene")

def main():

   a = int(input("Please Enter Side  A "))
   b = int(input("Please Enter Side  B ")) 
   c = int(input("Please Enter Side  C "))
   res= classify_triangle(a,b,c)
   print(res)


if __name__ == '__main__':
   unittest.main(exit=False, verbosity=2)
   main()
