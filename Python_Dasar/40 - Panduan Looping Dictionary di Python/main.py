# Panduan Looping Dictionary di Python

# Membuat sebuah dictionary
data_dict = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}

# Metode Looping Dictionary
## 1. Looping Standar
print("Looping Standar: ")
for key in data_dict:
    print(f"Key: {key}, Value: {data_dict[key]}")

## 2. Looping dengan .items() (Key dan Value)
print("\nLooping dengan .items(): ")
for key, value in data_dict.items():
    print(f"Key: {key}, Value: {value}")

## 3. Looping dengan .keys() (Hanya Key)
print("\nLooping dengan .keys(): ")
for key in data_dict.keys():
    print(f"Key: {key}")

## 4. Looping dengan .values() (Hanya Value)
print("\nLooping dengan .values(): ")
for value in data_dict.values():
    print(f"Value: {value}")