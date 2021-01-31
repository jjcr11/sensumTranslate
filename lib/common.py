#!/usr/bin/python3

import os

def printSensumSpanishComments():
    printLine()
    print('========================================================')
    print('=========== SENSUM SPANISH POSTS MODULE =============')
    print('========================================================')
    printLine()
        
def countFiles(path):
    path, dirs, files = next(os.walk(f'{path}'))
    file_count = len(files)
    print(f'--> You have {file_count} files')
    printLine()

def cleanTerminal():
    os.system('clear')
    
def enterToContinue():
    input("Press Enter to continue: ")

def printLine():
    print('')
    
def previewData(df):
    print(df.iloc[:3].to_string(index=False))
    
def cleanFileName(file):
    file = str(file)[24:]
    return file

def cleanFilePost(file):
    file = str(file)[20:]
    return file