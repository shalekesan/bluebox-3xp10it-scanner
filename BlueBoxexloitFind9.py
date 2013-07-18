#-------------------------------------------------------------------------------
# Name:        BlueBox3xp10!tfinder
# Purpose:      Detects apk files with bluebox exp10!t
#
# Author:      Palaniyappan Bala
#
# Created:     18/07/2013
# Copyright:   (c) Vicatec Research & Analysis Lab 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
import zipfile, sys



def isexp10it(apk):
    flag= False
    List = []
    fh = open(apk, 'r')
    z = zipfile.ZipFile(fh)
    for zip_entry in z.namelist():
        List.append(zip_entry)
    fh.close()
    if len(List) != len(set(List)):
        print "\nMalicious: BlueBox 3xp10!t Found!!!"
        flag=True
    else:
        print "\nSAFE: File is good to use !!!"
    return flag



def main():
    if(len(sys.argv)<1):
        print "Blueboxex10itFind.py <file>\n"
        print "file - APK/ZIP file "
        return
    apk=sys.argv[1]
    isexp10it(apk)

    pass

if __name__ == '__main__':
    main()
