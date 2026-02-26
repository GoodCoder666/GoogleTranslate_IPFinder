import subprocess
from pathlib import Path

def build():
    # Directories
    resources_ui_dir = Path('resources/ui')
    src_generated_dir = Path('src/ui/generated')

    src_generated_dir.mkdir(parents=True, exist_ok=True)

    # 1. Compile .ui files
    for ui_file in resources_ui_dir.glob('*.ui'):
        py_file = src_generated_dir / f'ui_{ui_file.stem}.py'
        print(f'Compiling {ui_file} -> {py_file}')
        subprocess.run(['pyside6-uic', str(ui_file), '-o', str(py_file)], check=True)

        # Patch res_rc import
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()

        patched = content.replace('import res_rc', 'from . import res_rc')
        if patched != content:
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(patched)
            print(f'  Fixed res_rc import in {py_file.name}')

    # 2. Compile translations
    ts_file = Path('resources/translations/en_US.ts')
    qm_file = Path('resources/translations/en_US.qm')
    py_files = [str(p) for p in Path('src').rglob('*.py') if 'generated' not in p.parts]

    print(f'Updating translations -> {ts_file}')
    lupdate_args = ['pyside6-lupdate', 'resources/ui'] + py_files + ['-ts', str(ts_file)]
    subprocess.run(lupdate_args, check=True)

    print(f'Releasing translations -> {qm_file}')
    subprocess.run(['pyside6-lrelease', str(ts_file), '-qm', str(qm_file)], check=True)

    # 3. Compile resources
    qrc_file = Path('resources/res.qrc')
    rc_py_file = src_generated_dir / 'res_rc.py'
    if qrc_file.exists():
        print(f'Compiling {qrc_file} -> {rc_py_file}')
        subprocess.run(['pyside6-rcc', str(qrc_file), '-o', str(rc_py_file)], check=True)

if __name__ == '__main__':
    build()
    print('Build complete.')
