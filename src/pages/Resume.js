import Footer from '../components/Footer';

export default function Resume() {
  return (
    <main>
      <p>
        <a
          href="https://github.com/dmitrvk"
          target="_blank"
          rel="noreferrer"
        >GitHub</a>
        &emsp; &emsp; &emsp;
        <a
          href="https://linkedin.com/in/dmitrykalyukov"
          target="_blank"
          rel="noreferrer"
        >LinkedIn</a>
        &emsp; &emsp; &emsp;
        <a
          href="https://dmitrvk.ml/public/resume/DmitryKalyukov.pdf"
          target="_blank"
          rel="noreferrer"
        >Download</a>
      </p>
      <p>
        <img
          class="resume"
          src="https://dmitrvk.ml/public/resume/resume.jpg"
          alt="Resume"
        />
      </p>
      <Footer />
    </main>
  );
}
