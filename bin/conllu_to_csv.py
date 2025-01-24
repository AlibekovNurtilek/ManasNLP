import csv

def conllu_to_csv(conllu_file, csv_file):
    with open(conllu_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Заголовки для CSV (на основе CoNLL-U)
        headers = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS', 'FEATS', 'HEAD', 'DEPREL', 'DEPS', 'MISC']
        writer.writerow(headers)
        
        for line in infile:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Игнорируем комментарии и пустые строки
            fields = line.split('\t')
            writer.writerow(fields)
    
    print(f"Файл успешно конвертирован в CSV: {csv_file}")

# Пример использования
conllu_to_csv('data/ky_ktmu-ud-test.conllu', 'data/ky_ktmu-ud-test.csv')
