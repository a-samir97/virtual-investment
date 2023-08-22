import {useState} from 'react';
import { useParams } from 'react-router-dom';
function CreateTransaction(props) {
    const [stock, setStock] = useState()
    const [quantity, setQuantity] = useState()
    const params = useParams()

    function handleChangeStock(e) {
        setStock(e.target.value)
        console.log(params)
        console.log(stock)
    }
    function handleChangeQuantity(e) {
        setQuantity(e.target.value)
        console.log(quantity)
    }

    function handleSubmit(e){
        e.preventDefault();
        fetch('http://localhost:8000/api/transactions/', {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
                "stock": stock,
                "quantity": quantity,
                "account": params['accountId'],
                "purchase_price": 50,
            })
        }).then(alert('transaction is successfully created.'))
        .catch(error => {
            console.log(error)
            alert('Please try again later')
        })
    }

    return (
        <div>
        <form onSubmit={handleSubmit}>

            <label for="stock">Stock</label>
            <select name="stock" onChange={handleChangeStock}>
            {props.stocks && props.stocks.map(stock =>(
                <option value={stock.id}>{stock.name} | {stock.price} $</option>
            ))}
            </select>

            <label for="lname">Quantity</label>
            <input type="text" id="quantity" name="quantity" placeholder="Quantity of the stock ..." onChange={handleChangeQuantity}/>
        
            <input type="submit" value="Submit" />
        </form>
        </div>
    )    
}

export default CreateTransaction;