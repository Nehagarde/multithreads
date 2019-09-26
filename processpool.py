import multiprocessing as mp
import time
from collections import Counter
chunk_size = 10000000


def read_lines_in_chunk(chunk,final_dict):
    words = chunk.split()
    result = Counter(words)
    for i in result.keys():
        if i in final_dict.keys():
            final_dict[i] += result[i]
        else:
            final_dict[i] = result[i]

def start_processing():
    m =mp.Manager()
    final_dict = m.dict()

    pool = mp.Pool(mp.cpu_count())
    with open(r'C:\Users\neha_garde\Downloads\test.txt') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            else:
                print("Started th")
                pool.apply_async(read_lines_in_chunk, args=(data,final_dict, ))

    pool.close()
    pool.join()
    print(final_dict)
    

if __name__ == '__main__':
    start=time.time()
    start_processing()
    end=time.time()
    print(end-start)