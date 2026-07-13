from collections import Counter

from yasara_doctor.scanner import ProjectScanner

scanner = ProjectScanner()

files = scanner.scan()

print("Python Files:", len
