
def resized(path,dest,height,width,mydir):
    from PIL import Image
    import PIL
    output=mydir 
    Input=output
    img = Image.open(Input)
    img = img.resize((width,height),PIL.Image.ANTIALIAS)
    img.save(output)
    print("resized")
