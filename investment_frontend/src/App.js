import './App.css';
function GeneralInformatio() {
  return (
    <div>
        <h3> General Information</h3>
        <div style={{display: 'flex', flexDirection: 'row'}}>
          <div style={{width: '30%', backgroundColor: 'grey', marginRight: '3px'}}> 
            <h4> Current Balance </h4>
            <h4> 1200.00 </h4>
          </div>

          <div style={{width: '30%', backgroundColor: 'grey', marginRight: '3px'}}>
            <h4> Total Profit/Loss </h4>
            <h4> 1200.00 </h4>
          </div>

          <div style={{width: '30%', backgroundColor: 'grey'}}>  
            <h4> Total Portfolio Value </h4>
            <h4> 1200.00 </h4>
          </div>
      </div>
    </div>
  )
}
function Stock() {
  return (
    <div style={{display: 'flex', flexDirection: 'row', margin: '5px', backgroundColor: 'white'}}>
      <p> Apple </p>
      <p> $ 5.00 </p> 
    </div>
  )
}

function RecentStocks() {
  return (
    <div style={{backgroundColor: 'pink'}}>
      <h3> Recent Stocks </h3>      
    <div>
      <Stock />
      <Stock />
      <Stock />
      <br></br>
    </div>
    </div>
  )
}

function Client() {
  return (
    <div style={{display: 'flex', flexDirection: 'row', margin: '5px', backgroundColor: 'white'}}>
      <a> Client name </a>
      <p> $ 1200.00</p>
    </div>
  )
} 

function MostProfitableClients() {
  return (
    <div style={{backgroundColor: 'beige'}}>
      <h3> Most Profitable Clients</h3>
      <div>
        <Client />
        <Client />
        <Client />
      </div>
    </div>
  )
}
function Navbar() {
  return (
    <div style={{ width: '100%', backgroundColor: 'yellow', display: 'flex', justifyContent: 'space-between', margin: '5px'}}> 
      <h4 style={{padding: '5px'}}> Logo </h4>
      <h4 style={{padding: '5px'}}> Client name</h4>
    </div>
  )
}

function Transactions(){
  return (
    <div>
      <br></br>
      <hr></hr>
      <div style={{display: 'flex', justifyContent: 'space-between'}}>
      <h3>Transactions</h3>
      <button>Create a new transaction</button>
      </div>
      <div style={{display: 'flex', justifyContent: 'space-between'}}>
        <table className='table'>
          <thead>
          <th style={{width: '15%'}}> Stock </th>
          <th style={{width: '15%'}}> Volume </th>
          <th style={{width: '15%'}}> Purchase Price </th>
          <th style={{width: '15%'}}> Current Price </th>
          <th style={{width: '15%'}}> Gain/Loss </th>
          <th style={{width: '15%'}}> Purchase Time </th>
          </thead>
          <tbody>
            <tr> 
              <td> Test </td>
              <td> Test </td>
              <td> Test </td>
              <td> Test </td>
              <td> Test </td>
              <td> Test </td>
            </tr>
          </tbody>
        </table>
      </div>
      </div>
  )
}
function App() {
  return (
    <div className='App'>
      <Navbar />
    <div style={{display: 'flex'}}>
      <div style={{width: '80%',}}>
        <GeneralInformatio />
        <Transactions />
      </div>

    <div>
      <RecentStocks />
      <MostProfitableClients />
    </div>

    </div>
    </div>
  );
}

export default App;
