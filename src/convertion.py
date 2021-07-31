
def converted(selected,path,dest,mydir):
    
    if selected == 0 :
        import cv2
        import numpy as np
        output= mydir

        
        
        #image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        #image1 = cv2.cvtColor(path, cv2.COLOR_BGR2GRAY )
#        print(Input)
        Input=dest+'/'+path
        print(Input)
        
        from PIL import Image 
        image_file = Image.open(Input) # open colour image
        #image_file = image_file.convert('1') # convert image to black and white
        image_file.save(output)
        print("RGB")
    elif selected == 1 :
        import cv2
        import numpy as np
        output=mydir 
        
        Input=dest+'/'+path
        print(Input)
        image = cv2.imread(Input,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(output,image)
        print("Gray")
    else:
        import cv2
        import numpy as np
        output=mydir 
        
        Input=dest+"/"+path
        print(Input)
#        image = cv2.imread(Input,cv2.IMREAD_GRAYSCALE)
#        cv2.imwrite(output+path,image)
        from PIL import Image 
        import os
        Image.open(Input).save(output+'test1.png')
        image_file = cv2.imread(output+'test1.png') # open colour image
        image_file = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
        #image_file = image_file.convert('1') # convert image to black and white
        ret,gray=cv2.threshold(image_file,120,256,cv2.THRESH_BINARY)
        
        cv2.imwrite(output,gray)
        os.remove(output+'test1.png')
        print("Binary")
        
    
        #from PIL import Image 
        #image_file = Image.open(Input) # open colour image
        #image_file = image_file.convert('1') # convert image to black and white
        #image_file.save(output+path)
#        from PIL import Image
#        img = Image.open(Input).convert('LA')
#        img.save(output+path)
#        print("Saved : "+path)
