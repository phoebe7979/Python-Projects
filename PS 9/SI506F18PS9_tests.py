from SI506F18_ps9 import *
import unittest
import requests

class Problem1(unittest.TestCase):
	def test_response(self):
		self.assertIsInstance(marvel_response,requests.Response)
	def test_artist_titles(self):
		self.assertEqual(sorted(artist_titles),sorted(['Anthony Russo & Joe Russo', 'Taika Waititi', 'Ryan Coogler', 'Jon Favreau', 'Anthony Russo & Joe Russo', 'Peyton Reed', 'Joss Whedon', 'Shane Black', 'Anthony Russo & Joe Russo', 'Scott Derrickson', 'Joe Johnston', 'James Gunn', 'James Gunn', 'Jon Favreau', 'Peyton Reed', 'Alan Taylor', 'Leo Riley', 'Leo Riley', 'Joss Whedon', 'Peter David', 'Marvel: 75 Years from Pulp to Pop!', 'Mitch Schauer', 'Mitch Schauer', 'Ghostface Killah', 'Marc Webb', 'Ruben Fleischer', 'Märvel & Dregen', 'Joel Coen & Ethan Coen', 'Märvel', 'Brad Thor', 'Marvel', 'Movie Reviews,Film,Comic Books,Marvel,DC,Star Wars,Netflix,Batman,Superman,X-Men,Flash,Daredevil,The Last Jedi,Guardians of the Galaxy,Justice League,Deadpool,Wonder Woman,Black Panther,Avengers,Infinity War,Thor,Venom,Ant-Man,Captain Marvel,Castlevani', 'Märvel', 'Märvel', 'Solillaquists of Sound', 'Eric Drath', 'Märvel', 'Märvel', 'Roger Michell', 'Märvel', 'Märvel', 'Märvel', 'Märvel', 'Dan Gvozden, Mark Ginocchio: spider-man, comics, marvel, spiderman, comic books', 'Märvel', 'Märvel', 'Märvel', "Marvel's Agents of S.H.I.E.L.D.", 'NVS, Marvel & Märvel', 'Märvel']))
	def test_artist_titles(self):
		self.assertIsInstance(artist_titles,list, "Testing that artist_titles is a list")
	def test_short_descrs(self):
		self.assertEqual(sorted(short_descriptions),sorted(['After the cataclysmic events in New York with The Avengers, Marvel’s “Captain America: The Winter', 'In Marvel Studios’ Thor: Ragnarok, Thor is imprisoned on the other side of the universe without his', "After the death of his father, the king of Wakanda, young T'Challa returns home to the isolated high", 'After surviving an unexpected attack in enemy territory, jet-setting industrialist Tony Stark builds', 'Marvel’s Captain America: Civil War finds Steve Rogers leading the newly formed team of Avengers in', 'From the Marvel Cinematic Universe comes Ant-Man and the Wasp, a new chapter featuring heroes with', 'Marvel Studios presents “Avengers: Age of Ultron,” the epic follow-up to the biggest Super Hero', 'An unprecedented cinematic journey ten years in the making and spanning the entire Marvel Cinematic', 'From Marvel comes Doctor Strange, the story of world-famous neurosurgeon Dr. Stephen Strange, whose', 'After being deemed unfit for military service, Steve Rogers volunteers for a top secret research', 'From Marvel, the studio that brought you the global blockbuster franchises of Iron Man, Thor,', 'Set to the sonic backdrop of Awesome Mixtape #2, Marvel Studios’ Guardians of the Galaxy Vol. 2', 'Marvel Entertainment presents the highly anticipated sequel to the blockbuster film based on the', 'The next evolution of the Marvel Cinematic Universe brings a founding member of The Avengers to the', 'Marvel’s "Thor: The Dark World" continues the adventures of Thor, the Mighty Avenger, as he battles', 'Marvel makes cinematic history again with the most unexpected team-up in the universe! Joining', 'In Iron Man & Captain America: Heroes United, Iron Man and Captain America battle to keep the Red', 'Experience an exciting journey through the 75 year history of the Marvel Universe, from its humble', "This Hallow's eve, Nightmare is bent on conquering our waking world by crossing through the Dream", 'The holiday season gets extra chilly as Loki and the frost giant Ymir plot to conquer the world.', 'It’s great to be Spider-Man (Andrew Garfield). For Peter Parker, there’s no feeling quite like', 'Tom Hardy stars as the lethal protector and anti-hero Venom - one of Marvel’s most enigmatic and', 'As the world comes to grips with the existence of superheroes and aliens, agent Phil Coulson']))

class Problem2(unittest.TestCase):
	def test_api_key(self):
		self.assertTrue(OMDB_API_KEY != "paste your api key string here")
		self.assertTrue(OMDB_API_KEY != "")
		self.assertIsInstance(OMDB_API_KEY, str)
		self.assertTrue(OMDB_API_KEY is not None)

class Problem3(unittest.TestCase):
	def test_director(self):
		self.assertEqual(bp_director, "Ryan Coogler")
	def test_box_office(self):
		self.assertEqual(box_office_bp, "$501,105,037")

class Problem4(unittest.TestCase):
	def test_function1(self):
		self.assertTrue(get_movie_data("Outbreak"),"Testing that the function runs")
		self.assertIsInstance(get_movie_data("Outbreak"),dict, "Testing that the function returns a Python object of type dictionary")
	def test_function2(self):
		self.assertEqual(get_movie_data("Interstellar")["Director"], "Christopher Nolan", "Testing an attribute of return val data")
	def test_function3(self):
		self.assertEqual(get_movie_data("You've Got Mail")["Actors"], "Tom Hanks, Meg Ryan, Greg Kinnear, Parker Posey","Testing an attribute of return val data")
	def test_function4(self):
		self.assertEqual(get_movie_data("The Martian")["Plot"],"An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.","Testing an attribute of return val data")

if __name__ == "__main__":
	unittest.main(verbosity=2)
