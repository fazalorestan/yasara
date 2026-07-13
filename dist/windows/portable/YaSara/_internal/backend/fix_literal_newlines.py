from pathlib import Path

ROOT = Path(r"D:\yasara_clean\backend")

fixed = 0

for file in ROOT.rglob("*.py"):
    try:
        text = file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    # فقط فایل‌هایی که newline واقعی ندارند ولی \n متنی دارند
    if "\\n" in text and "\n" not in text.replace("\\n", ""):
        repaired = (
            text
            .replace("\\r\\n", "\n")
            .replace("\\n", "\n")
            .replace("\\t", "\t")
        )

        file.write_text(repaired, encoding="utf-8", newline="\n")
        print("FIXED:", file)
        fixed += 1

print()
print(f"Done. Fixed {fixed} file(s).")