import operator
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
  	return render(request, 'about.html')

def count_view(request):
	fulltext = request.GET['fulltext']
	count, word_freq = count_words(fulltext)
	sortedWordFreq = sorted(word_freq.items(), key= operator.itemgetter(1), reverse=True) # itemgetter returns the count of the word since items returns a list of tuples
	context = {'fulltext': fulltext, 'count': count,'word_dist':sortedWordFreq}
	return render(request, 'count.html', context)

def count_words(fulltext):
	text_list = fulltext.split()
	word_freq = {}
	for x in text_list:
		if x in word_freq:
			word_freq[x] += 1 
		else:
			word_freq[x] = 1 		
	count = len(text_list)
	return (count, word_freq)