function AccountInfo(props) { 
    return (
      <div>
          <h3> General Information</h3>
          <div style={{display: 'flex', flexDirection: 'row'}}>
            <div style={{width: '30%', marginRight: '3px', backgroundColor: '#f2f2f2'}}> 
              <h4> Current Balance </h4>
              <h4> {props.account.balance} </h4>
            </div>
  
            <div style={{width: '30%', marginRight: '3px', backgroundColor: '#f2f2f2'}}>
              <h4> Total Profit/Loss </h4>
              <h4> {props.account.total_profit_loss} </h4>
            </div>
  
            <div style={{width: '30%', backgroundColor: '#f2f2f2'}}>  
              <h4> Total Portfolio Value </h4>
              <h4> {props.account.total_portfolio_value} </h4>
            </div>
        </div>
      </div>
    )
  }

export default AccountInfo;