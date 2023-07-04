import sys
def countLeftWhiteSpaces(line):
    count = 0
    for character in line:
        if character.isspace():
            count += 1
        else:
            break
    
    return count


def readLine(file, jsonResult = {}, parentTag = ''):
    line = file.readline()

    if not line:
        return jsonResult
    
    if line.startswith('#'):
        return readLine(file, jsonResult)
    
    if line.startswith('---'):
        return readLine(file, jsonResult)
    
    data = line.split(':')

    if len(data) == 1 and parentTag.strip():
        return data[0].strip()

    if len(data) == 2 and data[1].strip():
        key = data[0].strip()
        value = data[1].strip()
        jsonResult[key] = value
    
    if len(data) == 2 and not data[1].strip():
        jsonResult[data[0].strip()] = readLine(file, jsonResult, data[0].strip())

    return readLine(file, jsonResult)

if __name__ == '__main__':
    n = len(sys.argv)
    print(sys.argv)
    if n != 2:
        print("You must pass a valid path for the document")
        quit()

    print("\nPocessing file:", sys.argv[1])

    filename = sys.argv[1]
    if filename[:-4:-1] != 'lmy' and filename[:-5:-1 != 'lmay']:
        print("Not a valid format for the document")
        quit()

    file = open(filename, "r")

    jsonResult = readLine(file)

    print(jsonResult)
    file.close()