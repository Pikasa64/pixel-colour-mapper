from PIL import Image
from colorama import Fore,init
import subprocess as sb

init()

try:
    file_1 = input("enter the source image: ")
    f1_name = file_1.split(".")[0]
    img1 = Image.open(file_1).convert("RGB")
    file_2 = input("enter the destination image: ")
    f2_name = file_2.split(".")[0]
    img2 = Image.open(file_2).convert("RGB")
    dim = input("enter the dimension of two images to be cropped to (keep it low, default is 64): ")
    dim = int(dim) if dim else 64

    img1 = img1.resize((dim,dim))
    img2 = img2.resize((dim,dim))
    new = Image.new("RGB",(dim,dim),(0,0,0))

    pix1 = img1.load()
    pix2 = img2.load()
    pix_new = new.load()
    form = input("what format do you want to save it as? (default PNG): ")
    if form:
        output_file = f"{f1_name}-{f2_name}.{form}"
    else:
        output_file = f"{f1_name}-{f2_name}.png"

    acc = input("Enter the matching tolerance (higher = looser match, default 20): ")
    tolerance = int(acc) if acc else 20
    print(Fore.BLUE+"processing your image...")
    print(Fore.RESET)

    for x in range(0,dim):
        for y in range(0,dim):
            dest = pix2[x,y]
            found = False
            for i in range(0,dim):
                for j in range(0,dim):
                    src = list(pix1[i,j])
                    r,g,b = pix1[i,j]
                    match = True
                    for c in range(0,3):
                        if abs(src[c]-dest[c]) > tolerance:
                                match=False
                                break

                    if match:
                        pix_new[x,y] = (r,g,b)
                        found = True
                        break

                if found:
                    break

    new.save(output_file)
    print(Fore.GREEN+f"image saved as {output_file}")
    print(Fore.RESET)
    Image.open(output_file).show()
except Exception as e:
    print(Fore.RED+f"{e}")
