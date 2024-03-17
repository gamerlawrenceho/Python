import turtle as t

t.color('red')
t.penup()
t.tracer(0, 0)
t.stamp()
for a in range(8):
    t.home()
    t.right(a * 45)
    t.forward(80)
    t.stamp()

t.done()