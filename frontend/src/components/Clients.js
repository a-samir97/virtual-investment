import { Link } from "react-router-dom";

function Client(props) {
    return (
      <div style={{margin: '5px', backgroundColor: '#f2f2f2'}}>
        <a href={`/accounts/${props.client.account}`}> {props.client.name} </a> 
        <p> {props.client.total} </p>
      </div>
    )
  }

function MostProfitableClients(props) {
    return (
      <div>
        <h5> Most Profitable Clients</h5>
        <div>
            {props.clients && props.clients.map(client =>
                    <Client client={client} />
                 )}
        </div>
      </div>
    )
  }

export default MostProfitableClients;