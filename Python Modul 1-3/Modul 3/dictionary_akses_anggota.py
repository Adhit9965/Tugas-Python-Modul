dict_saya = {'nama':'Budi', 'usia':27}

#output:  Budi
print(dict_saya['nama'])

#output: 27
print(dict_saya.get('usia'))

#output None
print(dict_saya.get('alamat'))

#mengakses kunci yang tidak tersedia menyebabkan keyerror
#dict_saya['alamat']