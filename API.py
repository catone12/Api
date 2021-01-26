import requests

bb=0
class test_api():

	def __init__(self,requests):
		self.requests=requests
		# self.url='https://cat-fact.herokuapp.com'
		#
		# self.metod_get_horse='/facts?animal_type=horse'
		# self.metod_get_cat='/facts?animal_type=cat'
		# self.metod_get_dog = '/facts?animal_type=dog'
		# self.metod_get_snail = '/facts?animal_type=snail'
		# self.person='58e007480aac31001185ecef'
		self.count_facts_author=0


	def test_metod_get(self,url,metod,person):
		response=self.requests.get(f'{url}{metod}')

		for kk in range(len(response.json())):
			# print(response.json()[kk]['user'])
			if response.json()[kk]['user']==person:
				self.count_facts_author+=1

		# print(self.count_facts_author)
		return self.count_facts_author

	#
	# def test_dog(self,person):
	# 	response = self.requests.get(f'{self.url}{self.metod_get_dog}')
	#
	# 	for kk in range(len(response.json())):
	# 		print(response.json()[kk]['user'])
	# 		if response.json()[kk]['user'] == person:
	# 			self.count_facts_author += 1
	# 		print(self.count_facts_author)
	# def test_snail(self,person):
	# 	response = self.requests.get(f'{self.url}{self.metod_get_snail}')
	#
	# 	for kk in range(len(response.json())):
	# 		print(response.json()[kk]['user'])
	# 		if response.json()[kk]['user'] == person:
	# 			self.count_facts_author += 1
	# 		print(self.count_facts_author)
	# def test_horse(self,person):
	# 	response = self.requests.get(f'{self.url}{self.metod_get_horse}')
	#
	# 	for kk in range(len(response.json())):
	# 		print(response.json()[kk]['user'])
	# 		if response.json()[kk]['user'] == person:
	# 			self.count_facts_author += 1
	# 		print(self.count_facts_author)

	# def show_count(self):
	# 	self.test_horse()
	# 	self.test_dog()
	# 	self.test_cat()
	# 	self.test_snail()
	# 	print(self.count_facts_author)
# test_api().test_cat()
# test_api().test_dog()
# test_api().test_snail()
# test_api().test_horse()
count_facts=0
count_facts+=test_api(requests).test_metod_get('https://cat-fact.herokuapp.com','/facts?animal_type=horse','58e007480aac31001185ecef')
count_facts+=test_api(requests).test_metod_get('https://cat-fact.herokuapp.com','/facts?animal_type=horse','58e007480aac31001185ecef')
count_facts+=test_api(requests).test_metod_get('https://cat-fact.herokuapp.com','/facts?animal_type=horse','58e007480aac31001185ecef')
count_facts+=test_api(requests).test_metod_get('https://cat-fact.herokuapp.com','/facts?animal_type=horse','58e007480aac31001185ecef')
print(count_facts)
