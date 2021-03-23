import os
from shutil import copytree

SETTINGS_FILES = 'dev.py', 'prod.py'
APP_FILES = 'models.py', 'views.py'
TEMPLATE_FILES = 'base.html', 'index.html'
APP_DIRS = 'templates', ''
COMMON_FILES = '__init__.py', ''


def create_files(file):
    try:
        with open(file, 'x', encoding='utf-8') as f:
            f.write('')
    except FileExistsError as e:
        print(f'Локальная ошибка: {e}')
    except Exception as e:
        print(f'Глобальная ошибка: {e}')


def project_starter(parent_dir, *dirs):
    for path in dirs:
        os.makedirs(os.path.join(parent_dir, path), exist_ok=True)
        for file in COMMON_FILES:
            create_files(os.path.join(parent_dir, path, file))
        if path == 'settings':
            for file in SETTINGS_FILES:
                create_files(os.path.join(parent_dir, path, file))
        if path == 'mainapp' or path == 'authapp':
            for file in APP_FILES:
                create_files(os.path.join(parent_dir, path, file))
            for app_dir in APP_DIRS:
                os.makedirs(os.path.join(parent_dir, path, app_dir),
                            exist_ok=True)
                if app_dir == 'templates':
                    os.makedirs(os.path.join(parent_dir, path, app_dir, path),
                                exist_ok=True)
                    for file in TEMPLATE_FILES:
                        create_files(os.path.join(parent_dir, path, app_dir,
                                                  path, file))
    return 0


def copy_templates(parent_dir):
    templates_copies = os.path.join(parent_dir, 'templates')
    os.makedirs(templates_copies, exist_ok=True)

    for root, dirs, files in os.walk(parent_dir):
        if os.path.split(root)[-1] == 'templates' \
                and os.path.split(root)[0] != parent_dir:
            for item in dirs:
                try:
                    copytree(os.path.join(root, item),
                             os.path.join(templates_copies, item))
                except FileExistsError as e:
                    print(f'Локальная ошибка: {e}')
                except Exception as e:
                    print(f'Глобальная ошибка: {e}')


def create_starter(name):
    project_starter(name, 'settings', 'mainapp', 'authapp')
    copy_templates(name)
    return 0


if __name__ == '__main__':
    create_starter('my_project')
