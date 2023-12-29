interface Props {
    items: string[];
    onSelectItem: (item: string) => void;
    AAa: (item: string) =>void;
}
import { useState } from "react";

function ListGrup({items, onSelectItem, AAa}: Props) {
// Hook : vol dir que te dades que poden canviar tota l'estona
const [selectedIndex, setSelectedIndex] = useState(0);

    return (
        <>
        
        <ul className="list-group">
            <li className={ 'list-group-item' } ></li>
            {items.length === 0 && <p>Items not found</p>} 
            {items.map((item, index) => (
            <li 
                className={ 'list-group-item'} 
                key={item} 
                onClick={() => {

                    setSelectedIndex(index);
                    delete(items[index]);
                }} 
            >
            {item}
                </li>
            ))}
        </ul>
    </>
    );
}

export default ListGrup;
