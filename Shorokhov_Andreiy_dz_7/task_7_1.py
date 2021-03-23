import os


def project_starter(parent_dir, *dirs):
    for path in dirs:
        try:
            os.makedirs(os.path.join(parent_dir, path))
        except FileExistsError as e:
            print(f'Локальная ошибка: {e}')
        except Exception as e:
            print(f'Глобальная ошибка: {e}')
    return 0


def create_starter(name):
    project_starter(name, 'settings', 'mainapp', 'adminapp', 'authapp')
    return 0


if __name__ == '__main__':
    create_starter('my_project')
