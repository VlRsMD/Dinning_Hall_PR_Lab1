from datetime import datetime
import random
import time
import threading
import requests
import json
import menu
import order_out
from wsgiref.simple_server import make_server

def DH_App(environment, response):
    status = '200 OK'
    headers = [('content-type', 'text/html; charset=utf-8')]
    response(status, headers)
    return [b'<h2>Dinning hall server</h2>']


with make_server('', 3500, DH_App) as server:
    print('serving on port 3500...\nvisit http://127.0.0.1:3500\nTo exit press ctrl + c')
    server.serve_forever()
    
st = []

@DH_App.put("/put")

def order_stack():
    global st
    ## generating total of 40 orders
    for k in range(4):
        ## 10 tables generating orders
        for i in range(10):
            order_id = random.randrange(1, 11, 0)
            table_id = i
            waiter_id = random.randrange(1, 5, 0)
            priority = random.randrange(1, 6, 0)
            items = [random.randrange(1, 11, 0), random.randrange(1, 11, 0), random.randrange(1, 11, 0)]
            ## calculating maximum waiting time (5 next lines)
            max = menu.menu[items[0]].prep_time
            for i in range(1, 3):
                if menu.menu[items[i]].prep_time > max:
                    max = menu.menu[items[i]].prep_time
            max_wait = max * 1.3
            pick_up_time = datetime.timestamp(datetime.now())
            new_order = order_out.orderOut(order_id, table_id, waiter_id, priority, items, max_wait, pick_up_time)
            ## adding new order to the stack
            st.append(new_order)
        ## sleep for a while so that a table with same id does not generate orders with no pause
        time.sleep(1)

## send orders to kitchen
def send_order():
    global st
    mutex = threading.Lock()
    ## do while stack is not empty
    while len(st) > 0:
        ## lock
        mutex.acquire()
        pick_up_order = st.pop()
        order_to_json = json.dumps(pick_up_order.__dict__)
        requests.put("http://127.0.0.1:3501/put", json=order_to_json)
        ## unlock
        mutex.release()
    ## notify kitchen that no more orders are coming
    if len(st) == 0:
        requests.put("http://127.0.0.1:3501/put", json={"state": "no more incoming orders"})

## multiple waiters threads
waiters = [threading.Thread(target=send_order) for i in range(4)]

if __name__ == '__main__':
    ## starting waiters multithreading
    for waiter in waiters:
        waiter.start()
    ## starting dinning hall server
    DH_App.run(host='127.0.0.1', port=3500)
