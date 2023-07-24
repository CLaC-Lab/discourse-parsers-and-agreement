import os
import json
import csv
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download the tokenizer data if not already present

def find_words(filename, token_list):
    with open(filename, 'r') as file:
        content = file.read()
        words = word_tokenize(content)
        return ' '.join(words[token-1] for token in token_list)

def create_csv_from_json(json_path, output_csv_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    doc_id = data["DocID"]
    arg1_words = find_words(doc_id + '.txt', data["Arg1"]["TokenList"])
    arg2_words = find_words(doc_id + '.txt', data["Arg2"]["TokenList"])
    sense = data["Sense"][0]
    connective_word = find_words(doc_id + '.txt', data["Connective"]["TokenList"])

    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["DocID", "Arg1", "Arg2", "Connective", "Sense"])
        writer.writerow([doc_id, arg1_words, arg2_words, connective_word, sense])

if __name__ == "__main__":

    json_file_path = "output.json"

    csv_output_path = "output.csv"

    create_csv_from_json(json_file_path, csv_output_path)
