import { MouseEvent, useState } from "react";
interface Props {
  items: string[];
  heading: string;
  onSelectItem: (items: string) => void;
}
function ListGroup({items,heading,onSelectItem}: Props) {
  
  const [selectedIndex, setSelectedIndex] = useState(-1);
  // const [name,setName]= useState('')
  //events handler

  return (
    <>
      <h1>{heading}</h1>
      {items.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {items.map((items,index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={items}
            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(items)
            }}
          >
            {items}
          </li>
        ))}
      </ul>
    </>
  );
}
export default ListGroup;
