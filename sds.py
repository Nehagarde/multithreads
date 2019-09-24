import threading

final_dict=dict()
def process(chunk):
    words = line.split()
    for word in words:
        if word in final_dict.keys():
            final_dict[word] += 1
        else:
            final_dict[word] = 1

chunk size=100000000

if __name__ == '__main__':

    with open("test") as f:
        while True:
            t=f.seek()
            t1 = threading.Thread(target=process, args=(t,))

    print(final_dict)