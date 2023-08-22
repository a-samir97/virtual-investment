const getStocks = async () =>{
    const response = await fetch('http://localhost:8000/api/stocks/');
    const data = await response.json();
    return data
}

export default getStocks;