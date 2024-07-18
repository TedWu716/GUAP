import json

def parse_tax_laws(file_path):
    laws = []
    current_article = None 
    current_content = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == '[Article]':
                if current_article:
                    laws.append({
                        "article": current_article,
                        "content": ' '.join(current_content).strip()
                    })
                current_article = None
                current_content = []
            elif line == '[Content]':
                continue
            elif current_article is None:
                current_article = line
            else:
                current_content.append(line)

    if current_article:
        laws.append({
            "article": current_article,
            "content": ' '.join(current_content).strip()
        })

    return {"laws": laws}

# Parse the text file
parsed_laws = parse_tax_laws('tax_laws.txt')

# Write to JSON file
with open('tax_laws.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_laws, f, ensure_ascii=False, indent=2)

print("JSON file created: tax_laws.json")
