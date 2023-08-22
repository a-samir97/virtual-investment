# Virtual Investment Portfolio Management Task
<ul>
    <li><a href="#disclaimer">Disclaimer</a></li>
    <li><a href="#description">Description</a></li>
    <li><a href="#database_schema">Database_Schema</a></li>
    <li><a href="#backend_endpoints">Backend_Endpoints</a></li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#run-command">Run Command</a></li>
    <li><a href="#create-super-user">Create Super User</a></li>
    <li><a href="#improvements">improvements</a></li>
</ul>

## Disclaimer
I don't have experience in frontend development in general and everything done in this task/repo is the result of alot of self-study and experimenting done over my time (besides working hours).

Please take that into consideration.

## Description 
Each client should have some balance in their virtual investment portfolios. Gain
and loss of clients should be calculated based on the difference between purchase
and current prices of stocks. Each purchase should be deducted from the client’s
balance. There is no need to store unit price change logs for any stock.

## Database_Schema
![alt text](https://github.com/a-samir97/virtual-investment/blob/main/docs/database_schema.png)

## Backend_Endpoints 
- Customer API Endpoints
![alt text](https://github.com/a-samir97/virtual-investment/blob/main/docs/customers_endpoints.png)
- Stocks API Endpoints
![alt text](https://github.com/a-samir97/virtual-investment/blob/main/docs/stocks_endpoints.png)
- Transactions API Endpoints
![alt text](https://github.com/a-samir97/virtual-investment/blob/main/docs/transactions_endpoints.png)
- Accounts API Endpoints
![alt text](https://github.com/a-samir97/virtual-investment/blob/main/docs/accounts_endpoints.png)

## Challenges
- One of the most challenges in this task is frontend development, frontend development takes about 90% of the time.
- Race condition, which can happens in two casees
   - first case: many customers can buy the same stock (which can make a `race condition`)
   - second case: same customer can buy different stocks in the same balance (we need to `lock balance` in every create transaction)

## Run Command
- in this step you need just one command to run the project
- `docker-compose up`

## Run unit test (backend side)
- go to inside terminal of backend instance in docker `docker exec -it container_id`
- run `python manage.py test`
 
## Create Super User
- inside backend terminal instance `docker exec -it container_id`
- put this command to create super user which helps you to login in django admin
- `python manage.py createsuperuser`
- put `username, email, password`
- finally, you can go to login in django admin and see our data `http://localhost:8000/admin` 


## Improvements
- Improve UI
- Handle more errors in frontend side
- Use service layer in backend development to separate business from models
- Added unittests in frontend side
