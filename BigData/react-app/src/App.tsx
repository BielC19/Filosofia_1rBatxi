import React, { useState } from 'react';
import ListGrup from "./Componets/ListGruoe";


function App() {
  const [inputValue, setInputValue] = useState<string>('');
  const [items, setItems] = useState<string[]>([]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleAddItem = () => {
    setItems([...items, inputValue]);
    setInputValue('');
  };



  const [contratos, setContratos] = useState(items);

  const sss = (contrato: string) => {
    let indice = contratos.indexOf(contrato);
    items.splice(indice,0); // aplica splice a la copia
    setContratos(items)
    console.log(contrato + " Borrat       " + items);
    };

  const handleSelectItem = (item: string) => {
    items.indexOf(item)
    console.log(item);
  }

  return(
    <div>
      <h1>Coses per fer:</h1>
      <div className='btnInp'>
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        />
        <button onClick={handleAddItem}>Add Item</button>
      </div>
      <ListGrup  items={items} AAa={sss} onSelectItem={handleSelectItem}/>
    </div>
  )
}

export default App;
