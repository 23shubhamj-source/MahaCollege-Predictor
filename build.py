"""
MahaCollege Predictor 2026 - Build Script
Combines the HTML template with the embedded data to produce index.html
"""
import os

DATA_JS_PATH = r'C:\Users\shubh\.gemini\antigravity\scratch\mahacollege-predictor-2026\src\data\data.js'
OUTPUT_PATH = r'C:\Users\shubh\.gemini\antigravity\scratch\mahacollege-predictor-2026\index.html'
TEMPLATE_PATH = r'C:\Users\shubh\.gemini\antigravity\scratch\mahacollege-predictor-2026\src\template.html'

def build():
    print("Reading data...")
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        data_js = f.read()
    print(f"Data size: {len(data_js):,} chars")

    print("Reading template...")
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    print(f"Template size: {len(template):,} chars")

    print("Injecting data into template...")
    result = template.replace('/* __DATA_PLACEHOLDER__ */', data_js)

    print(f"Output size: {len(result):,} chars")
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(result)

    size_mb = os.path.getsize(OUTPUT_PATH) / 1024 / 1024
    print(f"Written to: {OUTPUT_PATH}")
    print(f"File size: {size_mb:.2f} MB")
    print("Done!")

if __name__ == '__main__':
    build()
