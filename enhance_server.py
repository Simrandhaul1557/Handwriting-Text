from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import re

app = Flask(__name__)
CORS(app)

# Use the public grammar correction model
enhancer = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

def clean_ocr_code(text):
    # Common OCR word corrections
    word_map = {
        'defin': 'def',
        'pritn': 'print',
        'retrun': 'return',
        'functoin': 'function',
        'intput': 'input',
        'lenght': 'length',
        'breath': 'breadth',
        'i n': 'in',
        'I ': 'if ',
        'wihle': 'while',
        'fro': 'for',
        'elese': 'else',
        'elif': 'elif',
        'whiel': 'while',
        'raange': 'range',
        'apend': 'append',
        'retun': 'return',
        'flase': 'false',
        'ture': 'true',
        'Fasle': 'False',
        'Ture': 'True',
        'prnit': 'print',
        'improt': 'import',
        'form': 'from',
        'aslo': 'also',
        'clas': 'class',
        'staic': 'static',
        'pubic': 'public',
        'pritn': 'print',
        'funciton': 'function',
        'retunr': 'return',
        'lenght': 'length',
        'breath': 'breadth',
        'intput': 'input',
        'funtion': 'function',
        'parmeter': 'parameter',
        'parmeters': 'parameters',
        'statment': 'statement',
        'statments': 'statements',
        'condtion': 'condition',
        'condtions': 'conditions',
        'exmaple': 'example',
        'exmaples': 'examples',
        'varible': 'variable',
        'varibles': 'variables',
        'statemnt': 'statement',
        'statemnts': 'statements',
        'functon': 'function',
        'functons': 'functions',
        'paranthesis': 'parenthesis',
        'parantheses': 'parentheses',
        'arguement': 'argument',
        'arguements': 'arguments',
        'paramter': 'parameter',
        'paramters': 'parameters',
        'parmeter': 'parameter',
        'parmeters': 'parameters',
        'statment': 'statement',
        'statments': 'statements',
        'condtion': 'condition',
        'condtions': 'conditions',
        'exmaple': 'example',
        'exmaples': 'examples',
        'varible': 'variable',
        'varibles': 'variables',
        'statemnt': 'statement',
        'statemnts': 'statements',
        'functon': 'function',
        'functons': 'functions',
        'paranthesis': 'parenthesis',
        'parantheses': 'parentheses',
        'arguement': 'argument',
        'arguements': 'arguments',
        'paramter': 'parameter',
        'paramters': 'parameters',
    }
    # Replace common OCR mistakes and keep line breaks
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        # Replace isolated 'l' with '1'
        line = re.sub(r'\bl\b', '1', line)
        line = line.replace('O', '0')
        # Word-level corrections
        for wrong, right in word_map.items():
            line = re.sub(r'\b' + re.escape(wrong) + r'\b', right, line, flags=re.IGNORECASE)
        # Remove extra spaces
        line = re.sub(r' +', ' ', line)
        cleaned_lines.append(line.strip())
    # Join lines with a single line break to preserve original structure
    return '\n'.join(cleaned_lines)

@app.route('/enhance', methods=['POST'])
def enhance():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'enhanced': ''})
    cleaned = clean_ocr_code(text)
    result = enhancer(cleaned, max_length=256, do_sample=False)
    enhanced = result[0]['generated_text']
    return jsonify({'enhanced': enhanced})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 