import os
import hashlib
import re
from markitdown import MarkItDown
from multiprocessing import Pool, cpu_count

def get_all_files_in_directory(directory):
    return [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files]

def generate_unique_filename(file_path, output_folder):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    file_hash = hashlib.md5(file_path.encode()).hexdigest()[:8]
    return f"{base_name}_{file_hash}.md"

def clean_markdown_content(content):
    # 특수 문자 제거
    content = re.sub(r'[^\w\s\n]', '', content)
    
    lines = content.split('\n')
    cleaned_lines = []
    prev_line = ""
    
    for line in lines:
        line = line.strip()
        
        # 빈 줄 제거
        if not line:
            continue
        
        # 윗줄과 동일한 내용 제거
        if line == prev_line:
            continue
        
        # 5글자 이하 줄 제거
        if len(line) <= 5:
            continue
        
        # 숫자만 있는 줄 제거
        if line.isdigit():
            continue
        
        # 중복 단어 제거
        words = line.split()
        seen = set()
        cleaned_words = []
        for word in words:
            if word.lower() not in seen:
                cleaned_words.append(word)
                seen.add(word.lower())
        
        cleaned_line = ' '.join(cleaned_words)
        cleaned_lines.append(cleaned_line)
        prev_line = cleaned_line
    
    return '\n'.join(cleaned_lines)

def convert_file(args):
    file_path, output_folder = args
    markitdown = MarkItDown()
    
    try:
        result = markitdown.convert(file_path)
        cleaned_content = clean_markdown_content(result.text_content)
        output_filename = generate_unique_filename(file_path, output_folder)
        output_path = os.path.join(output_folder, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        return f"Converted and cleaned {file_path} to {output_filename}"
    except Exception as e:
        return f"Error converting {file_path}: {str(e)}"

def convert_files_to_markdown():
    input_folder = 'input'
    output_folder = 'output'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    all_files = get_all_files_in_directory(input_folder)
    
    num_processes = cpu_count()
    with Pool(num_processes) as pool:
        results = pool.map(convert_file, [(file, output_folder) for file in all_files])
    
    for result in results:
        print(result)

if __name__ == "__main__":
    convert_files_to_markdown()
