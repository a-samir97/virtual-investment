const getRecentStocks = async () => {
    const response = await fetch('http://localhost:8000/api/stocks/recent/');
    const data = await response.json();
    return data
}

export default getRecentStocks;