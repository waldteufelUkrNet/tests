def file_search(folder, fileName): # list, str
  folderName = ''
  result = ''
  adressArr  = []
  parentFoldersArr = []

  def iterateDir(arr, pos = 1):
    arrLength = len( arr )
    parentFoldersArr.append(arr)

    if arrLength == 1: # folder is empty and only has a name ( arr['some name'] )

      return False

    else:              # folder is't empty, has a name and at less 1 item ( arr['some name', item 1, item 2, ... item n] )

      folderName = arr[0]
      adressArr.append(folderName)
      subfolder = False

      for item in arr[pos:]:
        if isinstance(item,str): # file name
          if item == fileName:
            return formAdressString(item)
        else:                    # new subfolder
          subfolder = iterateDir(item)
          if subfolder != False: # searched name is in subfolder
            return subfolder

      # subfolder iterarion is end. Must go up and iterate parent folder from subfolder next sibling
      # parentFolder = parentFoldersArr[ len(parentFoldersArr) - 2 ]
      # pos = parentFolder.index(arr)

      # parentFolder = parentFolder[:-2]
      # adressArr = adressArr[:-1]

      # a = iterateDir(parentFolder, pos)
      # if a != False:
      #   return a

    # return False

  def formAdressString(name):
    result = adressArr[0]
    for item in adressArr[1:]:
      result = result + '/' + item
    result = result + '/' + name
    return result

  return iterateDir(folder)

print 'test, second folder            : ' + str(file_search(['C:', ['eee', 'rrr', 'ttt'], ['yyy', 'ideas.txt']], 'ideas.txt') )

# print 'test, empty folder            : ' + str(file_search(['C:'], 'ideas.txt') )
# print 'test, simple                  : ' + str(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt') )
# print 'test, in subfolder            : ' + str(file_search(['C:', 'backup.log', ['dir', 'ideas.txt']], 'ideas.txt') )
# print 'test, empty folder before     : ' + str(file_search(['C:', 'backup.log', ['dir'], 'ideas.txt'], 'ideas.txt') )
# print 'test, not empty folder before : ' + str(file_search(['C:', 'backup.log', ['dir','q'], 'ideas.txt'], 'ideas.txt') )
# print 'test, hard variant plus       : ' + str(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py') )
# print 'test, hard variant minus      : ' + str(file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me') )



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