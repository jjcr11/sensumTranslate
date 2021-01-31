from __init__ import *
import common
import sensumTranslator as st

class SensumSpanishPosts:
    
    def __init__(self):
        common.printSensumSpanishComments()
        common.countFiles("../data/spanish_posts/")
        common.enterToContinue()
        
    def main(self):
        files = self.getFilesNames()
        self.readFormandAndSaveFiles(files)
        pass

    def getFilesNames(self):
        files = glob.glob("../data/spanish_posts/*.xlsx")
        return files

    def readFormandAndSaveFiles(self, files):
        for file in files:
            print('--> Uploading: ' + file)
            df = self.readAndFormatData(file)
            file = common.cleanFileName(file)
            self.saveFile(df, file)
        common.printLine()
        print('Your spanish data is now translated')
        common.printLine()

    def readAndFormatData(self, file):
        df = self.readExcel(file)
        df = self.translate(df)
        return df

    def readExcel(self, file):
        df = pd.read_excel(file)
        #dfh = df.head(10)
        return df

    def translate(self, df):
        translator = st.SensumTranslator()
        for i in range(len(df)):
            if(pd.isnull(df['message'][i])):
                pass
            else:
                df['message'][i] = translator.toTranslate(df['message'][i])
        return df
             

    def saveFile(self ,df, name):
        print(f'--> Saving file')
        df.to_excel(f'../output/PostsIngles.xlsx', index=False)
        print(f'--> Saved file: output/PostsIngles.xlsx')