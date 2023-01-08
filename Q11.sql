select consumer.consumer_name,sales_manager.city,orders.order_number,
orders.order_date,orders.purchase_amount from consumer inner join
 orders on consumer.consumer_id=orders.consumer_id inner join 
sales_manager on 
orders.sales_manager_id=sales_manager.sales_manager_id 
order by orders.order_date;