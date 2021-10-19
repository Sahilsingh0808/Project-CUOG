import pandas as pd
import re


def removeSpaces(str):
    return str.strip()


def StringManipulate(str,master,check):
    # print(str)
    if(check==0):   #string starts with number
        c1=master[0:2]
        c2=master[3:6]
        c3=str[0:2]
        c4=str[3:6]
        c5 = "N/A"
        c5No=-1
        c6="N/A"
        c7="N/A"
        c8="N/A"
        c9 = "N/A"
        textStr=""
        for i in range(len(str)-4):
            if(str[i]==" " and str[i+1].isalpha()
            and str[i+2].isalpha() and str[i+3]==" " and i>8):
                c5=str[i+1:i+3]
                c5No=i+3
                break


        if(c5No!=-1):   #with country code
            for i in range(c5No,len(str)):
                if(str[i].isdigit()):
                    numStr=str[i:]
                    numStr.strip()
                    numStr = re.sub(' +', ' ', numStr)
                    num=numStr.split(" ")
                    c6=(num[0])
                    c7=(num[1])
                    c8=(num[2])
                    c9=(num[3])
                    
                    textStr=str[6:c5No-3]
                    break

        else:   #without country code
            for i in range(6, len(str)):
                if(str[i].isdigit()):
                    c5No = i
                    break
              
            for i in range(c5No, len(str)):
                if(str[i].isdigit()):
                    numStr = str[i:]
                    numStr.strip()
                    numStr = re.sub(' +', ' ', numStr)
                    num = numStr.split(" ")
                    # print(c5No)
                    c6 = (num[0])
                    c7 = "N/A"
                    c8 = (num[1])
                    c9 = "N/A"
                    textStr=str[6:c5No]
                    break



    elif(check ==1):    #string starts with character
        c1=master[0:2]
        c2=master[3:6]
        c3="N/A"
        c4="N/A"
        c5="N/A"
        for i in range(len(str)-1):
            if(str[i].isdigit() and str[i+1]!=":"):
                numStr=str[i:]
                numStr.strip()
                numStr = re.sub(' +', ' ', numStr)
                num=numStr.split(" ")
                # print(num)
                try:
                    c6=num[0]
                except IndexError:
                    c6="N/A"
                try:
                    c7 = num[0]
                except IndexError:
                    c7 = "N/A"
                try:
                    c8 = num[0]
                except IndexError:
                    c8 = "N/A"
                try:
                    c9 = num[0]
                except IndexError:
                    c9 = "N/A"
                

                textStr=str[0:i]
                break

    textStr.strip()
    textStr = re.sub(' +', ' ', textStr)

    c1=removeSpaces(c1)
    c2=removeSpaces(c2)
    c3=removeSpaces(c3)
    c4=removeSpaces(c4)
    c5=removeSpaces(c5)
    c6=removeSpaces(c6)
    c7=removeSpaces(c7)
    c8=removeSpaces(c8)
    c9=removeSpaces(c9)
    textStr=removeSpaces(textStr)
    

    outputData=[c1,c2,c3,c4,c5,c6,c7,c8,c9,textStr]
    return outputData




            
            
                


def StringTrim(data_list):
    output=[[]]
    master=""
    for str in data_list:
        removeSpaces(str)
        if(str[0].isdigit()):
            master=str[:6]
        else:
            str = re.sub(r"^\s+", "", str)
            # print(str)
            if(str[0].isdigit()):
                outputData=StringManipulate(str,master,0)
                output.append(outputData)
            else:
                outputData=StringManipulate(str,master,1)
                output.append(outputData)

    return output



def main():


    #this list contains the keywords for the inflow txt files
    f=['aki','ali','ari','azi','cai','coi','cti','dci','dei','fli','fri','gai','hii','iai','idi','ili','ini','ksi','kyi','lai','mai','mdi','mei','mii','mni',
    'moi','msi','mti','nci','ndi','nei','nhi','nji','nmi','nvi','nyi','ohi','oki','ori','pai','rii','sci','sdi','tni','txi','uti','vai','vti','wai','wii','wvi','wyi']

    #this list contains the keywords for the inflow txt files
    g = ['ako', 'alo', 'aro', 'azo', 'cao', 'coo', 'cto', 'dco', 'deo', 'flo', 'fro', 'gao', 'hio', 'iao', 'ido', 'ilo', 'ino', 'kso', 'kyo', 'lao', 'mao', 'mdo', 'meo', 'mio', 'mno',
         'moo', 'mso', 'mto', 'nco', 'ndo', 'neo', 'nho', 'njo', 'nmo', 'nvo', 'nyo', 'oho', 'oko', 'oro', 'pao', 'rio', 'sco', 'sdo', 'tno', 'txo', 'uto', 'vao', 'vto', 'wao', 'wio', 'wvo', 'wyo']

    #this for loop is used to run all the files at once
    for i in range(52):

        #change the input and output path of the txt and xlsx files respectively according to your need
        inPath = r"C:\Users\sahil\OneDrive\Desktop\Oliver\1991to1992CountyMigration\1991to1992CountyMigrationOutflow\C9192"+g[i]+".txt"
        outPath = r"C:\Users\sahil\OneDrive\Desktop\Oliver\Output\1991to1992\O\C9192"+g[i]+".xlsx"

        df = pd.read_csv(inPath, sep='\t', names=["Data"])
        df.to_excel(r'output.xlsx',index=None)
        data_list=df["Data"].tolist()
        output=StringTrim(data_list)


        df = pd.DataFrame.from_records(output,columns=["C1","C2","C3","C4","C5","C6","C7","C8","C9","Text"])
        df.to_excel(outPath, index=None)



if __name__ == "__main__":
    main()


    


