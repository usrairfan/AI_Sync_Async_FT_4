# Synchoronous
#import time

# Step # 1
#print("Cooking start....")
#time.sleep(5)
#print("Cooking done...")

# Step # 2
#print("Washing Cloth start... ")
#time.sleep(6)
#print("Washing Cloth done....")


# Asynchronous
import asyncio
# Step # 1 
async def javascript_perho():
    print("Class start....")
    await asyncio.sleep(5)
    print("Class end...")

# Step # 2
async def typescript_perho():
    print("Class start....")
    await asyncio.sleep(3)
    print("Class end...")

# Step # 3    
async def main():
    await asyncio.gather(
        javascript_perho(),
        typescript_perho()
    )

asyncio.run(main())    