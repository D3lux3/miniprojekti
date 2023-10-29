import Ranker from "./components/ranker";
import Generator from "./components/generator";
import './styles/styles.scss';
import Header from "./components/header";
import Footer from "./components/footer";

const App = (): JSX.Element => (
<>
    <Header />
    <Ranker />
    <Generator />
    <Footer />
</>);

export default App;
