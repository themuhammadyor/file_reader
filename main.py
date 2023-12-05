import csv
import os


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def __iter__(self):
        self.file = open(file=self.file_path)
        return self
    def __next__(self):
        line  = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

if __name__ == '__main__':
    this_list = []
    for i in range(1, 11):
        t = '00' + str(i)
        if i >= 10:
            t = '0' + str(i)
        for line in FileReader(f"descriptions/{t}.txt"):
            # print(line)
            this_list.append(line)
            with open(f"{t}.csv", "w") as f:
                writer = csv.writer(f)
                first_row = ["name", "price", "descriptions"]
                writer.writerow(first_row)
                writer.writerow(this_list)