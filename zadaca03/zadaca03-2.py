import asyncio
import numpy as np
import psutil


async def afunc1():
    np.random.normal(loc=0.0,scale=10,size=100000)
    await asyncio.sleep(0.09)
async def afunc2():
    print("Iskorištenost CPU u 10 sekundi iznosi:", psutil.cpu_percent(10))
     

async def main():
    await afunc1()
    final = await afunc2()
    print(final)

if __name__=="__main__":
    asyncio.run(main())
