class SuperStr(str):

  def __init__(self,str):
    # self.name = name
    pass

  def is_repeatance(self,s):
    if not isinstance(s, str):
      return False

    if len(s) == 0:
      return False

    if s == None:
      return False

    if not (len(self) % len(s) == 0):
      return False

    arr = []
    substr = ''
    counter = 0
    for letter in self:
      substr = str(substr) + str(letter)
      counter = counter + 1
      if counter == len(s):
        arr.append(substr)
        counter = 0
        substr = ''

    for item in arr:
      if not item == s:
        return False

    return True

  def is_palindrom(self):
    if len(self) == 0:
      return True

    arr1 = []
    arr2 = []

    for symbol in self:
      arr1.append(symbol.lower())
      arr2.append(symbol.lower())

    arr2.reverse()

    for i in range(0, len(arr1) - 1 ):
      if arr1[i] != arr2[i]:
        return False

    return True

s2 = SuperStr('a')

print s2.is_repeatance('a')

s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 (str)
print int(s) # 123123123123 (int)
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True