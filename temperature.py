def konversisuhu(temperature, value):
    # Cek apakah 'value' adalah 'C' (Celsius)
    if value == 'C':
        # Konversi dari Fahrenheit ke Celsius
        temparaturesuhu = (temperature - 32) * 5/9
        return temparaturesuhu, 'C'
    else:
        # Jika bukan 'C', konversi dari Celsius ke Fahrenheit
        temparaturesuhu = (temperature * 9/5) + 32
        return temparaturesuhu, 'F'
    
celsius_temperature = 30
# Panggil fungsi untuk mengonversi ke Fahrenheit
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
# Cetak hasil konversi dari Celsius ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

fahrenhait_temperature = 86
# Panggil fungsi untuk mengonversi ke Celsius
temperaturesuhu, target_value = konversisuhu(fahrenhait_temperature, 'C')
# Cetak hasil konversi dari Fahrenheit ke Celsius
print(f"{fahrenhait_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}")