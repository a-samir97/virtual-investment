function Stock(props) {
    return (
      <div style={{display: 'flex', flexDirection: 'row', margin: '5px', backgroundColor: '#f2f2f2', justifyContent: 'space-around'}}>
        <p> {props.stock.name} </p>
        <p> {props.stock.price} </p>
      </div>
    )
  }

function RecentStocks(props) {
  
    return (
      <div>
        <h3> Recent Stocks </h3>      
      <div>
        { props.stocks && props.stocks.map(stock =>
        <Stock
          stock={stock}
          />
          )}
        <br></br>
      </div>
      </div>
    )
  }

export default RecentStocks;
