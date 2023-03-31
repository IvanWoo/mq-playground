from proj.tasks import slow_add

for i in range(10):
    slow_add.delay(i, i)

