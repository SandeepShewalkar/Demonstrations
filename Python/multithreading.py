import time
import threading
import asyncio

def calculateCube(numbers):
    for n in numbers:
        time.sleep(1)
        print("Cube of : ",n," is : ",n * n * n)

def calculateSquare(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square of : ",n," is : ",n*n)

def main():
# print("Execution Started.....")
# calculateSquare([5,10,15])
# calculateCube([5,10,15])
# print("Execution Ended.....")
    print("Execution Started.....")
    t1 = threading.Thread(target = calculateSquare, args = ([5,10,15],))
    t2 = threading.Thread(target = calculateCube, args = ([5,10,15],))
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print("Execution Ended.....")

main()

# async def main1():
#     print("Execution Started.....")
#     t1 = loop.create_task(calculateSquare[5,10,15])
#     t2 = loop.create_task(calculateCube([5,10,15]))
#     await asyncio.wait([t1,t2])
#     print("Execution Ended.....")

# if __name__ == '__main__':
    # try:        
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(main())
    # except Exception as e:
    #     print("exception")
    #     print(e)
    #     pass
    # finally:
    #     loop.close()
# asyncMain()
