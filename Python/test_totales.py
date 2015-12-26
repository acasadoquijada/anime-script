import unittest

from scriptAnime import *


class TestStringMethods(unittest.TestCase):
	
	def test_formato_anime(self):
		anime = "Sword ArT onLiNe"
		
		anime_limpio = formato_anime(anime)		
		
		self.assertEqual("sword-art-online", anime_limpio)
		
		print("Test formato anime correcto")

if __name__ == '__main__':
	unittest.main()	

