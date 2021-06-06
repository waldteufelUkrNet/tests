def file_search(folder, fileName): # list, str
  folderName = ''
  result = ''
  adressArr  = []

  def iterateDir(arr, pos = 0):
    arrLength = len( arr )

    if arrLength == 1: # folder is empty and only has a name ( arr['some name'] )
      return False
    else:              # folder is't empty, has a name and at less 1 item ( arr['some name', item 1, item 2, ... item n] )
      folderName = arr[0]
      adressArr.append(folderName)

      subfolderResult = ''

      for item in arr[1:]:
        if isinstance(item,str): # file name
          if item == fileName:
            return formAdressString(item)
        else:                    # new subfolder
          subfolderResult = iterateDir(item)

      return subfolderResult

  def formAdressString(name):
    result = adressArr[0]
    for item in adressArr[1:]:
      result = result + '/' + item
    result = result + '/' + name
    return result

  return iterateDir(folder)

# print 'test1, simple              : ' + str(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt') )
# print 'test3, in subfolder        : ' + str(file_search(['C:', 'backup.log', ['dir', 'ideas.txt']], 'ideas.txt') )
print 'test3, empty folder before : ' + str(file_search(['C:', 'backup.log', ['dir'], 'ideas.txt'], 'ideas.txt') )

# file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
# file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')


# print '===== start ====='
# print 'right result: C:/ideas.txt'
# print 'my result   : ' + str(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
# print '-----------------'
# print 'right result: False'
# print 'my result   : ' + str(file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me'))
# print '-----------------'
# print 'right result: /home/user2/desktop/new folder/hereiam.py'
# print 'my result   : ' + str(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))
# print '=====  end  ====='