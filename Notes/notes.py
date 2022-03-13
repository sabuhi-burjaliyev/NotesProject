import sys

comingcomand = sys.argv[-1]

commands = comingcomand.split('_')

if commands[0] == 'commands':
    print('new_<filename>\nadd_<filename>_<content>\ndelete_<filename>_<content>')

if commands[0]=='new':
    document = open('{}.txt'.format(commands[1]),'w')
    document.close()

if commands[0]=='add':
    with open('{}.txt'.format(commands[1]),'a') as document:
        document.write('{}\n'.format(commands[2]))

if commands[0]=='delete':
    newcontent = str()
    with open('{}.txt'.format(commands[1]),'r') as document:
        content=document.read()
        newcontent = content.strip('{}\n'.format(commands[2]))

    with open('{}.txt'.format(commands[1]),'w') as document:
        document.write(newcontent)