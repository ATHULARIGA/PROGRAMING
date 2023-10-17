// import ListGroup from "./components/ListGroup";

// function App() {
//   let items = ["New york", "San Francisco", "Tokyo", "London ", "Paris"];
//   const handleSelectItem = (item: string) => {
//     console.log(item);
//   };
//   return (
//     <div>
//       <ListGroup items={items} heading="cities" onSelectItem={handleSelectItem} />
//     </div>
//   );
// }
// export default App;

import Alert from "./components/Alert";
import Button from "./components/Button";
function App() {
  return (
    <div>
       <Button color='danger
       'onClick={()=>console.log("clicked")}>My Button</Button>
    </div>
  );
}
export default App;
