
OUTPUT_FILE = "output.txt"
DB_FILE = "localdb.txt"
class DbRepo():
    def __init__(self):
        pass

    def convert_output_to_db():
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as r:
            with open(DB_FILE, 'w', encoding='utf-8') as w:
                w.truncate(0)  # Clear the file
                for line in r.readlines():
                    name, image_link = line.strip().split(': ')
                    if(',' in name):
                        name = name[:name.index(',')]
                    if('ז"ל' not in name):
                        w.write(name + ': ' + image_link + ': ' + 'False\n')

    def get_people():
        people = []
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                name = line.split(': ')[0]
                image_link = line.split(': ')[1]
                lettered = bool(line.split(': ')[2])

                people.append({'name': name, 'image_link': image_link, 'lettered': lettered})
        return people
    
    def get_lettered_people():
        people = []
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                name = line.split(': ')[0]
                image_link = line.split(': ')[1]
                lettered = "True" in (line.split(': ')[2])

                if lettered:
                    people.append({'name': name, 'image_link': image_link, 'lettered': lettered})
        return people
    
    def get_unlettered_people():
        people = []
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                name = line.split(': ')[0]
                image_link = line.split(': ')[1]
                lettered = "True" in (line.split(': ')[2])

                if not lettered:
                    people.append({'name': name, 'image_link': image_link, 'lettered': lettered})
                    print(name)
        return people

    def get_image_link(name):
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                if(name in line):
                    return line.split(': ')[1].strip()
        return None

    def is_lettered(name):
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                if(name in line):
                    return "True" in (line.split(': ')[2].strip())
        return False
        
    def letter(name, letter: str):
        if(DbRepo.is_lettered(name)):
            return
        with open(DB_FILE, 'r+', encoding='utf-8') as r:
            lines = r.readlines()
            r.seek(0)  # Move the file pointer to the beginning of the file
            r.truncate()  # This truncates the file to remove its previous content

            for i in range(len(lines)):
                if name in lines[i]:
                    parts = lines[i].split(': ')
                    lines[i] = f"{parts[0]}: {parts[1]}: True: {letter}\n"

            r.writelines(lines)

    def get_letter(name):
        with open(DB_FILE, 'r', encoding='utf-8') as r:
            for line in r.readlines():
                if(name in line):
                    return line.split(': ')[3].strip()
        return None


if __name__ == '__main__':
    ans = input("Are you sure you want to convert the output file to the database file? (y/n) ")
    if(ans == 'y'):
        DbRepo.convert_output_to_db()
        print("Done!")
    else:
        print("Aborted")