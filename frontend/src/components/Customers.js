import { useEffect, useState } from 'react';
import {Link} from 'react-router-dom'
import getCustomers from '../api/getCustomers';
import '../App.css';

function Customer() {
  const [customers, setCustomers] = useState(null)

  useEffect(() => {  
    getCustomers() 
    .then(data => setCustomers(data))
    .catch(error => console.log(error))
  }, []);



  return (
    <div>
        <ul>
            { customers && customers.map(customer => 
                <li>
                    <Link to={`accounts/${customer.id}`} >
                         {customer.name}  
                     </Link>
                </li>
            )}
        </ul>
    </div>
  );
}

export default Customer;
