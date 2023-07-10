#!/usr/bin/python3
import asyncio

def file_name():
    file_ = "{}".format(__file__)
    file_ = file_.split('/')
    for element in file_:
        print(element)
    print(type(file_))
    file_name =  file_[-1]
    return file_name


async def greet():
    print("Ogundare, this is the File Name \"{}\"".format(file_name()))
    await asyncio.sleep(3)
    print("Olamide, this is the File Name {}".format(file_name()))
    # await asyncio.sleep(3)
    # print("Emmananuel")


async def main():
    await asyncio.gather(
        greet(),
        greet(),
        greet()
    )


if __name__ == "__main__":
    asyncio .run(main())
    # main()
    # print(f"{__file__.split('/')[-1]}")
    file_name()
