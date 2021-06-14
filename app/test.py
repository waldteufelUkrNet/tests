def convert_n_to_m(x, n, m): # x - int/srt (upper/lower), n, m - int: 1 <= n, m <= 36
  # return str: number x in system m
  # return False: x != int/str or !!!
  # osnova > 10: A-Z upper
  # 1-system: zero-amount literation

  alphaDigits = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'I':17,'J':18,'K':19,'L':20,'M':21,'N':22,'O':23,'P':24,'Q':25,'R':26,'S':27,'T':28,'U':29,'V':30,'W':31,'X':32,'Y':33,'Z':34}
  digitsAlpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U',30:'V',31:'W',32:'X',33:'Y',34:'Z'}

  # x validation
  if isinstance(x, int) or isinstance(x, long):
    x = str(x)

  if not isinstance(x, str):
    return False

  numberAsArray = []
  number = 0L
  for letter in x:
    if (letter >= 'A' and letter <= 'Z') or (letter >= 'a' and letter <= 'z'):
      letter = alphaDigits[letter.upper()]
    if int(letter) >= n:
      return False
    numberAsArray.append( int(letter) )
  numberAsArray.reverse()

  iterator = 0
  for item in numberAsArray:
    number = number + numberAsArray[iterator]*(n**iterator)
    iterator = iterator + 1

  # 1. n-number -> 10-number
  # try:
  #   number = int(x, base=n)
  # except:
  #   return False

  # 1.a
  if m == 1:
    return '0'*number

  # 2. 10-number -> m-number
  string = ''
  if number == 0:
    return '0'
  digits = []
  while number:
      digits.append(int(number % m))
      number //= m

  for num in digits[::-1]:
    if num > 9:
      num = digitsAlpha[num]
    string = string + str(num)
  return string

print '===== start ====='
print "right result: False"
print 'my result   : ' + str( convert_n_to_m([123], 4, 3) )
print '-----------------'
print "right result: 102"
print 'my result   : ' + str( convert_n_to_m("0123", 5, 6) )
print '-----------------'
print "right result: False"
print 'my result   : ' + str( convert_n_to_m("123", 3, 5) )
print '-----------------'
print "right result: 000000000000000000000000000"
print 'my result   : ' + str( convert_n_to_m(123, 4, 1) )
print '-----------------'
print "right result: False"
print 'my result   : ' + str( convert_n_to_m(-123.0, 11, 16) )
print '-----------------'
print "right result: 32E7"
print 'my result   : ' + str( convert_n_to_m("A1Z", 36, 16) )
print '-----------------'
print "right result: 0"
print 'my result   : ' + str( convert_n_to_m(0, 10, 2) )
print '-----------------'
print "right result: 0"
print 'my result   : ' + str( convert_n_to_m(000, 10, 2) )
print '-----------------'
print "right result: 0"
print 'my result   : ' + str( convert_n_to_m('000', 10, 2) )
print '-----------------'
print "right result: 1100001001"
print 'my result   : ' + str( convert_n_to_m(777L, 10, 2) )
print '-----------------'
print "right result: 2C09BC518E8048D23A"
print 'my result   : ' + str( convert_n_to_m(123123123123123123123, 11, 16) )
print '-----------------'
print "right result: 123123123123123123123"
print 'my result   : ' + str( convert_n_to_m(123123123123123123123, 10, 10) )
print '-----------------'
print "right result: HGPEYJ"
print 'my result   : ' + str( convert_n_to_m('qweasd', 33, 36) )
print '=====  end  ====='