def buah(normal_parameter,*args):
    """function toko buah"""
    print("Toko buah koperasi UNJANI Yogyakarta")
    print("Masukan banyaknya buah yang dibeli :{}".format(normal_parameter))
    for index, arg in enumerate (args):
        print("Buah {} : {}".format(index+1,arg))

buah(4,"apel","semangka","jeruk","anggur")          