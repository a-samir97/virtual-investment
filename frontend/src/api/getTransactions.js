const getTransactions = async (accountId) =>{
    const response = await fetch(`http://localhost:8000/api/transactions/${accountId}`);
    const data = await response.json();
    return data
}

export default getTransactions;