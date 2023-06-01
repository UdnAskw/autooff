import asyncio
from dataclasses import dataclass
import RPi.GPIO as GPIO


@dataclass
class Sensor():
    GPIO_PIN: int = 18
    INTERVAL: int = 3

    def __post_init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PIN, GPIO.IN)

    async def sensor(self, input_type: int):
        '''
        input_type
            0: GPIO.LOW
            1: GPIO.HIGH
        '''
        while True:
            if GPIO.input(self.GPIO_PIN) == input_type:
                yield True
                await asyncio.sleep(self.INTERVAL)


async def test():
    snsr = Sensor().sensor(1)
    while True:
        d = await snsr.__anext__()
        print(d)


if __name__ == "__main__":
    asyncio.get_event_loop()
    asyncio.run(test())