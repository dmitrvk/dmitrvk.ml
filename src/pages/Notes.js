import Footer from "../components/Footer";

function fillNotesList(data) {
  let notes = document.getElementById('notes');
  notes.innerHTML = '';

  for (let i = 0; i < data.length; i++) {
    let pdf_name = data[i].name.replace('.tex', '.pdf');
    let pdf_url = 'https://docs.google.com/viewer?url=https://dmitrvk.ml/notes/' + pdf_name;
    let note_name = pdf_name.replace('.pdf', '');

    notes.innerHTML += `<a href="${pdf_url}"><li>${note_name}</li></a>`;
  }
}

export default function Notes() {
  const api_url = 'https://api.github.com/repos/dmitrvk/notes/contents/notes'

  fetch(api_url)
    .then(response => response.json())
    .then(data => fillNotesList(data))
    .catch(error => console.error(error));

  return (
    <main>
      <h2>Notes</h2>
      <ul id="notes"></ul>
      <Footer />
    </main>
  );
}
