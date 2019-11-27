from PIL import Image,ImageFilter

#image = Image.open('guido.jpg')
'''
剪裁图像
rect = 80, 20, 310, 360
image.crop(rect).show()
'''
'''
生成略缩图
size = 128,128
image.thumbnail(size)
image.show()
'''

'''
#缩放和黏贴图像

image1 = Image.open('luohao.png')
image2 = Image.open('guido.jpg')
rect = 80,20,310,360
guido_head = image2.crop(rect)
width,height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5),int(height / 1.5))),(172,40))
image1.show()
'''


'''
旋转和翻转
image = Image.open('guido.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
'''

'''
操作像素
image = Image.open('guido.jpg')
for x in range(80,310):
    for y in range(20,360):
        image.putpixel((x,y),(128,128,128))
image.show()
'''

'''
滤镜效果
'''
image = Image.open('guido.jpg')
image.filter(ImageFilter.CONTOUR).show()