from proj.tasks import slow_add, add

for i in range(4):
    add.delay(i, i)
    slow_add.delay(i, i)
