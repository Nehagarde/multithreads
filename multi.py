import threading
import datetime,time
import re
import csv
import multiprocessing


t1 = time.time()
final_dict = dict()
def read_lines_in_chunk(chunk):
    words = chunk.split()
    for word in words:
        if word in final_dict.keys():
            final_dict[word] += 1
        else:
            final_dict[word] = 1


count=0
def start_process():
    chunk_size = 500000

    with open(r'C:\Users\neha_garde\Downloads\test.txt') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            else:
                print("Started th")
                t1=threading.Thread(target=read_lines_in_chunk, args=(data,))
                t1.start()


if __name__ == '__main__':
    print("here")
    start_process()
    print(final_dict)
    with open('testcsv1.csv', 'w') as f:
        for key in final_dict.keys():
            f.write("%s,%s\n" % (key, final_dict[key]))
    t2=time.time()

    print(t2-t1)