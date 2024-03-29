import threading

final_dict=dict()
def process(chunk):
    words = chunk.split()
    for word in words:
        if word in final_dict.keys():
            final_dict[word] += 1
        else:
            final_dict[word] = 1

chunksize=10000

if __name__ == '__main__':

    pool = Pool(5)
    jobs = []
    with open("test","r") as f:
        while True:
            t = f.read(chunksize)
            t1 = threading.Thread(target=process, args=(t,))
            t1.start()
            jobs.append(t1)

    print(final_dict)