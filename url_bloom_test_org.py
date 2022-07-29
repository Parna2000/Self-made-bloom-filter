from bloomfilter import BloomFilter
from random import shuffle
import csv

class Bloom(object):
    def __init__(self, test_url):
        n = 47282 #no of items to add
        p = 0.05 #false positive probability

        bloomf = BloomFilter(n,p)
        print("Size of bit array:{}".format(bloomf.size))
        print("False positive Probability:{}".format(bloomf.fp_prob))
        print("Number of hash functions:{}".format(bloomf.hash_count))

        # urls to be added
        malicious = []
        with open ('only_malicious.csv','r') as file:
            mal = csv.reader(file)
            for row in mal:
                malicious.append(row[0])

        # print(malicious)
        
        for item in malicious:
	        bloomf.add(item)

        shuffle(malicious)

        # test_word='https://briefingday.us8.list-manage.com/unsubscribe'

        if test_url in malicious:
            print(f'{test_url} is probably malicious!')
        else:
            print(f'{test_url} is definitely not malicious!')
            




