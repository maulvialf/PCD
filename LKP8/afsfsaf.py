# Kelas LVQ.
class LVQ:
    # Constructer dari kelas LVQ
    # Berisi parameter dataset, kelas/labels, epoch/iterasi, dan learning rate
    def __init__(self, dataset, labels, epochs=50, learning_rate=0.5):
        # inisiasi atribute
        # dataset
        self.dataset = dataset
        # ubah kelas atribute dari numpy datatype menjadi array
        self.labels = np.asarray(labels)
        # ambil jumlah record
        self.row = self.dataset.shape[0]
        # ambil jumlah kolom
        self.column = self.dataset.shape[1]
        # total kelas
        self.total_labels = len(set(self.labels))
        # inisiasi weigth
        self.weight = self.generate_weights()
        # isi nilai epoch
        self.epochs = epochs
        # isi kelas prediksi
        self.labels_pred = list(set(self.labels))
        # isi learning rate
        self.learning_rate = learning_rate
    
    # Fungsi train akan melakukan pelatihan weight pada Jaringan LVQ
    # sesuai dataset
    def train(self):
        # loop sebanyak epoch
        for epoch in range(self.epochs):
            # loop sebanyak jumlah record
            for row in range(self.row):
                # hitung eucladian distance dari dua data
                euc_dist = np.sum(np.abs(np.asarray(self.dataset.iloc[row])-self.weight)**2, axis=-1)
                # dalam LVQ, terdapat kompetisi untuk mendapatkan nilai minimum
                # pilih index dengan euc distance paling kecil.
                min_index = np.argmin(euc_dist)
                # Jika kelas prediksi sama dengan kelas pemenang dekatkan weight
                if self.labels_pred[min_index] == self.labels[row]:
                    self.weight[min_index]  += self.learning_rate * (self.dataset.iloc[row] - self.weight[min_index])
                # Jika kelas prediksi tidak sama dengan kelas pemenang dekatkan jauhkan weight
                else:
                    self.weight[min_index]  -= self.learning_rate * (self.dataset.iloc[row] - self.weight[min_index])      
            # Info epoch
            print("Epoch :", epoch)
            # Kecilkan learning rate
            self.learning_rate /= 2
    
    # Fungsi generate_weights akan mereturn nilai random
    # sebanyak kolom x label
    def generate_weights(self):
        # generate weight random untuk inisiasi
        return np.random.uniform(0.0, 1.0, (self.total_labels, self.column))
    
    # Return nilai weight. Agar nilai weigth dapat diambil diluar kelas LVQ
    def get_weights(self):
        # dapatkan nilai weight
        return self.weight
    

    # Fungsi prediksi untuk menghitung akurasi LVQ
    def predict(self, testX, testY):
        # Ambil total record
        total_row = testY.size
        # konversi menjadi array
        testY = np.asarray(testY)
        # inisiasi jumlah predicted
        predicted = 0
        # loop semua record
        for row in range(total_row):
            # hitung eucladian distance
            euc_dist = np.sum(np.abs(np.asarray(testX.iloc[row])-self.weight)**2, axis=-1)
            # nilai minimum dari hasil kompetisi jaringan
            min_index = np.argmin(euc_dist)
            if self.labels_pred[min_index] == testY[row]:
                # jika kelas benar. ingkeremen nilai predicted
                predicted+=1

        # return persentase akurasi
        return predicted/total_row