const getCustomers = async () => {
    const response = await fetch('http://localhost:8000/api/customers/');
    const data = await response.json();
    return data
}

export default getCustomers;