## Your name: Ethan McCall
## The option you've chosen: Option 2

# Put import statements you expect to need here!
import unittest
import itertools
import collections
import tweepy
import twitter_info # same deal as always...
import json
import sqlite3
import omdb



# Write your test cases here.
class Test1(unittest.TestCase):
	def test_request_movie(self): 
		d={}
		self.assertEqual(type(request_movie("The Hangover"),type(d)))
class Test2(unittest.TestCase):
	def test_characterize_rating(self):
		h=Movie()
		self.assertEqual(h.characterize_rating(3.0),"poor")
class Test3(unittest.TestCase):
	def test_omdb_rating(self): 
		h=Movie()
		self.assertEqual(movie.omdb_rating(),type(6.5),"Testing that rating is an integer")
class Test4(unittest.TestCase):
	def test_is_actors_in_movie(self): 
		h=Movie()
		self.assertIsIn(type("Bradley Cooper"),type(h.get_director()))
class Test5(unittest.TestCase):
	def test_get_actor_twitter(self):
		d={}
		self.assertEqual(type(get_actor_twitter("Ben Stiller")), type(r))
class Test6(unittest.TestCase):
	def test_user_info(self):
		r=user_info("umich")
		d={}
		f={}
		m=[d,f]
		self.assertEqual(type(m),type(r))
	def test_user_info(self):
		r=user_info("umich")
		d={}
		f={}
		m=[d,f]
		self.assertEqual(type(d),type(r[0]))
class Test7(unittest.TestCase):
	def test_movie_list(self):
		pp=[]
		self.assertEqual(type(pp),type(movie_list()))

class Test8(unittest.TestCase):
	def test_three_movie_class1(self): 
		d={}
		f={}
		m=[d,f]
		self.assertequal(type(m),type(three_movie_class))
	def test_three_movie_class2(self): 
		d={}
		f={}
		m=[d,f]
		self.assertequal(type(f),type(three_movie_class[0]))



if __name__ == "__main__":
	unittest.main(verbosity=2)


## Remember to invoke all your tests...