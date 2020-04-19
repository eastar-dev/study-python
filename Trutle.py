import turtle

t = turtle.Pen()
t.shape("turtle")
t.speed(1)

rabbit = 50
carrot = 0

if rabbit:
    t.forward(100)
if carrot:
    t.forward(100)

t.backward(100)

for i in range(3, 10, 2):
    print(i)
