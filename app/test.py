def encode_morze(text): # string
  # return string
  # . = ^
  # - = ^^^
  # after point or dash 1 _
  # after letter 3 _
  # after world 7 _
  # after message 0 _
  # only english letter lowercase/uppercase
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
  morse_code_processed = {}
  for key in morse_code:
    encoded_letter = ''
    if morse_code[key][0] == '.':
      encoded_letter = encoded_letter + '^'
    else:
      encoded_letter = encoded_letter + '^^^'

    for symbol in morse_code[key][1:]:
      if symbol == '.':
        encoded_letter = encoded_letter + '_' + '^'
      else:
        encoded_letter = encoded_letter + '_' + '^^^'

    morse_code_processed[key] = encoded_letter

  def encode_word(word):

    # filter no-letter
    filtered_word = ''
    for letter in word:
      if letter >= 'A' and letter <= 'Z':
        filtered_word = filtered_word + letter

    if len(filtered_word) == 0:
      return ''

    # letter-word into dot-dash-word
    result_word = morse_code_processed[ filtered_word[0] ]

    for letter in filtered_word[1:]:
      result_word = result_word + '___' + morse_code_processed[letter]

    return result_word


  string = text.upper()
  wordsArr = string.split(' ')

  result = encode_word( wordsArr[0] )
  for word in wordsArr[1:]:
    result = result + '_______' + encode_word( word )

  return result

print '===== start ====='
print 'right result: ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^'
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