# Импорт переменных из файла src/config.py
from src.config import ENCODINGS, FILE_LOLLIPOPS, FILE_ECONOM, FILE_DIGIT


# цикл для определения кодировки у файла
count_enc = 0
for enc in ENCODINGS:
    try:
        FILE_DIGIT.read_text(encoding=enc)
        enc_show = enc
        break
    except UnicodeDecodeError:
        pass
    count_enc += 1

# вывод кодировки и её порядкового номера в списке ENCODINGS[]
print("Кодировка:", enc or "не нашел нужную кодировку")
print("Порядковый номер кодировки:", count_enc)
