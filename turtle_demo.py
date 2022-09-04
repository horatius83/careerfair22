# %%
from turtle import *

color('blue', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
# %%
from turtle import *
from typing import Tuple
import random

MAXIMUM_DISTANCE = 500
OFFSET = MAXIMUM_DISTANCE / 2

def get_random_distance() -> int:
    return random.randint(-OFFSET, OFFSET)

def get_random_point() -> Tuple[int, int]:
    return (get_random_distance(), get_random_distance())

def get_random_color() -> str:
    return [random.random() for _ in range(3)]

for _ in range(100):
    x, y = get_random_point()
    setposition(x,y)
    color(*get_random_color())
    dot(20)
done()
print('done')

# %%
import math
from typing import Tuple, List
import random
from turtle import penup, done, dot, setposition, color, speed

SCALING_FACTOR = 500.0
OFFSET_X = -250.0

def midpoint(p: Tuple[float, float], q: Tuple[float, float]) -> Tuple[float, float]:
    """Given points p and q return a point at the midpoint between them"""
    return (0.5 * (q[0] - p[0]), 0.5 * (q[1] - p[1]))

def translate_and_scale(a: Tuple[float, float]) -> Tuple[float, float]:
    """Translate a point by a globally defined offset and scaling factor"""
    x, y = [OFFSET_X + SCALING_FACTOR * b for b in a]
    return (x,y)

def get_color(x: float, y: float) -> List[float]:
    """Given a point on the screen generate a color"""
    def sine_wave_conversion(t: float) -> float:
        return 0.5 * (1.0 + math.sin(((2.0 * math.pi) / SCALING_FACTOR) * t))
    # 2 * pi = 250x, (2 * pi) / 250 = x
    #r = min(1.0, abs(x / 500.0))
    r = sine_wave_conversion(y)
    #g = min(1.0, abs(y / 500.0))
    g = sine_wave_conversion(y + (SCALING_FACTOR / 3.0))
    #b = min(1.0, abs((y + 128) / 500.0))
    b = sine_wave_conversion(y + (2.0 * SCALING_FACTOR / 3.0))
    return [r, g, b]

corners = [(0,0), (0.5, math.sqrt(3)/2), (1,0)]
scaled_corners = [translate_and_scale(c) for c in corners]

N_DOTS = 2_000

x,y = translate_and_scale((random.random() for _ in range(2)))

speed(10)
penup()
for i in range(N_DOTS):
    corner = random.sample(scaled_corners, 1)
    x,y = midpoint(corner[0], (x,y))
    setposition(x,y)
    color(get_color(x, y))
    dot(5)
    print(f'{i} of {N_DOTS}')
done()
print('Done!')

# %%
import math

SCALING_FACTOR = 500.0

def sine_wave_conversion(t: float) -> float:
    # y = mx + b
    # (0, 0), (500, 2 * pi)
    return 0.5 * (1.0 + math.sin(((2.0 * math.pi) / SCALING_FACTOR) * t))

[sine_wave_conversion(x - 250) for x in range(500)]
# %%
