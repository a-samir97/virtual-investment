const getAccountInfo = async (accountId) => {
    const response = await fetch(`http://localhost:8000/api/accounts/${accountId}/`);
    const data = await response.json();
    return data
}

export default getAccountInfo;