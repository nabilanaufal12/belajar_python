import time

start_time = time.time()

# kode yang ingin diukur waktunya
for i in range(1000):
    a = 10
# akhir kode yang ingin diukur waktunya

end_time = time.time()
print("waktu eksekusi:", end_time - start_time, "detik")