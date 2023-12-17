//Llista
import React, { useState } from 'react';
import ListGrup from "./Componets/ListGruoe";
function App() {
  let items = ['Posar una rendadora', 'Fer el deures de BigData', 'Comprar Formatge', 'Netegar la pissara', 'Anara a casa caminant', 'Afagir a Spotify una canço'];
  const [contratos, setContratos] = useState(items);

  const sss = (contrato: string) => {
    let indice = contratos.indexOf(contrato);
    items.splice(indice, 1); // aplica splice a la copia
    setContratos(items)
    console.log(contrato + " Borrat       " + items);
    };
    const handleAdds = () => {
      setContratos([...contratos, newItem]);
    };

  const handleSelectItem = (item: string) => {
    items.indexOf(item)
    console.log(item);
  }

  return <div>
      <ListGrup handleAdd={handleAdds} items={items} heading="Coses per fer:" AAa={sss} onSelectItem={handleSelectItem}/>
    </div>
}

export default App;

//Alert
/*
import Alert from "./Componets/Alert";
function App() {
  return(
    <div>
      <Alert>
        Hello <span>World</span>
      </Alert>
    </div>
  )
}
export default App;
*/
//Button
/*
import Button from "./Componets/Button"

function App() {
  return (
    <div>
      <Button color="danger" onClick={() => console.log('Clicked')}>Holaa</Button>
    </div>
  );
}
export default App;
*/