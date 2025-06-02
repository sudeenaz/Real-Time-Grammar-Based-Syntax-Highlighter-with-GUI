import re

# Token tipleri
TOKEN_SPECIFICATION = [    
    ('IF',        r'\bif\b'),         # 'if' anahtar kelimesi
    ('ELSE',      r'\belse\b'),       # 'else' anahtar kelimesi
    ('NUMBER',    r'\d+'),            # Sayılar
    ('ID',        r'[a-zA-Z_]\w*'),   # Değişken adları (identifier)
    ('EQ',        r'=='),             # Eşittir karşılaştırma
    ('ASSIGN',    r'='),              # Atama operatörü
    ('PLUS',      r'\+'),             # Toplama operatörü
    ('LPAREN',    r'\('),             # Sol parantez
    ('RPAREN',    r'\)'),             # Sağ parantez
    ('LBRACE',    r'\{'),             # Sol süslü parantez
    ('RBRACE',    r'\}'),             # Sağ süslü parantez
    ('SEMI',      r';'),              # Noktalı virgül
    ('SKIP',      r'[ \t]+'),         # Boşluk ve tab
    ('NEWLINE',   r'\n'),             # Yeni satır
    ('MISMATCH',  r'.'),              # Eşleşmeyen karakter
]


token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
compiled_re = re.compile(token_regex)

def tokenize(code):
    tokens = []
    line_start = 0
    for mo in compiled_re.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        start = mo.start()
        end = mo.end()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', value, start, end))
        elif kind == 'ID':
            tokens.append(('ID', value, start, end))
        elif kind in ('IF', 'ELSE', 'EQ', 'ASSIGN', 'PLUS', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI'):
            tokens.append((kind, value, start, end))
        elif kind == 'SKIP':
            continue
        elif kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Geçersiz karakter: {value!r}')
    return tokens

# Test 
sample_code = """
if (x == 5) {
    y = x + 1;
}
"""

print("Token listesi:")
for token in tokenize(sample_code):
    print(token)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def match(self, expected_type):
        if self.current()[0] == expected_type:
            self.pos += 1
            return True
        else:
            return False

    def parse(self):
        while self.current()[0] != 'EOF':
            if not self.statement():
                print(f"Hata: Geçersiz ifade {self.current()}")
                return False
        print("Başarılı: Tüm ifadeler doğru.")
        return True

    def statement(self):
        if self.match('IF'):
            return self.if_statement()
        elif self.current()[0] == 'ID':
            return self.assignment()
        else:
            return False

    def assignment(self):
        if self.match('ID') and self.match('ASSIGN') and self.expr() and self.match('SEMI'):
            return True
        return False

    def if_statement(self):
        if self.match('LPAREN') and self.expr() and self.match('RPAREN') and self.match('LBRACE'):
            while self.current()[0] != 'RBRACE' and self.current()[0] != 'EOF':
                if not self.statement():
                    return False
            return self.match('RBRACE')
        return False

    def expr(self):
        if not self.term():
            return False
        while self.current()[0] in ('PLUS', 'EQ'):
            self.match(self.current()[0])
            if not self.term():
                return False
        return True

    def term(self):
        token_type = self.current()[0]
        if token_type in ('ID', 'NUMBER'):
            self.match(token_type)
            return True
        return False

import tkinter as tk

sample_code = """
if (x == 5) {
    y = x + 1;
}
"""

root = tk.Tk()
root.title("Real-Time Syntax Highlighter")

text = tk.Text(root, font=("Consolas", 14), wrap="none")
text.insert("1.0", sample_code)  # Başlangıç metni
text.pack(expand=True, fill="both")

COLOR_MAP = {
    'IF': 'blue',
    'ELSE': 'blue',
    'ID': 'black',
    'NUMBER': 'green',
    'EQ': 'orange',
    'ASSIGN': 'orange',
    'PLUS': 'red',
    'LPAREN': 'gray',
    'RPAREN': 'gray',
    'LBRACE': 'gray',
    'RBRACE': 'gray',
    'SEMI': 'purple',
}

# Tag'lere renk atama
for token_type, color in COLOR_MAP.items():
    text.tag_config(token_type, foreground=color)

# Vurgulama fonksiyonu
def highlight(event=None):
    # Tüm tag'leri temizle
    for tag in text.tag_names():
        text.tag_remove(tag, "1.0", "end")
    
    # Mevcut metni al
    text_content = text.get("1.0", "end-1c")
    
    try:
        # Token'ları al
        tokens = tokenize(text_content)
        
        # Her token için renklendirme yap
        for token_type, token_value, start, end in tokens:
            if token_type in COLOR_MAP:
                start_index = f"1.0+{start}c"
                end_index = f"1.0+{end}c"
                text.tag_add(token_type, start_index, end_index)
    except Exception as e:
        # Hata durumunda sadece hatalı kısmı kırmızı yap
        pass

# Her değişiklikte vurgulama yap
text.bind("<KeyRelease>", highlight)
text.bind("<KeyPress>", highlight)
highlight()  # İlk çalıştırma

# Parser sonucu gösteren etiket
result_label = tk.Label(root, text="", font=("Consolas", 12))
result_label.pack()

# Parser buton fonksiyonu
def check_syntax():
    code = text.get("1.0", "end-1c")
    tokens = tokenize(code)
    try:
        parser = Parser(tokens)
        success = parser.parse()
        if success:
            result_label.config(text="Kod gramer açısından geçerli.", fg="green")
        else:
            result_label.config(text="Kod geçersiz.", fg="red")
    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}", fg="red")

# Buton ekle
check_button = tk.Button(root, text="Kodu Kontrol Et", command=check_syntax)
check_button.pack(pady=10)

# Uygulamayı başlat
root.mainloop()

