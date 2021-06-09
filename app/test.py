def find_most_frequent(text): # str: a-z ,.:;!?-
  # return alphabetical list of words in lowercase > 2
  # hand-made == hand, made
  # page != pages
  # page == Page

  l_text = text.lower()
  wordsArr = []
  currentWord = ''

  # build array of all words
  for letter in l_text:
    if letter >= 'a' and letter <= 'z':
      currentWord = currentWord + letter
    else:
      if len(currentWord) > 0:
        wordsArr.append(currentWord)
      currentWord = ''

  resultArr = []
  copiedArr = []
  for word in wordsArr:
    copiedArr.append(word)

  for word in wordsArr:
    count = 0
    for word2 in copiedArr:
      if str(word) == str(word2):
        count = count + 1

    if count > 1 and not word in resultArr:
      resultArr.append(word)
  resultArr.sort()
  return resultArr

print '===== start ====='
print "right result: ['hello']"
print 'my result   : ' + str( find_most_frequent('Hello,Hello, my dear!') )
print '-----------------'
print "right result:  ['recursion', 'to', 'understand']"
print 'my result   : ' + str( find_most_frequent('to understand recursion you need first to understand recursion...') )
print '-----------------'
print "right result: ['mom']"
print 'my result   : ' + str( find_most_frequent('Mom! Mom! Are you sleeping?!!!') )
print '=====  end  ====='