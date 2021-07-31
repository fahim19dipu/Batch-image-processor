
def backSUB(path):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    
    img = cv2.imread(path, -1)
    
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    masked_image = fgbg.apply(img)
    
    masked_image[masked_image==127]=255
    cv2.imwrite("ALT.png",masked_image)
def remove_shadow(path,dest,mydir):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    
    output=mydir 
    Input=output
    print(Input)
    
    img = cv2.imread(Input,-1)
    
    rgb_planes = cv2.split(img)
    
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        #print("asdasdsd")
        dilated_img = cv2.dilate(plane, np.ones((50,50), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)  
        norm_img = cv2.normalize(diff_img, None)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)
    
    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    #cv2.imwrite("SW_2",result_norm)
    cv2.imwrite(output, result)
    print("shadow_outed")