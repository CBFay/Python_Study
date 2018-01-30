# Experimentation with asynchronous code
# Created 1.30.2018 by CB Fay

import asyncio

async def main():
    
    routines = [
        largest_prime(10000),
        largest_prime(1000),
        largest_prime(100)
    ]
    
    await asyncio.wait(routines)
    
def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True

async def largest_prime(n):
    for i in reversed(range(2, n)):
        if is_prime(i):
            print(i)
            return i
        await asyncio.sleep(.01)
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
