import ListGrup from "./Componets/ListGruoe";
function App() {
  let items = ['Barcelona', 'Tokio', 'Sant Francisco', 'Sant Fausto', 'Sant fost', 'Granollers'];

  const handleSelectItem = (item: string) => {
    console.log(item);
  }

  return <div><ListGrup items={items} heading="Ciutats" onSelectItem={handleSelectItem}/></div>
}

export default App;