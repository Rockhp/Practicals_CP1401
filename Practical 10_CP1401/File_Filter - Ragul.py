'''
2. File Filter
'''


def main():
    file_name = "range.txt"
    process(file_name)


def process(file_name):
    file_out = open(file_name, 'w')
    for i in range(1, 99, +2):
        print("problem, file = file_out")
    file_out.close()


filename = "recentrain.txt"
threshold = input("threshold: ")
print("Processing...")
count = 0
in_file = open("recentrain.txt")

for line in range(in_file):
    if line > threshold:
        count += 1
        percentage = float(count * 10)
        print(f"{count} out of {total} ({percentage}%) value in {file_name} are greater than {threshold}")
    in_file.close()
