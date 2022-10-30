import asyncio
import os


async def afun1(x):
    assert isinstance(x,list)
    await asyncio.sleep(0.02)
    return[{"naziv:":n, "velicina":v} for v,n in os.stat(x).st_size]

def fun2():
    pass
    

async def main():
   dir_path = 'D:\distsys\Zadatak1'
   
   file="datoteka1"
   file_path=os.path.join(dir_path,file)
   with open(file_path, 'w') as f:
     pass

   file="datoteka2"
   file_path=os.path.join(dir_path,file)
   with open(file_path, 'w') as f:
     pass

   file="datoteka3"
   file_path=os.path.join(dir_path,file)
   with open(file_path, 'w') as f:
     pass

   dir_list=os.listdir(dir_path)
   lista=[]
   for item in dir_list:
     lista.append(item)
   print("Lista direktorija:")

   final = await afun1(lista)
   print(final)
   
if __name__=="__main__":
    asyncio.run(main())