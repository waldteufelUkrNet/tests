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

  if len(currentWord) != 0:
    wordsArr.append(currentWord)

  resultObj = {}
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
      resultObj[word] = count

  max_count = 0
  for key in resultObj:
    if resultObj[key] > max_count:
      max_count = resultObj[key]

  for key in resultObj:
    if resultObj[key] == max_count:
      resultArr.append(key)

  resultArr.sort()
  return resultArr

print '===== start ====='
print "right result: ['hello']"
print 'my result   : ' + str( find_most_frequent('Hello,Hello, my dear!') )
print '-----------------'
print "right result: ['recursion', 'to', 'understand']"
print 'my result   : ' + str( find_most_frequent('to understand recursion you need first to understand recursion...') )
print '-----------------'
print "right result: ['mom']"
print 'my result   : ' + str( find_most_frequent('Mom! Mom! Are you sleeping?!!!') )
print '-----------------'
print "right result: ['mike']"
print 'my result   : ' + str( find_most_frequent('Mike-Paul mike lol') )
print '-----------------'
print "right result: ['hello']"
print 'my result   : ' + str( find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello") )
print '-----------------'
print "right result: ['i']"
print 'my result   : ' + str( find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind") )
print '-----------------'
print "right result: ['pages', 'the']"
print 'my result   : ' + str( find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.') )
print '=====  end  ====='