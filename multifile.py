from multiprocessing import Pool, Manager
import re

manager = Manager()

final_dict=manager.dict()
def process(line,final_dict):
    words = line.split()
    for word in words:
        if word in final_dict.keys():
            final_dict[word] += 1
        else:
            final_dict[word] = 1

if __name__ == '__main__':
    #init objects
    pool = Pool(5)
    jobs = []
    #create jobs
    with open("test") as f:
        for line in f:
            jobs.append(pool.apply(process,(line,final_dict,)) )
    #clean up
    pool.close()
    print(final_dict)