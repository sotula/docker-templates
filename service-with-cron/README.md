### Example of service with cron 

Sometimes we need to do smth regurarly. For example we need do query to db each 10 minutes and then process data with our service. 
We can run service for processing data and run cron which will do query and send data to service in the same container.
