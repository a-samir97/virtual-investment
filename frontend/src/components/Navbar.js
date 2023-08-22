function Navbar(props) {
    return (
      <div style={{ width: '100%', backgroundColor: '#f2f2f2', display: 'flex', justifyContent: 'space-between', margin: '5px'}}> 
        <a href="/" style={{fontFamily: 'serif', fontWeight: 'bold', margin: '10px'}}> Adcash Task </a>
        <p style={{fontFamily: 'serif', fontWeight: 'bold', margin: '10px'}}> {props.name} </p>
      </div>
    )
  }
export default Navbar;
