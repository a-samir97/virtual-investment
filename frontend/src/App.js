import { useEffect, useState } from 'react';
import {useParams} from 'react-router-dom';
import './App.css';
import RecentStocks from './components/Stocks'
import MostProfitableClients from './components/Clients';
import AccountInfo from './components/AccountInfo';
import Navbar from './components/Navbar';
import TransactionsTable from './components/Transaction';
import getStocks from './api/getStocks';
import getAccountInfo from './api/getAccountInfo';
import CreateTransaction from './components/createTransaction';
import getMostProfitableClients from './api/getMostProfitableClients';
import getRecentStocks from './api/getRecentStocks';

function App() {
  const [stocks, setStocks] = useState(null)
  const [accountInfo, setAccountInfo] = useState(null)
  const [clients, setClients] = useState(null)
  const [recentStock, setRecentStock] = useState(null)

  const params = useParams();

  useEffect(() => {  
    getStocks() 
    .then(data => setStocks(data))
    .catch(error => console.log(error))
  }, []);

  useEffect(() => {  
    getAccountInfo(params['accountId'])
    .then(data => setAccountInfo(data))
    .catch(error => console.error(error))
  }, []);

  useEffect(() => {  
    getMostProfitableClients(params['accountId'])
    .then(data => setClients(data))
    .catch(error => console.error(error))
  }, []);

  useEffect(() => {  
    getRecentStocks() 
    .then(data => setRecentStock(data))
    .catch(error => console.log(error))
  }, []);

  return (
    <div className='App'>
      {accountInfo && < Navbar name={accountInfo.name}/>}
    <div style={{display: 'flex'}}>
      <div style={{width: '80%',}}>
        {accountInfo && <AccountInfo account={accountInfo}/>}
        <br></br>
        {accountInfo && <TransactionsTable transactions={accountInfo.transactions} />}
        <br></br>
        <hr></hr>
        <CreateTransaction stocks={stocks}/>
        </div>
          <div>
            { recentStock && <RecentStocks stocks={recentStock}/>}
            { clients && <MostProfitableClients clients={clients} />}
          </div>

        </div>
      </div>
  );
  }
export default App;
