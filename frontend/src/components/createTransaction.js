import {useState} from 'react';
import { useParams } from 'react-router-dom';
function CreateTransaction(props) {
    const [stock, setStock] = useState()
    const [quantity, setQuantity] = useState()
    const params = useParams()

    function handleChangeStock(e) {
        setStock(e.target.value)
    }
    function handleChangeQuantity(e) {
        setQuantity(e.target.value)
    }

    function handleSubmit(e){
        e.preventDefault();
        fetch('http://localhost:8000/api/transactions/', {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({
                "stock": stock,
                "quantity": quantity,
                "account": params['accountId']
            })
        }).then(resp => {
                resp.json().then(data => {
                    if (resp.status !== 201){
                        alert(data['error'])
                    } else {
                        alert("Transaction created successfully")
                    }

                })
        })
        .catch(error => {
            alert('Please try again later')
        })
    }

    return (
        <div>
        <form onSubmit={handleSubmit}>

            <label for="stock">Stock</label>
            <select name="stock" onChange={handleChangeStock}>
            {props.stocks && props.stocks.map(stock =>(
                <option value={stock.id}>{stock.name} | {stock.price}$ | {stock.quantity} shares</option>
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