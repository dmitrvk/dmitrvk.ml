import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './index.css';
import App from './App';
import Music from "./pages/Music";
import Notes from "./pages/Notes";
import Resume from "./pages/Resume";
import Test from "./pages/Test";

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="resume" element={<Resume />} />
      <Route path="notes" element={<Notes />} />
      <Route path="music" element={<Music />} />
      <Route path="test" element={<Test />} />
    </Routes>
  </BrowserRouter>
);
