import Footer from '../components/Footer';

export default function Music() {
  return (
    <main>
      <h2>Sheet Music</h2>
      <ul id="music">
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/castlejam.pdf">
          <li>Castle Jam</li>
        </a>
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/createdtofly.pdf">
          <li>Created to Fly</li>
        </a>
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/forestlight.pdf">
          <li>Forest Light</li>
        </a>
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/igosomewhere.pdf">
          <li>I Go Somewhere</li>
        </a>
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/june.pdf">
          <li>June</li>
        </a>
        <a href="https://docs.google.com/viewer?url=https://dmitrvk.ml/music/kotiki.pdf">
          <li>Kotiki</li>
        </a>
      </ul>
      <Footer />
    </main>
  );
}
