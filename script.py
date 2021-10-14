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
                c6=(num[0])
                c7=(num[1])
                c8=(num[2])
                c9=(num[3])

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
    
    print(textStr)

   


    

    outputData=[c1,c2,c3,c4,c5,c6,c7,c8,c9,textStr]
    return outputData




            
            
                


def StringTrim(data_list):
    output=[[]]
    master=""
    for str in data_list:
        if(str[0].isdigit()):
            master=str[:6]
        else:
            str = re.sub(r"^\s+", "", str)
            if(str[0].isdigit()):
                outputData=StringManipulate(str,master,0)
                output.append(outputData)
            else:
                outputData=StringManipulate(str,master,1)
                output.append(outputData)

    return output



def main():

    # path=input("Enter path of file to be executed:")
    # fileName=""
    # for i in reversed(range(len(path))):
    #     if(path[i]=="/"):
    #         break
    #     else:
    #         fileName=path[i]+fileName
    # fileName.replace("txt","xlsx")

    df = pd.read_csv(
        r'C:\Users\sahil\OneDrive\Desktop\Oliver\1990to1991CountyMigration\1990to1991CountyMigrationInflow\C9091aki.txt', sep='\t', names=["Data"])
    df.to_excel(r'output.xlsx',index=None)
    data_list=df["Data"].tolist()
    output=StringTrim(data_list)
    # print(output)
    # print(data_list)
    # print(StringTrim(data_list[2]))

    df = pd.DataFrame.from_records(output,columns=["C1","C2","C3","C4","C5","C6","C7","C8","C9","Text"])
    df.to_excel(r'C:\Users\sahil\OneDrive\Desktop\Oliver\Output\1990to1991\I\C9091aki.xlsx', index=None)



if __name__ == "__main__":
    main()


    


