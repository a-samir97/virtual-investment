const getMostProfitableClients = async () =>{
    const response = await fetch('http://127.0.0.1:8000/api/accounts/most_profitable/');
    const data = await response.json();
    return data
}

export default getMostProfitableClients;