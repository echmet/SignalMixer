import os, psutil, sys

purge = False
minSize = 0

if len(sys.argv) > 1:
    if sys.argv[1] == 'purge':
        purge = True
        if len(sys.argv) > 2:
            minSize = int(sys.argv[2])
		

#set the base path of the freezed executable; (might change,
#check the last part for different architectures and python versions
basePath = 'C:\\Building\\ECHMET\\Python\\SignalMixer\\build\\exe.win32-3.6'
#look for current processes and break when my program is found;
#be sure that the name is unique
for procId in psutil.pids():
    proc = psutil.Process(procId)
    if proc.name().lower() == 'themixer.exe':
        break
    proc = None

if proc is None:
    print('Process not found, aborting...')
    sys.exit(1)

#search for its dependencies and build a list of those *inside*
#its path, ignoring system deps in C:\Windows, etc.
deps = [p.path.lower() for p in proc.memory_maps() if p.path.lower().startswith(basePath)]

#create a list of all files inside the build path
allFiles = []
for root, dirs, files in os.walk(basePath):
    for fileName in files:
        filePath = os.path.join(root, fileName).lower()
        allFiles.append(filePath)

#create a list of existing files not required, ignoring .pyc and .pyd files
unusedSet = set(allFiles) ^ set(deps)
unusedFiles = []
for filePath in sorted(unusedSet):
    if filePath.endswith('pyc') or filePath.endswith('pyd'):
        continue
    unusedFiles.append((filePath[len(basePath):], os.stat(filePath).st_size))

out = open('rtdeps.txt', 'w')
totalSize = 0
totalRemovedSize = 0
	
#print the list, sorted by size
for filePath, size in sorted(unusedFiles, key=lambda d: d[1]):
    out.write('{} {}\n'.format(filePath, size))
    totalSize += size
    if purge:
        def allowedSuffixes(suffixList):
            for suffix in suffixList:
                if filePath.endswith('.' + suffix):
                    return True
            return False

        fullPath = basePath + filePath
        try:
            if not allowedSuffixes(['dll', 'qmlc', 'py', 'qml', 'exe', 'txt']):
                msg = 'Not removing {}'.format(filePath)
                out.write(msg + '\n')
                print(msg)
                continue
            if size > minSize:
                os.unlink(fullPath)
                totalRemovedSize += size
        except OSError:
            msg = 'Cannot remove {}'.format(filePath)
            out.write(msg + '\n')
            print(msg)


out.write('Total size: {}\n'.format(totalSize))
print('Total size: {}'.format(totalSize))
print('Total removed size: {}'.format(totalRemovedSize))
