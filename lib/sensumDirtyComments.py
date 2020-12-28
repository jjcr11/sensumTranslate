#!/usr/bin/python3

from __init__ import *
import common

class SensumDirtyComments:
    
    def __init__(self):
        common.printSensumDirtyComments()
        common.countFiles("../data/dirty_comments/")
        common.enterToContinue()
        self._data = pd.DataFrame()
        
    def main(self):
        files = self.getFilesNames()
        self.readFormandAndSaveFiles(files)