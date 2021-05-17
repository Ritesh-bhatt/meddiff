# Input dictionary.
files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
# Function to group the files.
def group_by_owners(files):
    result = {}

    for key, value in files.items():

        if value not in result.keys():
            result[value] = [key]
        else:
            result[value].append(key)

    return result
print(group_by_owners(files))
