import { Link } from "react-router-dom";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="App">
      <h1>Dmitry Kalyukov</h1>
      <nav>
        <ul>
          <Link to="/notes"><li>Notes</li></Link>
          <Link to="/music"><li>Music</li></Link>
          <Link to="/test" className="a-test"><li>Test</li></Link>
        </ul>
      </nav>
      <Footer />
    </div>
  );
}
