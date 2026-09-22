from pathlib import Path
import py_compile
import sys

root = Path(__file__).resolve().parents[1]
py_files = sorted((root / 'src').glob('*.py'))
failed = []
for p in py_files:
    try:
        py_compile.compile(str(p), doraise=True)
        print(f'OK   {p.relative_to(root)}')
    except Exception as e:
        failed.append((p, e))
        print(f'FAIL {p.relative_to(root)}: {e}')

print(f'\nCompiled {len(py_files)-len(failed)}/{len(py_files)} scripts.')
if failed:
    sys.exit(1)
