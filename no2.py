def mahasiswa(nama,nim,prodi,hobi):
    """function profil mahasiswa"""
    print("Profil Mahasiswa UNJANI Yogyakarta")
    print("Nama : {}".format(nama))
    print("NIM : {}".format(nim))
    print("Prodi : {}".format(prodi))
    print("Hobi : {}".format(hobi))
    
pelajar = {'nama':"Lidiya",'nim':"232102001",'prodi':"informatika",'hobi':"nyanyi"}
mahasiswa(**pelajar)             