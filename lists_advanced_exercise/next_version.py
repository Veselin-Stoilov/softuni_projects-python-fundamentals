def update_version(current_version: list):
    current_version_string = ''.join(current_version)
    new_version = int(current_version_string) + 1
    new_version_list = list(str(new_version))
    new_version = '.'.join(new_version_list)
    return new_version


old_version = input().split('.')
print(update_version(old_version))
