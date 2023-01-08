select consumer.consumer_name,sales_manager.city,
orders.order_number,orders.order_date,orders.purchase_amount,
sales_manager.sales_manager_name from consumer inner join
orders on consumer.consumer_id=orders.consumer_id
inner join sales_manager on 
orders.sales_manager_id=sales_manager.sales_manager_id
where purchase_amount<500 order by orders.consumer_id asc;

