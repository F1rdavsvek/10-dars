# from multiprocessing import Process
# import time
#
# def generate_number(num):
#     for i in range(1, num + 1):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     process = []
#
#     for i in range(10):
#         pr = Process(target=generate_number, args= (5,))
#         pr.start()
#         process.append(pr)
#
#
#     for pr in process:
#         pr.join()

# -----------------------------------------------------------------------

# from multiprocessing import Process, Queue
# import time
#
# def generate_number(num, q:  Queue):
#     l = []
#     for i in range(1, num + 1):
#         print(i)
#         l.append(i)
#         time.sleep(1)
#     q.put(l)
#
# if __name__ == "__main__":
#     q = Queue()
#     q1 = Queue()
#     pr = Process(target=generate_number, args= (5, q))
#     pr1 = Process(target=generate_number, args= (5, q1))
#     pr.start()
#     pr1.start()
#     pr.join()
#     pr1.join()
#     print(q.get())
#     print(q1.get())