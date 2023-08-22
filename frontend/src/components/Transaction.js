function TransactionsTable(props){
    return (
      <div style={{backgroundColor: '#f2f2f2'}}>
        <br></br>
        <div>
        <h3 style={{justifyContent: 'center'}}>Transactions</h3>
        </div>
        <div style={{justifyContent: 'space-between'}}>
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

                {props.transactions.map(transaction => (
                  <tr>
                    <td> {transaction.name} </td>
                    <td> {transaction.quantity} </td>
                    <td> {transaction.purchase_price} </td>
                    <td> {transaction.current_price} </td>
                    <td> {transaction.gain_loss} </td>
                    <td> {transaction.created_at} </td>
                </tr>
                ))} 

            </tbody>
          </table>
        </div>
        </div>
    )
  }

export default TransactionsTable;