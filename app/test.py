def file_search(folder, filename): # list, str
  result = ''
  foldername = folder[0]
  result = result + foldername + '/'

  
  print result
  print foldername

  for item in folder[1:]:
    # print 'item: ' + str(item)
    if isinstance(item, list):
      # sublist iteration
      a = 1
    else:
      if item == filename:
        result = result + filename
        return result

  return False


print '===== start ====='
print 'right result: C:/ideas.txt'
print 'my result   : ' + str(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
print '-----------------'
print 'right result: False'
print 'my result   : ' + str(file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me'))
print '-----------------'
print 'right result: /home/user2/desktop/new folder/hereiam.py'
print 'my result   : ' + str(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))
print '=====  end  ====='