# DDP-Minpro-2
Nama: Azhaar Athahiroh, NIM: 2409116057, Kelas: B, Tema: Jasa Cooking Class
# Flowchart
![image](https://github.com/user-attachments/assets/50d3c55d-b91d-4fe9-8527-d0e2f56408fc)

# Penjelasan dan Output

![image](https://github.com/user-attachments/assets/c7a3e43d-3cd2-4b9a-a35c-2d78a77ca1ac)

Disini saya sebagai user, rolenya sebagai admin.

![image](https://github.com/user-attachments/assets/f91084aa-33bb-42a8-aeaa-7d01900de039)

Ini daftar kelas memasak yang tersedia. Masing masing punya kode kelas, nama kelas, harga per kelas, jadwal kapan kelasnya diadakan, dan jumlah slot yang masih kosong. Jadi pembeli bisa memilih kelas sesuai slot yang ada.

![image](https://github.com/user-attachments/assets/21ea3e8d-69bb-4fc3-b7ec-81e1c698bc0c)

Ini buat login. Program minta input username dan password. Kalau cocok dengan data di users, kita berhasil login. Kalo salah, akan muncul error.

![image](https://github.com/user-attachments/assets/cda08466-8d72-45df-94be-9a61467f78c9)

Ini contoh Input untuk yang username sekaligus password dan Output yang tulisan login berhasil.

![image](https://github.com/user-attachments/assets/ffce69ef-e563-4954-8ac9-59278e75f3da)

Setelah login, kita disuruh memilih role atau peran. Ada 2 opsi, yaitu admin atau pembeli. Kalau pilih admin, kita bisa ngelola kelas seperti menambah dan menghapus kelas. Kalau pilih pembeli, kita bisa melihat daftar kelas dan daftar ke salah satu kelas.

![image](https://github.com/user-attachments/assets/6b15d7f9-0198-4d04-bd97-2932ce97e072)

Contoh input, yaitu saya memasukkan pilihan saya dan outputnya akan memunculkan menu admin.

![image](https://github.com/user-attachments/assets/b0e234e7-dbb2-489a-9737-0bd089a0dce4)

Fungsi ini untuk menampilkan daftar kelas memasak yang tersedia. Tabel yang dipakai library PrettyTable, jadi tampilan lebih rapi.

![image](https://github.com/user-attachments/assets/6bbc2363-82e4-4883-9aef-92f690868f5c)

Contoh output beberapa daftar kelas masakan

![image](https://github.com/user-attachments/assets/f57f206f-0012-4adb-89e0-69457a4f914d)

Admin memakai fungsi ini untuk menambah kelas baru. Kelas yang ditambahkan otomatis masuk ke dalam list cooking_class.

![image](https://github.com/user-attachments/assets/82c8599a-18db-4fd1-bef4-07b67a1e77cb)

Contoh Input (Masukkan semua dari kode kelas sampai slot kelas) sekaligus Output (Kelas sate ayam sudah berhasil ditambah)

![image](https://github.com/user-attachments/assets/08969cf6-b1f5-4689-a3ce-3b3581ccc532)

Admin bisa menghapus kelas berdasarkan kode kelas. Kalau kelasnya ada, langsung dihapus. Kalau tidak ada, program bakal kasih tau kalau kode kelasnya gak ditemukan.

![image](https://github.com/user-attachments/assets/2e7d537f-f557-4ade-bda2-ffa74f2f2726)

Ini contoh input kode kelas yang ingin dihapus, output untuk melihat apakah kode kelas berhasil dihapus.

![image](https://github.com/user-attachments/assets/e2434120-ebdd-4e5f-be61-8b54c92757fe)

Fungsi ini dipakai oleh pembeli untuk daftar ke kelas masak. Caranya, kita pilih kelas berdasarkan kode kelas yang tersedia. Kalau slot masih ada, kita bisa daftar. Kalau slotnya sudah penuh, kita akan dapat pesan kalau kelasnnya penuh.

![image](https://github.com/user-attachments/assets/b27904af-b334-47ed-b96c-953fe671de70)

Ini input untuk kode kelas yang ingin diikuti sedangkan output menunjukkan hasil berhasil mendaftar kekelas bebek goreng sehingga yang awalnya ada 6 slot sisa 5 slot.

![image](https://github.com/user-attachments/assets/6e21833e-df33-4660-ae5a-bfd65ab2e94d)
![image](https://github.com/user-attachments/assets/d44aa411-fce1-4080-95ac-f324dddd6990)

![image](https://github.com/user-attachments/assets/3349e2a0-e8f0-40de-86e4-5dcd636bf254)
![image](https://github.com/user-attachments/assets/fa3048fd-3160-4dbd-904b-897a9a16fd28)

Ini fungsi yang menampilkan menu sesuai peran yang kita pilih, kalau admin kita bisa hapus kelas dan tambah kelas. Kalau pembeli, kita bisa lihat daftar kelas dan daftar ke kelas yang kita mau.

![image](https://github.com/user-attachments/assets/501947a9-11f3-43e5-b3d3-31eb8f983c85)

Ini bagian memastikan fungsi login() hanya akan dijalankan kalau kita yang langsung menjalankan file ini. jadi, kalau ada orang yang mau menggunakan kode ini di file lain, fungsi loginnya nggak bakal langsung jalan.
