## new order builder
class orderOut:
    def __init__(self, order_id, table_id, waiter_id, priority, items, max_wait, pick_up_time):
        self.order_id = order_id
        self.table_id = table_id
        self.waiter_id = waiter_id
        self.priority = priority
        self.items = items
        self.max_wait = max_wait
        self.pick_up_time = pick_up_time
