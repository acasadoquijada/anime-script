import unittest

from scriptAnime import *


class Test(unittest.TestCase):
	
	def test_formato_anime(self):
		anime = "Sword ArT onLiNe"
		
		anime_limpio = formato_anime(anime)		
		
		self.assertEqual("sword-art-online", anime_limpio)
		
		print("Test formato anime correcto")


	def test_registro(self):
		anime = "bleach"
		capitulo = 44
		
		registro(anime,capitulo)
		
		historial(anime)
		
		con = lite.connect('registro.db')

		with con:

			cur = con.cursor()
			info = cur.execute("SELECT capitulo FROM bleach")
			
			self.assertEqual(cur.fetchone()[0], capitulo)

		print("Test registro/historial correcto")


if __name__ == '__main__':
	unittest.main()	

