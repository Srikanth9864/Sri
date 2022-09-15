# f = open("/Users/sandeep/Desktop/Training/_python/data_files/sample_file.txt")
# f.close()
# read()
# contents = f.read()
# readlines()
# lines = f.readlines()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

# most memory efficient way of reading files in python
# for index, line in enumerate(f):
#     print(index, line)

# lines = f.readlines()
# for line in lines[::-1]:
#     print(line)

# most standard way of reading files
# with open('./data_files/access_log.txt', 'r') as f:
#     ip_address = [ ]
#     for line in f:
#         line = line.strip()
#         parts = line.split()
#         ip_address.append(parts[0])

# count = { }
# for item in ip_address:
#     if item in count:
#         count[item] += 1
#     else:
#         count[item] = 1

# sort the dictionary based on values
# by_count = sorted(count.items(), key=lambda item: item[-1])
# most_visited_ip = by_count[-3:]
# least_visited_ip = by_count[:3]

# unique_ip = [ ]
# for item in ip_address:
#     if item not in unique_ip:
#         unique_ip.append(item)

# with open("./unique_ip.txt", 'w') as fw:
#     for item in unique_ip:
#         fw.write(item)
#         fw.write("\n")

# d = {"66.249.65.38": 10, "66.249.65.38": 2}

# {"INFO": 100, "TRACE": 30, "WARNING": 26}
# with open("./data_files/sample.log", "r") as log:
#     messages = [ ]
#     for line in log:
#         line = line.strip()
#         if line:
#             parts = line.split()
#             messages.append(parts[2])

# message_count = { }
# for message in messages:
#     if message in message_count:
#         message_count[message] += 1
#     else:
#         message_count[message] = 1


def count():
    with open("./data_files/sample_file.txt", "r") as f:
        word_count = { }
        for line in f:
            line = line.strip()
            # if the string has atleast one character or if i have got a valid line
            if line:
                words = line.split()
                for word in words:
                    if word in word_count:
                        word_count[word] = word_count[word] + 1
                    else:
                        word_count[word] = 1
    return word_count

def word_count():
    """ Returns the total number of words present in the file"""
    _word_count = 0
    with open("./data_files/sample_file.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                words = line.split()
                _word_count = _word_count + len(words)
    return _word_count


# with open("./data_files/sample_file.txt") as f:
#     for index, line in enumerate(f, start=1):
#         if "python" in line:
#             print(f"{index} : {line}")

# with open("spam_.txt", "x") as f:
#     f.write("hello there")
#     f.write("\n")

# with open("./data_files/java.txt", "r") as f_java, open("./data_files/python.txt", "r") as f_py:
#     for java_line, py_line in zip(f_java, f_py):
#         print(java_line, py_line)

# with open("./data_files/sample.log", "r") as fr, open("info.txt", "w") as fw:
#     for line in fr:
#         if "WARNING" in line:
#             fw.write(line)

with open("./data_files/sample.log", "r") as fr:
    with open("info.txt", "w") as fw:
        for line in fr:
            if "INFO" in line:
                fw.write(line)