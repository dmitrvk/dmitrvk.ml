import { Link } from "react-router-dom";
import Footer from "./components/Footer";
import Social from "./components/Social";

export default function App() {
  return (
    <div className="App">
      <h1>Dmitry Kalyukov</h1>
      <nav>
        <ul>
          <Link to="/resume"><li>Resume</li></Link>
          <Link to="/notes"><li>Notes</li></Link>
          <Link to="/music"><li>Music</li></Link>
          <Link to="/test" className="a-test"><li>Test</li></Link>
        </ul>
      </nav>
      <Social />
      <Footer />
    </div>
  );
}
