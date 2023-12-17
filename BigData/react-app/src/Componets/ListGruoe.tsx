interface Props {
    items: string[];
    onSelectItem: (item: string) => void;
    AAa: (item: string) =>void;
}
import { useState } from "react";

function ListGrup({items, onSelectItem, AAa}: Props) {
// Hook : vol dir que te dades que poden canviar tota l'estona
const [selectedIndex, setSelectedIndex] = useState(-1);

    return (
        <>
        
        <ul className="list-group">
            <li className={ 'list-group-item' } ></li>
            {items.length === 0 && <p>Items not found</p>} 
            {items.map((item, index) => (
            <li 
                className={ /*selectedIndex === index ? 'list-group-item ': */'list-group-item'} 
                key={item} 
                onClick={() => {
                    setSelectedIndex(index);
                    onSelectItem(item)
                }} 
            ><input type="checkbox" name="index" onChange={() => AAa(item) } />
            {item}
                </li>
            ))}
        </ul>
    </>
    );
}

export default ListGrup;
