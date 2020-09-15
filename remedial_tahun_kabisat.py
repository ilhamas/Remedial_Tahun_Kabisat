tahun = int(input('Input tahun :'))               #membuat variabel tahun yang berisi fungsi input tahun yang bertipe data integer
if tahun % 4 == 0 :                               #sesuai soal bahwa setiap 4 tahun sekali jumlah hari akan di tambah 1 dengan kata lain tahun kabisat terjadi setiap 4 tahun sekali maka dibuat kondisi jika tahun modulo 4 sama dengan 0 
    print('Hasil : TAHUN KABISAT')                #Jika kondisi sesuai maka akan di print Hasil : TAHUN KABISAT
else :                                            #Jika kondisi tidak sesuai makan akan di print Hasil : BUKAN TAHUN KABISAT 
    print('Hasil : BUKAN TAHUN KABISAT')
