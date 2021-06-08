morse_code = {
  "A" : ".-",
  "B" : "-...",
  "C" : "-.-.",
  "D" : "-..",
  "E" : ".",
  "F" : "..-.",
  "G" : "--.",
  "H" : "....",
  "I" : "..",
  "J" : ".---",
  "K" : "-.-",
  "L" : ".-..",
  "M" : "--",
  "N" : "-.",
  "O" : "---",
  "P" : ".--.",
  "Q" : "--.-",
  "R" : ".-.",
  "S" : "...",
  "T" : "-",
  "U" : "..-",
  "V" : "...-",
  "W" : ".--",
  "X" : "-..-",
  "Y" : "-.--",
  "Z" : "--.."
}

def encode_morze(text): # string
  # return string
  # . = ^
  # - = ^^^
  # after point or dash 1 _
  # after letter 3 _
  # after world 7 _
  # after message 0 _
  # only english letter lowercase/uppercase

  def encode_word(word):
    result_word = morse_code[ word[0] ]


    return result_word


  string = text.upper()
  wordsArr = string.split(' ')
  print("wordsArr", len(wordsArr) )

  result = encode_word( wordsArr[0] )

  return result

print '===== start ====='
print 'right result: ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^0'
print 'my result   : ' + str(encode_morze('Morze code'))
print '-----------------'
print 'right result: ^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^'
print 'my result   : ' + str(encode_morze('Prometheus'))
print '-----------------'
print 'right result: ^_^_^___^^^_^^^_^^^___^_^_^'
print 'my result   : ' + str(encode_morze('SOS'))
print '-----------------'
print 'right result: '
print 'my result   : ' + str(encode_morze('1'))
print '-----------------'
print 'right result: '
print 'my result   : ' + str(encode_morze(''))
print '=====  end  ====='