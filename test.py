from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img
COLOR = "grayscale"   # "rgb", "rgba", "grayscale"
IMG_SIZE = (50,50)    # 画像サイズ
img = load_img("./image/3.png",color_mode=COLOR,target_size=IMG_SIZE)
img_array = img_to_array(img)
save_img("./image/new_sample.png", img_array)