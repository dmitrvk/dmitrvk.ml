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
      <div class="social">
        <a href="https://linkedin.com/in/dmitrykalyukov" target="_blank" rel="noopener">
          <img class="social-icon" src="https://simpleicons.org/icons/linkedin.svg" alt="LinkedIn"/>
        </a>
        <a href="https://github.com/dmitrvk" target="_blank" rel="noopener">
          <img class="social-icon" src="https://simpleicons.org/icons/github.svg" alt="GitHub"/>
        </a>
        <a href="https://instagram.com/dmitry.kalyukov" target="_blank" rel="noopener">
          <img class="social-icon" src="https://simpleicons.org/icons/instagram.svg" alt="Instagram"/>
        </a>
        <a href="https://t.me/dmitrvk" target="_blank" rel="noopener">
          <img class="social-icon" src="https://simpleicons.org/icons/telegram.svg" alt="Telegram"/>
        </a>
      </div>
      <Footer />
    </div>
  );
}
