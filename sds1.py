import threading
from multiprocessing import Pool, Manager


manager = Manager()

final_dict=manager.dict()
def process(chunk):
    words = chunk.split()
    for word in words:
        if word in final_dict.keys():
            final_dict[word] += 1
        else:
            final_dict[word] = 1

chunksize=10000000

if __name__ == '__main__':

    with open("test","r") as f:
        while True:
            t = f.read(chunksize)
            t1 = threading.Thread(target=process, args=(t,))
            t1.start()

    print(final_dict)