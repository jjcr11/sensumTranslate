#!/usr/bin/python3

import os

def printSensumDirtyComments():
    printLine()
    print('========================================================')
    print('=========== SENSUM DIRTY COMMENTS MODULE =============')
    print('========================================================')
    printLine()

def printSensumDirtyPosts():
    printLine()
    print('========================================================')
    print('=========== SENSUM DIRTY POSTS MODULE =============')
    print('========================================================')
    printLine()

def printSensumCleanComments():
    printLine()
    print('========================================================')
    print('=========== SENSUM CLEAN COMMENTS MODULE =============')
    print('========================================================')
    printLine()

def printSensumCleanPosts():
    printLine()
    print('========================================================')
    print('=========== SENSUM CLEAN POSTS MODULE ================')
    print('========================================================')
    printLine()

def printSensumJoinCleanFiles():
    printLine()
    print('========================================================')
    print('============ SENSUM JOIN CLEAN FILES =================')
    print('========================================================')
    printLine()

def printRenamingDfColumns():
    printLine()
    print('========================================================')
    print('================ RENAMING DF COLUMNS ===================')
    print('========================================================')
    printLine()

def printCleanningComments():
    printLine()
    print('========================================================')
    print('================= CLEANING COMMENTS ====================')
    print('========================================================')

def printSavingFile():
    printLine()
    print('========================================================')
    print('=================== SAVING FILE =======================')
    print('========================================================')
    printLine()

def printPreviewingData():
    printLine()
    print('========================================================')
    print('================== PREVIWEING DATA =====================')
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