from pathlib import Path

def merge_conllu_files_with_updated_ids(file1_path, file2_path, output_path):
    current_sent_id = 1  # Начинаем нумерацию с 1

    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2, open(output_path, 'w', encoding='utf-8') as out:
        for file in (f1, f2):
            for line in file:
                if line.startswith("# sent_id"):  
                    out.write(f"# sent_id = {current_sent_id}\n")
                    current_sent_id += 1
                else:
                    out.write(line)
            out.write("\n")  # Добавляем пустую строку между предложениями

if __name__ == "__main__":
    train_file_path = Path("data/ky_ktmu-ud-train.conllu")
    test_file_path = Path("data/ky_ktmu-ud-test.conllu")
    merged_file_path = Path("data/ky_ktmu-ud-merged.conllu")
    
    merge_conllu_files_with_updated_ids(train_file_path, test_file_path, merged_file_path)
    
    print(f"Файлы объединены и сохранены в {merged_file_path}")
